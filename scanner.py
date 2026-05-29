#!/usr/bin/env python3
"""
Design System Auditor - Scanner Script
Escanea un repositorio y extrae datos para el análisis de design system.
"""

import os
import re
import json
import argparse
from pathlib import Path
from collections import defaultdict
from dataclasses import dataclass, asdict
from typing import List, Dict, Set, Tuple, Optional

# =============================================================================
# CONFIGURACIÓN
# =============================================================================

# Patrones de archivos a analizar
STYLE_EXTENSIONS = {'.css', '.scss', '.less', '.sass'}
COMPONENT_EXTENSIONS = {'.tsx', '.jsx', '.vue', '.svelte'}
TOKEN_EXTENSIONS = {'.css', '.scss', '.ts', '.js', '.json'}

# Carpetas a ignorar
IGNORE_DIRS = {
    'node_modules', '.git', 'dist', 'build', '.next', '.nuxt', 
    'coverage', '__pycache__', '.cache', 'vendor'
}

# Patrones de nombres de carpetas de tokens
TOKEN_DIR_PATTERNS = {'tokens', 'theme', 'themes', 'design-tokens', 'styles', 'variables'}

# Patrones de nombres de archivos de tokens
TOKEN_FILE_PATTERNS = {
    'tokens', 'variables', 'theme', 'colors', 'spacing', 
    'typography', 'primitives', 'semantic'
}

# =============================================================================
# REGEX PATTERNS
# =============================================================================

# CSS custom properties
CSS_VAR_DEFINITION = re.compile(r'--([a-zA-Z0-9-]+)\s*:\s*([^;]+);')
CSS_VAR_USAGE = re.compile(r'var\(--([a-zA-Z0-9-]+)\)')

# Valores literales
HEX_COLOR = re.compile(r'#[0-9A-Fa-f]{3,8}\b')
PX_VALUE = re.compile(r'\b\d+px\b')
REM_VALUE = re.compile(r'\b\d+(?:\.\d+)?rem\b')
EM_VALUE = re.compile(r'\b\d+(?:\.\d+)?em\b')
RGBA_VALUE = re.compile(r'rgba?\([^)]+\)')

# Tailwind classes
TAILWIND_CLASS = re.compile(r'\b(text|bg|border|p|m|px|py|mx|my|pt|pb|pl|pr|mt|mb|ml|mr|w|h|rounded|shadow|flex|grid|gap)-[a-zA-Z0-9\[\]/-]+')

# Token level patterns
PRIMITIVE_COLOR = re.compile(r'^(color-)?(blue|red|green|gray|neutral|slate|zinc|stone|orange|amber|yellow|lime|emerald|teal|cyan|sky|indigo|violet|purple|fuchsia|pink|rose|black|white)-\d+$')
PRIMITIVE_SPACING = re.compile(r'^(space|spacing|gap)-\d+$')
PRIMITIVE_SCALE = re.compile(r'^(radius|font|shadow|text)-(xs|sm|md|lg|xl|2xl|3xl|\d+)$')

SEMANTIC_PREFIXES = {'text', 'bg', 'background', 'border', 'surface', 'overlay', 'icon', 'link', 'action', 'status', 'feedback'}
SEMANTIC_SUFFIXES = {'primary', 'secondary', 'tertiary', 'subtle', 'muted', 'strong', 'disabled', 'error', 'success', 'warning', 'info', 'surface', 'elevated'}

COMPONENT_PREFIXES = {
    'button', 'card', 'input', 'modal', 'dropdown', 'tooltip', 'badge', 'alert',
    'avatar', 'checkbox', 'radio', 'switch', 'tab', 'tag', 'chip', 'dialog',
    'drawer', 'popover', 'menu', 'nav', 'header', 'footer', 'sidebar', 'table',
    'list', 'form', 'field', 'select', 'textarea', 'accordion', 'breadcrumb'
}

# =============================================================================
# DATA CLASSES
# =============================================================================

@dataclass
class TokenInfo:
    name: str
    value: str
    file: str
    level: str  # primitive, semantic, component, unknown
    type: str   # color, spacing, radius, shadow, typography, other

@dataclass
class TokenUsage:
    token: str
    file: str
    count: int
    level: str

@dataclass
class LiteralValue:
    value: str
    file: str
    count: int
    type: str  # color, spacing, other

@dataclass
class ComponentAnalysis:
    name: str
    file: str
    tokens_used: List[str]
    token_levels: Set[str]
    literal_values: List[str]
    has_tailwind: bool
    has_inline_styles: bool

@dataclass
class ScanResult:
    # Estructura
    token_dirs: List[str]
    token_files: List[str]
    component_files: List[str]
    style_files: List[str]
    has_platform_dirs: bool
    platform_dirs: List[str]
    
    # Tokens
    token_definitions: List[TokenInfo]
    token_usages: List[TokenUsage]
    literal_values: List[LiteralValue]
    
    # Componentes
    components: List[ComponentAnalysis]
    
    # Métricas calculadas
    total_tokens_defined: int
    total_tokens_used: int
    total_literals: int
    
    # Clasificación
    token_model: str  # none, primitive, semantic, hybrid
    architecture_model: str  # centralized, co-located, multiplatform, hybrid-unstable
    
    # Anti-patrones
    antipatterns: List[Dict]
    
    # Score
    scores: Dict[str, float]
    total_score: float

# =============================================================================
# CLASSIFICATION FUNCTIONS
# =============================================================================

def classify_token_level(name: str) -> str:
    """Clasifica un token en primitive, semantic, component, o unknown."""
    name_lower = name.lower()
    
    # Check component first (most specific)
    for prefix in COMPONENT_PREFIXES:
        if name_lower.startswith(prefix + '-'):
            return 'component'
    
    # Check primitive patterns
    if PRIMITIVE_COLOR.match(name_lower):
        return 'primitive'
    if PRIMITIVE_SPACING.match(name_lower):
        return 'primitive'
    if PRIMITIVE_SCALE.match(name_lower):
        return 'primitive'
    
    # Check semantic patterns
    parts = name_lower.replace('color-', '').split('-')
    if parts[0] in SEMANTIC_PREFIXES:
        return 'semantic'
    if len(parts) > 1 and parts[-1] in SEMANTIC_SUFFIXES:
        return 'semantic'
    
    # Check for numeric suffix (likely primitive)
    if re.search(r'-\d+$', name_lower):
        return 'primitive'
    
    return 'unknown'

def classify_token_type(name: str, value: str) -> str:
    """Clasifica el tipo de token (color, spacing, etc.)."""
    name_lower = name.lower()
    
    if 'color' in name_lower or 'bg' in name_lower or 'text' in name_lower or 'border' in name_lower:
        return 'color'
    if 'space' in name_lower or 'gap' in name_lower or 'padding' in name_lower or 'margin' in name_lower:
        return 'spacing'
    if 'radius' in name_lower or 'rounded' in name_lower:
        return 'radius'
    if 'shadow' in name_lower:
        return 'shadow'
    if 'font' in name_lower or 'text' in name_lower or 'line' in name_lower:
        return 'typography'
    
    # Infer from value
    if HEX_COLOR.search(value) or RGBA_VALUE.search(value):
        return 'color'
    if PX_VALUE.search(value) or REM_VALUE.search(value):
        return 'spacing'
    
    return 'other'

def classify_literal_type(value: str) -> str:
    """Clasifica el tipo de valor literal."""
    if HEX_COLOR.match(value) or RGBA_VALUE.match(value):
        return 'color'
    if PX_VALUE.match(value) or REM_VALUE.match(value) or EM_VALUE.match(value):
        return 'spacing'
    return 'other'

# =============================================================================
# SCANNER FUNCTIONS
# =============================================================================

def should_ignore(path: Path) -> bool:
    """Determina si un path debe ser ignorado."""
    for part in path.parts:
        if part in IGNORE_DIRS:
            return True
    return False

def is_token_file(path: Path) -> bool:
    """Determina si un archivo es probablemente de tokens."""
    name_lower = path.stem.lower()
    for pattern in TOKEN_FILE_PATTERNS:
        if pattern in name_lower:
            return True
    # Check if in a token directory
    for part in path.parts:
        if part.lower() in TOKEN_DIR_PATTERNS:
            return True
    return False

def scan_directory_structure(root: Path) -> Tuple[List[str], List[str], List[str], List[str], bool, List[str]]:
    """Escanea la estructura de directorios."""
    token_dirs = []
    token_files = []
    component_files = []
    style_files = []
    platform_dirs = []
    
    for path in root.rglob('*'):
        if should_ignore(path):
            continue
            
        if path.is_dir():
            name_lower = path.name.lower()
            if name_lower in TOKEN_DIR_PATTERNS:
                token_dirs.append(str(path.relative_to(root)))
            if name_lower == 'platform' or name_lower == 'platforms':
                # Check subdirs
                for subdir in path.iterdir():
                    if subdir.is_dir() and subdir.name.lower() in {'web', 'ios', 'android', 'native', 'tv'}:
                        platform_dirs.append(str(subdir.relative_to(root)))
        
        elif path.is_file():
            suffix = path.suffix.lower()
            rel_path = str(path.relative_to(root))
            
            if suffix in TOKEN_EXTENSIONS and is_token_file(path):
                token_files.append(rel_path)
            
            if suffix in COMPONENT_EXTENSIONS:
                component_files.append(rel_path)
            
            if suffix in STYLE_EXTENSIONS:
                style_files.append(rel_path)
    
    has_platform = len(platform_dirs) >= 2
    return token_dirs, token_files, component_files, style_files, has_platform, platform_dirs

def extract_tokens_from_file(filepath: Path, root: Path) -> Tuple[List[TokenInfo], List[TokenUsage], List[LiteralValue]]:
    """Extrae tokens y valores literales de un archivo."""
    definitions = []
    usages = defaultdict(int)
    literals = defaultdict(int)
    
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return [], [], []
    
    rel_path = str(filepath.relative_to(root))
    
    # Extract definitions
    for match in CSS_VAR_DEFINITION.finditer(content):
        name, value = match.groups()
        level = classify_token_level(name)
        token_type = classify_token_type(name, value)
        definitions.append(TokenInfo(
            name=name,
            value=value.strip(),
            file=rel_path,
            level=level,
            type=token_type
        ))
    
    # Extract usages
    for match in CSS_VAR_USAGE.finditer(content):
        name = match.group(1)
        usages[name] += 1
    
    # Extract literal values
    for pattern, type_name in [(HEX_COLOR, 'color'), (PX_VALUE, 'spacing'), (REM_VALUE, 'spacing')]:
        for match in pattern.finditer(content):
            value = match.group(0)
            literals[(value, type_name)] += 1
    
    usage_list = [
        TokenUsage(
            token=name,
            file=rel_path,
            count=count,
            level=classify_token_level(name)
        )
        for name, count in usages.items()
    ]
    
    literal_list = [
        LiteralValue(
            value=value,
            file=rel_path,
            count=count,
            type=type_name
        )
        for (value, type_name), count in literals.items()
    ]
    
    return definitions, usage_list, literal_list

def analyze_component(filepath: Path, root: Path) -> Optional[ComponentAnalysis]:
    """Analiza un archivo de componente."""
    try:
        content = filepath.read_text(encoding='utf-8', errors='ignore')
    except Exception:
        return None
    
    rel_path = str(filepath.relative_to(root))
    name = filepath.stem
    
    # Extract tokens used
    tokens = list(set(CSS_VAR_USAGE.findall(content)))
    token_levels = set(classify_token_level(t) for t in tokens)
    
    # Extract literals
    literals = []
    for pattern in [HEX_COLOR, PX_VALUE, REM_VALUE]:
        literals.extend(pattern.findall(content))
    literals = list(set(literals))
    
    # Check for Tailwind
    has_tailwind = bool(TAILWIND_CLASS.search(content))
    
    # Check for inline styles
    has_inline = 'style={{' in content or 'style="' in content
    
    return ComponentAnalysis(
        name=name,
        file=rel_path,
        tokens_used=tokens,
        token_levels=token_levels,
        literal_values=literals,
        has_tailwind=has_tailwind,
        has_inline_styles=has_inline
    )

# =============================================================================
# ANALYSIS FUNCTIONS
# =============================================================================

def calculate_token_model(definitions: List[TokenInfo], usages: List[TokenUsage], literals: List[LiteralValue]) -> str:
    """Determina el modelo de tokens."""
    total_usages = sum(u.count for u in usages)
    total_literals = sum(l.count for l in literals)
    
    if total_usages == 0 and total_literals == 0:
        return 'none'
    
    total = total_usages + total_literals
    literal_pct = (total_literals / total * 100) if total > 0 else 0
    
    if literal_pct >= 60:
        return 'none'
    
    if literal_pct >= 30:
        return 'immature'
    
    # Count by level
    level_counts = defaultdict(int)
    for usage in usages:
        level_counts[usage.level] += usage.count
    
    total_tokens = sum(level_counts.values())
    if total_tokens == 0:
        return 'none'
    
    primitive_pct = level_counts['primitive'] / total_tokens * 100
    semantic_pct = level_counts['semantic'] / total_tokens * 100
    component_pct = level_counts['component'] / total_tokens * 100
    
    if primitive_pct >= 70:
        return 'primitive'
    if semantic_pct >= 60:
        return 'semantic'
    if component_pct >= 20 and semantic_pct >= 30:
        return 'hybrid'
    if semantic_pct >= 40:
        return 'semantic'
    
    return 'primitive'

def calculate_architecture_model(token_dirs: List[str], token_files: List[str], 
                                  component_files: List[str], has_platform: bool) -> str:
    """Determina el modelo de arquitectura."""
    if has_platform:
        return 'multiplatform'
    
    # Check for co-located tokens
    colocated_count = 0
    for tf in token_files:
        parts = Path(tf).parts
        if 'components' in parts or any(p.lower() in COMPONENT_PREFIXES for p in parts):
            colocated_count += 1
    
    centralized_count = 0
    for tf in token_files:
        parts = Path(tf).parts
        if any(p.lower() in TOKEN_DIR_PATTERNS for p in parts):
            centralized_count += 1
    
    total = colocated_count + centralized_count
    if total == 0:
        return 'none'
    
    colocated_pct = colocated_count / total * 100
    
    if colocated_pct >= 70:
        return 'co-located'
    if colocated_pct <= 30:
        return 'centralized'
    
    return 'hybrid-unstable'

def detect_antipatterns(components: List[ComponentAnalysis], 
                        definitions: List[TokenInfo],
                        usages: List[TokenUsage]) -> List[Dict]:
    """Detecta anti-patrones."""
    antipatterns = []
    
    # AP-01: Mezcla de niveles en mismo componente
    for comp in components:
        levels = {l for l in comp.token_levels if l != 'unknown'}
        if len(levels) >= 2:
            antipatterns.append({
                'id': 'AP-01',
                'name': 'Mezcla de niveles en mismo componente',
                'severity': 'high',
                'file': comp.file,
                'details': f"Componente {comp.name} usa tokens de niveles: {', '.join(levels)}"
            })
    
    # AP-02: Primitives en componentes de alto nivel
    for comp in components:
        if comp.name.lower() in COMPONENT_PREFIXES:
            primitive_count = sum(1 for t in comp.tokens_used if classify_token_level(t) == 'primitive')
            if primitive_count >= 3:
                antipatterns.append({
                    'id': 'AP-02',
                    'name': 'Primitives en componentes de alto nivel',
                    'severity': 'medium',
                    'file': comp.file,
                    'details': f"Componente {comp.name} usa {primitive_count} primitives directamente"
                })
    
    # AP-08: Mezcla de sistemas
    for comp in components:
        if comp.has_tailwind and len(comp.tokens_used) > 0 and len(comp.literal_values) > 0:
            antipatterns.append({
                'id': 'AP-08',
                'name': 'Mezcla de sistemas (Tailwind + tokens + literales)',
                'severity': 'high',
                'file': comp.file,
                'details': f"Componente {comp.name} mezcla Tailwind, CSS variables y valores literales"
            })
    
    # AP-09: Valores mágicos excesivos
    for comp in components:
        if len(comp.literal_values) >= 4:
            antipatterns.append({
                'id': 'AP-09',
                'name': 'Valores mágicos excesivos',
                'severity': 'medium',
                'file': comp.file,
                'details': f"Componente {comp.name} tiene {len(comp.literal_values)} valores literales"
            })
    
    # AP-10: Tokens huérfanos
    defined_tokens = {d.name for d in definitions}
    used_tokens = {u.token for u in usages}
    orphans = defined_tokens - used_tokens
    if orphans:
        antipatterns.append({
            'id': 'AP-10',
            'name': 'Tokens huérfanos',
            'severity': 'low',
            'details': f"{len(orphans)} tokens definidos pero no usados: {', '.join(list(orphans)[:5])}{'...' if len(orphans) > 5 else ''}"
        })
    
    # AP-04: Tokens duplicados (mismo nombre, distintos valores)
    token_values = defaultdict(set)
    for d in definitions:
        token_values[d.name].add(d.value)
    
    duplicates = {name: values for name, values in token_values.items() if len(values) > 1}
    if duplicates:
        for name, values in list(duplicates.items())[:3]:
            antipatterns.append({
                'id': 'AP-04',
                'name': 'Token con definiciones contradictorias',
                'severity': 'high',
                'details': f"Token --{name} tiene {len(values)} valores distintos"
            })
    
    return antipatterns

def calculate_scores(components: List[ComponentAnalysis],
                     definitions: List[TokenInfo],
                     usages: List[TokenUsage],
                     literals: List[LiteralValue],
                     antipatterns: List[Dict],
                     token_files: List[str]) -> Tuple[Dict[str, float], float]:
    """Calcula los scores de salud."""
    scores = {}
    
    # Consistencia de niveles (30%)
    components_with_mix = sum(1 for c in components if len({l for l in c.token_levels if l != 'unknown'}) >= 2)
    total_components = len(components) if components else 1
    scores['consistency'] = 100 - (components_with_mix / total_components * 100)
    
    # Cobertura de tokens (25%)
    total_usages = sum(u.count for u in usages)
    total_literals = sum(l.count for l in literals)
    total = total_usages + total_literals
    scores['coverage'] = (total_usages / total * 100) if total > 0 else 0
    
    # Centralización (20%)
    unique_dirs = len(set(str(Path(f).parent) for f in token_files))
    centralization_penalty = min(unique_dirs - 1, 5) * 15  # -15 por cada dir extra, max -75
    scores['centralization'] = max(100 - centralization_penalty, 25)
    
    # Tokens activos (15%)
    defined = len(set(d.name for d in definitions))
    used = len(set(u.token for u in usages))
    scores['active_tokens'] = (used / defined * 100) if defined > 0 else 100
    
    # Sin duplicados (10%)
    token_values = defaultdict(set)
    for d in definitions:
        token_values[d.name].add(d.value)
    duplicates = sum(1 for values in token_values.values() if len(values) > 1)
    scores['no_duplicates'] = 100 - (duplicates / max(len(token_values), 1) * 100)
    
    # Calcular score total
    weights = {
        'consistency': 0.30,
        'coverage': 0.25,
        'centralization': 0.20,
        'active_tokens': 0.15,
        'no_duplicates': 0.10
    }
    
    total_score = sum(scores[k] * weights[k] for k in weights)
    
    # Penalizar por anti-patrones
    severity_penalties = {'high': 5, 'medium': 2, 'low': 0.5}
    antipattern_penalty = sum(severity_penalties.get(ap['severity'], 0) for ap in antipatterns)
    antipattern_penalty = min(antipattern_penalty, 30)  # Max -30
    
    total_score = max(total_score - antipattern_penalty, 0)
    
    return scores, round(total_score, 1)

# =============================================================================
# MAIN SCANNER
# =============================================================================

def scan(root_path: str) -> ScanResult:
    """Ejecuta el escaneo completo."""
    root = Path(root_path).resolve()
    
    if not root.exists():
        raise ValueError(f"Path does not exist: {root}")
    
    # Fase 1: Escanear estructura
    token_dirs, token_files, component_files, style_files, has_platform, platform_dirs = scan_directory_structure(root)
    
    # Fase 2: Extraer tokens
    all_definitions = []
    all_usages = []
    all_literals = []
    
    files_to_scan = set(token_files + style_files + component_files)
    for rel_path in files_to_scan:
        filepath = root / rel_path
        if filepath.exists():
            defs, usages, lits = extract_tokens_from_file(filepath, root)
            all_definitions.extend(defs)
            all_usages.extend(usages)
            all_literals.extend(lits)
    
    # Fase 3: Analizar componentes
    components = []
    for rel_path in component_files:
        filepath = root / rel_path
        if filepath.exists():
            comp = analyze_component(filepath, root)
            if comp:
                components.append(comp)
    
    # Fase 4: Clasificar
    token_model = calculate_token_model(all_definitions, all_usages, all_literals)
    architecture_model = calculate_architecture_model(token_dirs, token_files, component_files, has_platform)
    
    # Fase 5: Detectar anti-patrones
    antipatterns = detect_antipatterns(components, all_definitions, all_usages)
    
    # Fase 6: Calcular scores
    scores, total_score = calculate_scores(
        components, all_definitions, all_usages, all_literals, antipatterns, token_files
    )
    
    return ScanResult(
        token_dirs=token_dirs,
        token_files=token_files,
        component_files=component_files,
        style_files=style_files,
        has_platform_dirs=has_platform,
        platform_dirs=platform_dirs,
        token_definitions=all_definitions,
        token_usages=all_usages,
        literal_values=all_literals,
        components=components,
        total_tokens_defined=len(set(d.name for d in all_definitions)),
        total_tokens_used=len(set(u.token for u in all_usages)),
        total_literals=len(all_literals),
        token_model=token_model,
        architecture_model=architecture_model,
        antipatterns=antipatterns,
        scores=scores,
        total_score=total_score
    )

def result_to_dict(result: ScanResult) -> dict:
    """Convierte el resultado a diccionario para JSON."""
    return {
        'structure': {
            'token_dirs': result.token_dirs,
            'token_files': result.token_files[:20],  # Limitar para output
            'component_files_count': len(result.component_files),
            'style_files_count': len(result.style_files),
            'has_platform_dirs': result.has_platform_dirs,
            'platform_dirs': result.platform_dirs
        },
        'metrics': {
            'total_tokens_defined': result.total_tokens_defined,
            'total_tokens_used': result.total_tokens_used,
            'total_literals': result.total_literals,
            'components_analyzed': len(result.components)
        },
        'classification': {
            'token_model': result.token_model,
            'architecture_model': result.architecture_model
        },
        'scores': result.scores,
        'total_score': result.total_score,
        'antipatterns': result.antipatterns,
        'top_tokens': [
            {'name': u.token, 'count': u.count, 'level': u.level}
            for u in sorted(result.token_usages, key=lambda x: -x.count)[:15]
        ],
        'token_levels_distribution': {
            level: sum(1 for d in result.token_definitions if d.level == level)
            for level in ['primitive', 'semantic', 'component', 'unknown']
        }
    }

# =============================================================================
# CLI
# =============================================================================

def main():
    parser = argparse.ArgumentParser(description='Design System Auditor Scanner')
    parser.add_argument('--root', '-r', default='.', help='Root directory to scan')
    parser.add_argument('--output', '-o', help='Output JSON file')
    parser.add_argument('--verbose', '-v', action='store_true', help='Verbose output')
    
    args = parser.parse_args()
    
    print(f"🔍 Scanning: {args.root}")
    
    try:
        result = scan(args.root)
        output = result_to_dict(result)
        
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(output, f, indent=2)
            print(f"📄 Results saved to: {args.output}")
        else:
            print(json.dumps(output, indent=2))
        
        # Summary
        print("\n" + "="*50)
        print("📊 SUMMARY")
        print("="*50)
        print(f"Score: {result.total_score}/100")
        print(f"Token Model: {result.token_model}")
        print(f"Architecture: {result.architecture_model}")
        print(f"Tokens defined: {result.total_tokens_defined}")
        print(f"Tokens used: {result.total_tokens_used}")
        print(f"Literals found: {result.total_literals}")
        print(f"Anti-patterns: {len(result.antipatterns)}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        raise

if __name__ == '__main__':
    main()
