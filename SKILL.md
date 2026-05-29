---
name: design-system-auditor
description: >-
  Audita y puntua Design Systems analizando codigo fuente. Usa esta skill
  cuando el usuario quiera evaluar la madurez de su design system, analizar
  tokens CSS/JS, detectar anti-patrones, obtener un score de salud, o planificar
  una migracion entre modelos de design system. Triggers incluyen frases como
  auditar design system, analizar tokens, score del sistema de diseno, migrar a
  semantic tokens, evaluar arquitectura de componentes, detectar anti-patrones
  CSS, health check del DS, o cualquier mencion de tokens, design systems, o
  arquitectura de estilos en contexto de evaluacion.
---

# Design System Auditor

Audita un Design System desde el código fuente. Genera un diagnóstico contextualizado: qué modelo tiene, a qué se parece, qué problemas tiene, y qué hacer — respaldado por casos reales.

> **REGLA ABSOLUTA — leer antes de hacer cualquier cosa:**
> No leer ningún archivo del repositorio. No ejecutar ningún comando. No analizar ningún código.
> La auditoría EMPIEZA con preguntas al usuario (Fase 0). Solo después de recibir las respuestas se puede continuar con Fase 1.
> Si el usuario ya proporcionó contexto suficiente (fase de empresa, tamaño del equipo, plataformas, productos), mencionar qué se asumió y preguntar si falta algo antes de continuar.

---

## FASE 0 — Contexto (siempre primero)

Hacer las preguntas obligatorias al usuario. Esperar respuesta. Recién ahí avanzar a Fase 1.

### Preguntas obligatorias (siempre hacer)

**EQUIPO**

1. **¿Cuántos diseñadores y cuántos frontend/full-stack engineers?**
   - Pre-seed: 1–2 diseño, <10 devs · Seed: 2–5 diseño, 10–30 devs · Serie A: 5–10 diseño, 30–100 devs · Serie B+: 10+ diseño, 100+ devs
   - Si <3 diseñadores o <15 devs: formalizaciones mínimas; prioridad es momentum.

2. **¿En qué fase está la empresa?** (Pre-seed / Seed / Serie A / Serie B / Growth / Enterprise)

**PRODUCTO**

3. **¿Cuántos productos o apps distintas usan este sistema?**
   - 1 producto = sin presión global. Múltiples = punto de dolor.

4. **¿Plataformas?** (solo web / web + mobile / web + mobile + otras)
   - Si incluye mobile: ¿nativo (iOS/Android) o cross-platform (RN, Flutter)?

### Preguntas adicionales por dimensión (seleccionar según fase)

**EQUIPO**

5. **¿Quién es dueño del design system?** (nombre, rol) — sin owner = sin gobernanza.
6. **¿Hay proceso formal diseño→código?** (Figma, specs, handoff manual)
7. *(Seed+)* **¿Cómo se hace code review para cambios visuales/tokens?**
8. *(Seed+)* **¿Separación entre DS team y product teams?**
9. *(Serie A+)* **¿Hay gobernanza de tokens?** ¿Quién puede crear tokens nuevos?
10. *(Serie A+)* **¿Cuánto tarda agregar un token nuevo?** — si >2 semanas: gobernanza reactiva.
11. *(Enterprise)* **¿Hay equipos usando diferentes DS?** — oportunidad de unificación.

**PRODUCTO**

12. **¿Estado actual del DS?** (no existe / básico / en transición / maduro)
13. **¿Hay rebrand o cambio visual importante en roadmap?** — si SÍ: timing crítico.
14. **¿Una marca o múltiples?** (sub-branded, white-label, marketplace)
15. *(Serie A+ o >2 productos)* **¿Qué % de UI está en el DS actual?** — <30% sin tracción, >70% buena adopción.
16. *(Serie A+)* **¿Hay APIs internas o monorepo?** — determina si arquitectura centralizada es posible.
17. *(Con historial de rebrands)* **¿Cuántos rebrands totales? ¿En cuánto tiempo?**

**TÉCNICA**

18. **¿Qué estrategia usan ahora?** (valores literales / primitivos / semánticos / otro)
19. **¿Stack principal?** (React / Vue / Angular / Svelte / otros)
20. **¿CSS o CSS-in-JS?** (CSS / SCSS / CSS Modules / Tailwind / styled-components / Panda / otro)
21. *(Seed+)* **¿Tienen deuda técnica documentada en el DS?** — cuál es.
22. *(Seed+)* **¿Herramientas de análisis en CI/CD?** (linting, tests de accesibilidad, análisis de duplicación)
23. *(Serie A+)* **¿Cómo se versionan tokens y componentes?** — sin versioning = cambios rompen product teams.
24. *(Serie A+)* **¿Documentación de componentes?** (Storybook, etc.)
25. *(Multiplataforma)* **¿Build pipeline para multi-plataforma?** ¿Manual o automatizado?
26. *(CSS-in-JS o custom vars)* **¿Tokens generados de una única fuente o múltiples sitios?**
27. *(Migración planeada)* **¿Hay plan de migración existente?**

**NEGOCIO**

28. *(Si hay iniciativa planeada)* **¿Hay presupuesto reservado para mejorar el DS?**
29. **¿Cuál es el roadmap de productos en los próximos 6 meses?**
30. *(Si hay inconsistencias visibles)* **¿Cuánto tiempo pierde el equipo por inconsistencias visuales?**
31. *(Multi-equipo o multiplataforma)* **¿Cuáles son los mayores friction points?** (onboarding, cambios globales, coordinación)

### Guía de selección por fase

| Fase | Preguntas mínimas | Modelo de referencia |
|------|------------------|----------------------|
| Pre-seed (<10 personas) | 1–4, 5, 12, 18–20. Omitir gobernanza y multi-equipo. | GitHub 2011–2015 |
| Seed (10–50 personas) | 1–4, 5, 12–14, 18–22. Agregar 7 y 21. | Atlassian 2012 |
| Serie A (50–200 personas) | 1–4, 5, 12–24, 28–30. Foco en fragmentación y ownership. | Shopify pre-2017 |
| Serie B / Growth (200–1000) | Todas excepto Enterprise-only (9, 11). | Shopify 2017+ (Polaris) |
| Enterprise (1000+) | Todas. Agregar gobernanza multi-región, soporte partners. | IBM Carbon / Microsoft Fluent |

### Señales de alerta que cambian el enfoque

**🔴 Rojo — bloquea o reorienta la auditoría**

1. "No existe DS" + equipo >20 personas + >2 productos → no auditar tokens; primero mapear qué existe y proponer arquitectura base.
2. "No hay código fuente accesible" → solo checklist self-service.
3. "Diseños y código nunca sincronizados" → agregar Figma→código workflow como prerequisito.

**🟡 Amarillo — cambia el enfoque**

4. "Intentamos migrar y fue un desastre" → indagar por qué; enfocar en lecciones.
5. "Equipos en múltiples países con gustos distintos" → no es problema de tokens, es gobernanza.
6. "Migración a plataforma en próximos 3 meses" → plan "post-migración", no "ahora".
7. "Nuevo Head of Design/CTO reciente" → preguntar qué cambios plantea antes de recomendar.
8. "No hay comunicación Design↔Eng" → problema organizacional primero.
9. Producto financiero, salud o regulado → foco en WCAG/compliance, no velocidad.
10. "Queremos hacer white-label" → tokens semánticos son obligatorios; cambio de arquitectura.

**Salida esperada de Fase 0:**
- Contexto demográfico: equipo, fase, productos, plataformas
- Modelo de referencia elegido (sección **Benchmarks** más abajo)
- Señales de alerta identificadas que modifiquen el scope

---

## FASE 1 — Escaneo del repositorio

```bash
# Archivos de tokens
find . -type f \( -name "*.tokens.*" -o -name "variables.css" -o -name "theme*.css" -o -name "theme*.ts" -o -name "tokens.json" -o -path "*/tokens/*" \) 2>/dev/null | head -50

# Componentes
find . -type f \( -name "*.tsx" -o -name "*.vue" -o -name "*.svelte" \) -path "*/components/*" 2>/dev/null | head -50

# Estructura de carpetas relevante
find . -type d \( -name "tokens" -o -name "theme" -o -name "design-system" -o -name "platform" -o -name "primitives" -o -name "semantic" \) 2>/dev/null

# CSS custom properties usadas
grep -roh "var(--[a-zA-Z0-9-]*)" --include="*.css" --include="*.scss" --include="*.tsx" . | sort | uniq -c | sort -rn | head -50

# Valores literales (hex)
grep -roh "#[0-9A-Fa-f]\{3,6\}" --include="*.css" --include="*.scss" --include="*.tsx" . | sort | uniq -c | sort -rn | head -30

# Valores literales (px/rem)
grep -roh "[0-9]\+\(px\|rem\|em\)" --include="*.css" --include="*.scss" --include="*.tsx" . | sort | uniq -c | sort -rn | head -30
```

---

## FASE 1b — Análisis de arquitectura de componentes

Corre en paralelo (o inmediatamente después) de la Fase 1. Analiza la estructura interna de los componentes como segundo eje de auditoría.

**Qué computar (9 métricas clave):**

| Métrica | Healthy | Warning | Crítico |
|---------|---------|---------|---------|
| LOC por componente | < 200–300 | 300–500 | > 500 |
| Complejidad ciclomática | < 10 | 10–20 | > 20 |
| Complejidad cognitiva | < 15 | 15–25 | > 25 |
| Props por componente | < 7–10 | 10–15 | > 15 |
| `useState` por componente | < 3 | 3–5 | > 5 |
| Reuse rate (cobertura UI) | > 80% | 50–80% | < 50% |
| Code duplication | < 2% | 2–4% | > 4% |
| Dependencies fan-out | Moderado | Alto | Circular |
| Test coverage DS | > 80% | 60–80% | < 60% |

**Anti-patrones a detectar (AP-6 a AP-10):**

| Código | Anti-patrón | Señal principal |
|--------|-------------|-----------------|
| AP-6 | God Component | LOC > 500 o CC > 15 + `useState` > 4 |
| AP-7 | Prop Drilling | Props cruzan > 3 capas sin consumirse en intermedios |
| AP-8 | Component Duplication | jscpd reporta > 4% o variantes similares del mismo elemento |
| AP-9 | Over-Abstraction | > 15 props o > 10 boolean flags en un componente |
| AP-10 | Tight Coupling | Dependencias circulares o alto fan-out en dependency-cruiser |

**Identificar el tier de patrón moderno usado:**
- ¿El codebase usa Atomic Design, Compound Components, o Headless Components?
- ¿Qué patrones están ausentes? (ej: todo es monolítico, sin composición)

**Comandos de apoyo:**
```bash
# Detección de duplicación
jscpd --min-tokens 50 --languages javascript ./src

# Análisis de dependencias y ciclos
depcruise --output-type text src/

# LOC por archivo de componente
find . -path "*/components/*" \( -name "*.tsx" -o -name "*.vue" \) | xargs wc -l | sort -rn | head -30
```

**Output de esta fase:** Lista de componentes con métricas fuera de umbral, anti-patrones AP-6 a AP-10 detectados, y tier de arquitectura identificado. Esta información alimenta el sub-score de **componentes (30%)** en la Fase 5.

---

## FASE 2 — Clasificación de tokens

### Cómo identificar el nivel de un token por su nombre

**PRIMITIVE** — valor crudo, sin intención de uso
- Patrón: `<color-base>-<escala>` o `<propiedad>-<escala>`
- Ejemplos: `blue-500`, `gray-900`, `space-4`, `radius-md`, `font-sm`
- Colores base: `blue red green gray neutral slate zinc orange amber yellow lime emerald teal cyan sky indigo violet purple fuchsia pink rose black white`
- Escalas numéricas: `50 100 200 300 400 500 600 700 800 900 950`
- Escalas de tamaño: `xs sm md lg xl 2xl 3xl`

**SEMANTIC** — nombra intención, no valor
- Patrón: `color-<contexto>-<variante>` o `<propiedad>-<contexto>`
- Prefijos de contexto: `text- bg- background- border- surface- overlay- action- status- feedback- icon- link-`
- Sufijos de intención: `-primary -secondary -tertiary -subtle -muted -strong -surface -elevated -disabled -focus -error -success -warning`
- Ejemplos: `color-text-primary`, `color-bg-surface`, `color-action-primary`, `spacing-content`

**COMPONENT** — específico de un componente UI
- Patrón: `<componente>-<propiedad>` o `<componente>-<estado>-<propiedad>`
- Prefijos: `button- card- input- modal- dropdown- tooltip- badge- alert- avatar- checkbox- radio- switch- tab- tag- chip- dialog- drawer- popover- menu- nav- header- footer- sidebar- table- list- form- field-`
- Ejemplos: `button-bg`, `button-hover-bg`, `card-radius`, `input-focus-border`

### Árbol de decisión rápido

```
¿Empieza con nombre de componente UI?
  SÍ → COMPONENT
  NO → ¿Tiene sufijo numérico o escala (xs/sm/md/lg)?
         SÍ → ¿Prefijo es color base (blue, gray...)?
                SÍ → PRIMITIVE
                NO → ¿Prefijo indica contexto (text, bg, border)?
                       SÍ → SEMANTIC
                       NO → PRIMITIVE
         NO → ¿Contiene palabras de intención (primary, surface, subtle)?
                SÍ → SEMANTIC
                NO → ¿Contiene contexto (text, bg, border)?
                       SÍ → SEMANTIC
                       NO → INDETERMINADO
```

### Casos ambiguos

| Token | Resolución |
|-------|------------|
| `color-primary` | Primitive con alias — señalar como deuda semántica |
| `text-sm` | Depende: si es `font-size` → primitive; si es color de texto → revisar |
| `spacing-lg` | Primitive (escala sin contexto) |
| `spacing-content` | Semantic (contexto de uso explícito) |

---

## FASE 3 — Clasificación del modelo

### Modelo de tokens

| Señal | Clasificación |
|-------|---------------|
| ≥60% valores literales en componentes | **Sin tokens** |
| 30–59% valores literales | **Tokens inmaduros** |
| <30% literales, ≥70% uso de primitives | **Token-first primitivo** |
| <30% literales, ≥60% semantic tokens | **Semantic-first** |
| <30% literales, 3 niveles claros, ninguno >60% | **Hybrid** |

### Modelo de arquitectura

| Señal | Clasificación |
|-------|---------------|
| 100% de tokens en `tokens/` o `design-system/tokens/` | **Centralized** |
| ≥70% de componentes tienen `*.tokens.*` colocado | **Co-located** |
| Existe `platform/` con ≥2 subdirectorios (web, ios, android) | **Multiplatform** |
| 30–70% tokens centrales + 30–70% tokens locales | **Híbrido inestable** |

---

## FASE 3b — Modelo Objetivo

> Referencia: `5__Modelo_Objetivo_y_Decision.md`

La Fase 3 clasificó **dónde está** el sistema. Esta fase determina **dónde debería estar**, dado el contexto específico del usuario.

**Pasos:**

1. Revisar las respuestas de Fase 0: fase de empresa, número de marcas, productos, plataformas, tamaño del equipo de diseño, rebrand y dark mode en roadmap.
2. Aplicar las matrices de decisión del documento `5__Modelo_Objetivo_y_Decision.md`:
   - Matriz 5.2 → modelo objetivo de **tokens**
   - Matriz 5.3 → modelo objetivo de **arquitectura**
3. Construir el argumento prescriptivo: "dado que [contexto], el modelo correcto es [X] porque [razones]". Anclar cada razón en el contexto real del usuario, no en generalidades.
4. Identificar lo que **NO** necesitan todavía y por qué, usando la sección 5.4.
5. Listar los triggers concretos para evolucionar al siguiente nivel (sección 5.5).
6. Verificar coherencia con el plan de cambios: ¿las tareas previstas llevan hacia el objetivo, o alguna está sobre-diseñando?

**Output de esta fase:** alimenta el bloque **Current / Target model** (`[[CURRENT_MODEL]]`, `[[TARGET_MODEL]]`) del reporte HTML.

```
Modelo objetivo de tokens:       [nombre]
Modelo objetivo de arquitectura: [nombre]
Por qué este objetivo:           [2–4 razones ancladas en el contexto real]
Lo que NO necesitás todavía:     [lista con razón + trigger para reconsiderar]
Qué ganás al llegar:             [beneficios concretos en lenguaje de negocio]
Cuándo ir más allá:              [triggers específicos]
```

---

## FASE 4 — Detección de anti-patrones

| Código | Anti-patrón | Cómo detectar | Severidad |
|--------|-------------|---------------|-----------|
| AP-01 | Mezcla de niveles en mismo componente | Un componente usa `blue-500` + `color-text-primary` + `button-bg` para el mismo tipo de propiedad | 🔴 Alta |
| AP-02 | Primitives en componentes de alto nivel | `button`, `card`, `modal` usan ≥3 primitives directamente | 🟡 Media |
| AP-03 | Token de componente usado fuera de su componente | `button-radius` aparece en archivos de `card/` | 🔴 Alta |
| AP-04 | Token semántico sin definición | Token usado en componentes pero sin `:root { --token: ... }` visible | 🔴 Alta |
| AP-05 | Fuentes de tokens fragmentadas | ≥3 ubicaciones distintas definen tokens del mismo tipo | 🔴 Alta |
| AP-06 | Redefinición local de tokens globales | `button.tokens.ts` redefine algo ya en `tokens/colors.css` | 🟡 Media |
| AP-07 | Inline styles con valores mágicos | `style={{ color: '#1A73E8' }}` en componentes reutilizables | 🟡 Media |
| AP-08 | Tokens huérfanos | Token definido en `:root` pero con 0 usos en componentes | 🟢 Baja |
| AP-09 | Duplicación de definición | Mismo nombre de token con valores distintos en ≥2 archivos | 🔴 Alta |

---

## FASE 5 — Score de salud

### Fórmula de 3 ejes

```
Score Compuesto = (Tokens × 50%) + (Componentes × 30%) + (Arquitectura × 20%)
```

Presentar **siempre ambos**: score compuesto (para CEO/CTO) + 3 sub-scores (para equipo técnico).

---

### Sub-score Tokens (0–100)

| Métrica | Peso | Fórmula |
|---------|------|---------|
| Cobertura de tokens | 30% | `100 − (literales / total_valores) × 100` |
| Consistencia de nivel | 25% | `100 − (componentes_inconsistentes / total) × 100` |
| Ausencia de huérfanos | 20% | `100 − (tokens_sin_uso / total_tokens) × 100` |
| Centralización | 15% | 1 fuente=100 · 2=80 · 3=50 · 4+=0 |
| Ausencia de duplicación | 10% | `100 − (tokens_duplicados / total_tokens) × 100` |

`Sub-score Tokens = (Cob×0.30) + (Cons×0.25) + (Huérf×0.20) + (Centr×0.15) + (Dupl×0.10)`

**Penalizaciones:**
- AP-01 (mezcla de niveles): −30 pts
- AP-04 (token fuera de su componente): −25 pts
- AP-05 (duplicación de definición global): −40 pts
- Múltiples instancias: primera = 100% · segunda/tercera = 70% · cuarta+ = 50%
- Regla: si un anti-patrón ya está capturado en la métrica base (ej: AP-05 capturado en Duplicación), no penalizar dos veces.

---

### Sub-score Componentes (0–100)

| Métrica | Peso | Fórmula |
|---------|------|---------|
| Complejidad (LOC + CC) | 40% | 0% God Components=100 · 1–10%=80 · 11–25%=50 · 26%+=0 |
| Reuse rate | 30% | `(componentes_reutilizables / total) × 100` |
| Code duplication | 20% | <2%=100 · 2–4%=50 · >4%=0 |
| Prop drilling | 10% | depth ≤2=100 · 3–4=75 · 5+=0 |

`Sub-score Componentes = (Comp×0.40) + (Reuse×0.30) + (Dupl×0.20) + (Props×0.10)`

**Penalización:** AP-09 (God Component) si no está capturado en métrica de Complejidad: −35 pts.

---

### Sub-score Arquitectura (0–100)

| Métrica | Peso | Valores |
|---------|------|---------|
| Modelo clasificado | 50% | Centralized/Multiplatform=100 · Hybrid claro=70 · Co-located sin core=50 · Sin tokens=0 |
| Separación de concerns | 30% | 0 redefiniciones no-doc=100 · >10% componentes redefinen=30 |
| Escalabilidad | 20% | Documentación+paths+automation=100 · parcial=70 · no=50 |

`Sub-score Arquitectura = (Modelo×0.50) + (Concerns×0.30) + (Escal×0.20)`

---

### Tabla de interpretación contextualizada por fase

| Score | Pre-seed | Seed/Serie A | Serie B | Enterprise |
|-------|----------|-------------|---------|------------|
| 90–100 | ⭐ Excelente | ⭐ Excelente | ⭐ Excelente | ⭐ Excelente |
| 75–89 | ✅ Aceptable | ✅ Aceptable | 🟡 Necesita atención | ✅ Aceptable |
| 60–74 | 🟡 Monitorear | 🟡 Plan de mejora | 🔴 Crítico | 🔴 Crítico |
| 40–59 | 🔴 Acelerar si posible | 🔴 Plan urgente | 🔴 Crítico | 🔴 Crítico |
| <40 | 🔴 Refactor antes de escala | 🔴 Urgente | 🔴 Falla | 🔴 Falla |

**Labels:** 90–100 = EXCELENTE · 75–89 = BUENO · 60–74 = ACEPTABLE · 40–59 = PROBLEMAS · <40 = DISFUNCIONAL

**Colores para sub-scores y barras:** score ≥75 → `#22c55e` · 60–74 → `#eab308` · <60 → `#ef4444`

**Gauge del hero:** `[[SCORE_RING_DEG]]` = score × 3.6 (ej: 62 → 223deg). El número y label del gauge usan `--c-blue` fijo.

---

### Output esperado de Fase 5

```json
{
  "score_global": 60,
  "label": "ACEPTABLE",
  "score_ring_deg": 216,
  "fase_detectada": "Seed/Serie A",
  "score_verdict": "Aceptable para esta etapa — plan de mejora incremental antes de escalar",
  "sub_scores": {
    "tokens": { "score": 49, "color": "#ef4444" },
    "componentes": { "score": 68, "color": "#eab308" },
    "arquitectura": { "score": 76, "color": "#22c55e" }
  },
  "anti_patrones_detectados": [
    { "id": "AP-04", "instancias": 1, "penalizacion": 25 }
  ],
  "prioridades": ["Tokens", "Componentes", "Arquitectura"]
}
```

---

## FASE 6 — Reporte + result-page.html

### Estructura del reporte HTML (orden visual)

1. **Hero** — contexto Fase 0 + gauge de score + prescripción de modelo (`[[MODEL_PRESCRIPTION]]`: Given… should be… because… when…)
2. **Referencia** — empresa más cercana + diferencias (`[[DIFF_ITEMS]]`)
3. **Modelo actual → objetivo** — dos polos (`[[CURRENT_MODEL]]`, `[[TARGET_MODEL]]`)
4. **ROI** — 3 stats + tabla de áreas
5. **Diagnóstico** — resumen ejecutivo (3 párrafos) + badges de modelo + 3 sub-scores
6. **Anti-patrones** — tabla con columnas Level, AP, nombre, qué es, dónde, velocidad, QA, deuda, riesgo, esfuerzo
7. **Qué NO tocar** — cards con título, razón, cuándo reconsiderar
8. **Action plan** — lista única cronológica: checkbox + tarea + periodo a la derecha; resumen de esfuerzo arriba; riesgos como líneas `step-note`
9. **Métricas post-implementación** — panel filas (métrica / antes / después / cómo medir)
10. **Descarga Markdown** — botón `audit-result.md` (plan accionable para Cursor/Claude)
11. **Scope y firma**

---

### Paso final — Generar result-page.html + audit-result.md

Al terminar el reporte, generar **dos archivos** en el **mismo directorio** (repo del cliente o carpeta del audit):

| Archivo | Audiencia |
|---------|-----------|
| `result-page.html` | Reporte visual completo |
| `audit-result.md` | Plan accionable en el IDE (`@audit-result.md`) |

**Proceso:**
1. Copiar el template HTML al final de este archivo (sección "Template HTML").
2. Reemplazar todos los `[[PLACEHOLDER]]` con los valores reales del audit.
3. Para los bloques dinámicos marcados con `[[*_HTML]]`: generar el HTML completo siguiendo los comentarios del template como guía de formato.
4. Generar `audit-result.md` con el template de la sección "Template audit-result.md" (mismo contenido accionable; **no** duplicar ROI ni referencia visual).
5. En el HTML: reemplazar `[[AUDIT_RESULT_MD]]` dentro de `<script id="audit-md-source">` con el **mismo texto** que `audit-result.md` (fallback si `fetch` falla en `file://`).
6. Escribir `result-page.html` y `audit-result.md`.

**Tabla de placeholders:**

| Placeholder | Fuente |
|-------------|--------|
| `[[CLIENT_NAME]]` | Fase 0 — nombre de la empresa / repo |
| `[[STAT_DESIGNERS]]` / `[[STAT_FRONTEND]]` / `[[STAT_FULLSTACK]]` | Fase 0 — conteos de equipo (usar `—` si desconocido) |
| `[[STAT_APPS]]` / `[[STAT_PLATFORMS]]` | Fase 0 — productos y plataformas |
| `[[COMPANY_PHASE]]` | Fase 0 — fase detectada |
| `[[SCORE_GLOBAL]]` / `[[SCORE_LABEL]]` | Fase 5 — score compuesto y label |
| `[[SCORE_RING_DEG]]` | Fase 5 — `round(score × 3.6)` para el arco del gauge |
| `[[MODEL_PRESCRIPTION]]` | Fase 3b — párrafo bajo el gauge: Given [contexto] → should be [TARGET_MODEL] → because [razones] → when [trigger] (inglés en el reporte) |
| `[[REFERENCE_COMPANY]]` | Empresa de referencia más cercana |
| `[[DIFF_ITEMS]]` | `<li>` por cada diferencia clave |
| `[[CURRENT_MODEL]]` / `[[TARGET_MODEL]]` | Fase 3b — modelo actual y objetivo (tokens + arquitectura resumidos) |
| `[[EXEC_LINE_1/2/3]]` | Resumen ejecutivo (3 párrafos) |
| `[[TOKEN_MODEL]]` / `[[ARCH_MODEL]]` | Fases 2+3 — modelos clasificados |
| `[[TOKEN_MODEL_EVIDENCE]]` / `[[ARCH_MODEL_EVIDENCE]]` | Evidencia concreta del código |
| `[[TOKEN_SCORE]]` / `[[COMP_SCORE]]` / `[[ARCH_SCORE]]` | Fase 5 — sub-scores (número) |
| `[[TOKEN_SCORE_COLOR]]` / `[[COMP_SCORE_COLOR]]` / `[[ARCH_SCORE_COLOR]]` | Fase 5 — color hex |
| `[[TOKEN_IMPACT]]` / `[[COMP_IMPACT]]` / `[[ARCH_IMPACT]]` | Una línea de impacto por eje |
| `[[ANTIPATTERNS_TABLE_ROWS]]` | `<tr>` por anti-patrón (ver formato en template) |
| `[[NOT_TOUCH_HTML]]` | HTML de cards por "qué no tocar" |
| `[[ACTION_PLAN_HTML]]` | Lista unificada action plan (ver formato en template HTML) |
| `[[ACTION_PLAN_MD]]` | Mismo plan en Markdown: `- [ ]` tarea — *periodo*; riesgos sin checkbox |
| `[[TOTAL_PM]]` / `[[CALENDAR_DURATION]]` / `[[DEDICATION]]` | Resumen de esfuerzo (línea bajo el heading Action plan) |
| `[[ROI_ANNUAL_SAVING]]` / `[[ROI_PAYBACK]]` / `[[ROI_YEAR1]]` | Estimación ROI |
| `[[ROI_TABLE_ROWS]]` | `<tr>` por área de ahorro |
| `[[METRICS_ROWS_HTML]]` | Filas `.metrics-row` del panel de métricas |
| `[[SCOPE_NOTE]]` | Supuestos de Fase 0 para el pie de scope |
| `[[AUDIT_DATE]]` / `[[AUDITOR_NAME]]` / `[[AUDITOR_ORG]]` / `[[AUDITOR_EMAIL]]` | Firma |
| `[[AUDIT_VERSION]]` | `Design System Auditor v1.0` |
| `[[AUDIT_RESULT_MD]]` | Cuerpo completo de `audit-result.md` (también embebido en HTML para descarga offline) |

---

## Modelos de referencia

### Estrategia de tokens

| Modelo | En qué consiste | Cuándo usarlo | Quiénes lo usan |
|--------|-----------------|---------------|-----------------|
| **Sin tokens** | Valores literales directos (`#3B82F6`, `16px`) | MVP, prototipo, <5 componentes | — punto de partida, no destino |
| **Token-first primitivo** | Tokens nombran valores crudos: `blue-500`, `space-4` | 1 producto, 1 marca, equipo pequeño | Tailwind (clases), sistemas internos tempranos |
| **Semantic-first** | Tokens nombran intención: `color-text-primary`, `color-bg-surface` | Multi-producto, dark mode, múltiples contextos | Apple (HIG), Spotify (Encore), Atlassian |
| **Hybrid** | 3 niveles: primitive → semantic → component tokens | Plataformas con múltiples equipos y productos | Shopify (Polaris), Microsoft (Fluent), GitHub (Primer) |

### Arquitectura de código

| Modelo | En qué consiste | Cuándo usarlo | Quiénes lo usan |
|--------|-----------------|---------------|-----------------|
| **Centralized** | `tokens/` global + `components/` que solo consumen | Governance central, consistencia sobre velocidad | IBM (Carbon), Shopify (Polaris), Atlassian |
| **Co-located** | Cada componente tiene su `button.tokens.ts` propio | SaaS con foco en velocidad, micro-frontends | Vercel (Geist), Notion, Linear |
| **Multiplatform infra** | Core de tokens → build por plataforma (web/iOS/Android) | App en múltiples plataformas con misma marca | Spotify (Encore), Tesla, Disney |

---

## Benchmarks por perfil

| Fase | Equipo | Modelo recomendado | Referencia real |
|------|--------|--------------------|-----------------|
| Pre-seed / Seed | 1–2 diseñadores, <15 devs, 1 producto | Sin tokens → Primitivo, sin arquitectura formal | GitHub 2011–2015: empezaron con CSS en una Ruby Gem, sin equipo dedicado |
| Seed / Serie A | 3–5 diseñadores, equipo creciendo, 1–2 productos | Primitivo → Semantic, Centralized simple | Atlassian 2012: 5 personas, 12 productos, primer DS fue 20 archivos HTML bajo un escritorio |
| Serie A / Serie B | Múltiples equipos, 2–4 productos | Semantic o Hybrid, Centralized | Shopify pre-2017: inconsistencia entre productos fue el trigger |
| Serie B+ con ecosistema | Plataforma + partners externos | Hybrid (3 niveles), Centralized + open source | Shopify Polaris 2017: lanzado para que partners construyeran apps coherentes |
| Serie B+ multiplataforma | Consumer app en web + mobile + otros | Semantic + Multiplatform infra | Spotify 2018: tenían 22 DS distintos, Encore los unificó con tokens compartidos |
| Growth / Enterprise | Múltiples productos, escala global | Hybrid + Multiplatform | IBM Carbon, Microsoft Fluent |

### Resultados documentados (para respaldar recomendaciones)

| Acción | Resultado típico | Fuente |
|--------|-----------------|--------|
| Formalizar DS desde cero | 20–46% mejora en eficiencia diseño/dev | Smashing Magazine, agregado de Slack, Sparkbox, Klüver |
| Migrar a tokens (primitivos) | 20–30% reducción en tiempo de cambios visuales | Múltiples empresas mid-size |
| Migrar a tokens semánticos | Rebrand en minutos en lugar de meses | Spotify: antes de Encore un rebrand tomaba meses |
| Adopción DS al 80%+ | Cambios globales en semanas | Shopify: rediseño 7 años → desplegado en 10 semanas con 86.6% cobertura |
| Estudio controlado con Carbon (IBM) | Build time 4.2h → 2.0h (47% más rápido) | Sparkbox 2022, estudio controlado con 8 developers |
| Onboarding de nuevos diseñadores | 40% más rápido | Atlassian — con DS documentado vs sin él |

### Cuándo NO formalizar todavía

- Menos de 3 diseñadores — el overhead supera el beneficio
- Menos de 2 productos/apps — no hay suficiente superficie de inconsistencia
- Producto en pivoteo activo — esperar a que el diseño estabilice su identidad visual
- Sin buy-in de ingeniería — un DS sin adopción dev es solo documentación

### Señales de que es el momento correcto

- Diseñadores redibujando los mismos componentes en cada proyecto
- Un bug visual aparece en múltiples lugares simultáneamente
- Onboarding de nuevo diseñador o dev tarda >2 semanas
- Dark mode o rebrand están en el roadmap
- Más de 2 equipos trabajando en paralelo sobre el mismo producto

---

## Migraciones

### Mapa de transiciones válidas

```
Sin tokens → Primitive → Semantic → Hybrid
Centralized → Co-located (con reglas)
Centralized → Multiplatform
```

Nunca saltar pasos hacia adelante sin consolidar el anterior. Las regresiones (Hybrid → Primitive) solo tienen sentido para simplificar sistemas sobre-ingenieriados.

### Sin tokens → Primitive

**Pasos:** inventariar valores únicos → crear escala de colores/spacing/radius en `:root` → reemplazar literales por `var(--token)` progresivamente (primero componentes más usados, un tipo de propiedad a la vez).

**Validación:** ≤30% de valores literales restantes.

**Riesgo:** crear >100 primitives es sobre-ingeniería. Mantener la escala acotada.

**Tiempo típico:** 2–6 semanas para sistema mediano.

---

### Primitive → Semantic

**Pasos:** identificar patrones de uso recurrentes (¿qué primitive siempre se usa para texto principal?) → crear capa semántica que mapea intención a primitives → migrar componentes reemplazando `var(--gray-900)` por `var(--color-text-primary)`.

**Validación:** ≥60% de usos son semantic tokens.

**Riesgo:** crear tokens semánticos 1:1 con primitives (ej: `--color-blue: var(--blue-500)`) — no aportan abstracción real.

**Tiempo típico:** 1–3 meses.

---

### Semantic → Hybrid (añadir component tokens)

**Pasos:** identificar componentes con ≥5 semantic tokens o múltiples variantes complejas → crear component tokens que referencian semantic tokens → establecer regla: component → semantic → primitive (nunca saltar niveles).

**Validación:** cada nivel solo referencia al nivel inmediatamente inferior.

**Riesgo:** crear component tokens para todo (sobre-abstracción). Solo aplicar donde hay variantes reales o estados complejos.

**Tiempo típico:** 1–2 meses por módulo de componentes.

---

### Centralized → Co-located (sin perder gobernanza)

**Pasos:** separar tokens en core (primitives + semantic, centralizados) y component tokens (movidos a carpetas de componentes) → establecer que los component tokens importan del core → definir ownership claro (DS team = core, equipos = component tokens con review).

**Validación:** core tokens no duplicados localmente, component tokens no usados fuera de su componente.

**Riesgo:** equipos redefiniendo core tokens localmente ("shadow tokens").

---

### Single platform → Multiplatform

**Pasos:** convertir tokens a formato agnóstico (JSON/YAML) → usar Style Dictionary o similar para generar outputs por plataforma (CSS, Swift, XML) → establecer que cambios en core hacen rebuild de todas las plataformas.

**Riesgo:** complejidad de build que nadie entiende. Requiere que alguien sea dueño del pipeline.

---

## Notas de uso

- **Solo código:** esta skill analiza código, no Figma ni documentación
- **Agnóstico de framework:** funciona con CSS, SCSS, CSS-in-JS, Tailwind
- **No destructivo:** solo lee, nunca modifica
- **Iterativo:** el usuario puede pedir profundizar en cualquier sección

---

## Template HTML

Usar este template para generar `result-page.html`. Copiar, reemplazar todos los `[[PLACEHOLDER]]` con los valores reales del audit, y generar los bloques `[[*_HTML]]` siguiendo los comentarios como guía de formato.

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Audit DS — [[CLIENT_NAME]]</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet" />
  <style>
    :root {
      --c-bg: #fff;
      --c-panel: #f7f7f7;
      --c-surface: rgba(17, 17, 17, 0.03);
      --c-surface-2: rgba(17, 17, 17, 0.06);
      --c-track: rgba(17, 17, 17, 0.12);
      --c-line: rgba(17, 17, 17, 0.12);
      --c-text: #111;
      --c-text-muted: rgba(17, 17, 17, 0.65);
      --c-text-faint: rgba(17, 17, 17, 0.45);
      --c-blue: #2383e2;
      --c-green: #22c55e;
      --c-yellow: #eab308;
      --c-red: #ef4444;
      --c-warn: #856400;
      --radius-tag: 4px;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: var(--c-bg);
      color: var(--c-text);
      font-family: "Roboto Condensed", "Arial Narrow", Arial, sans-serif;
      font-size: 14px;
      line-height: 1.6;
      padding: 40px 24px 80px;
    }
    .page { max-width: 900px; margin: 0 auto; }
    code {
      font-family: "SF Mono", "Fira Code", monospace;
      font-size: 0.92em;
      background: var(--c-surface-2);
      padding: 0.1em 0.35em;
    }
    .hero-top { display: flex; gap: 16px; align-items: stretch; margin-bottom: 16px; }
    @media (max-width: 720px) { .hero-top { flex-direction: column; } }
    .hero-panel { background: var(--c-panel); padding: 24px; display: flex; flex-direction: column; gap: 32px; }
    .hero-panel.context { flex: 0 0 416px; max-width: 100%; }
    .hero-panel.score { flex: 1; min-width: 0; }
    .hero-eyebrow { font-size: 11px; letter-spacing: 0.08em; text-transform: uppercase; color: var(--c-text); }
    .hero-title { font-family: "Instrument Serif", Georgia, serif; font-size: 48px; font-weight: 400; line-height: 1; color: var(--c-text); }
    .stats-list { display: flex; flex-direction: column; gap: 8px; width: 100%; }
    .stat-row { display: flex; justify-content: space-between; align-items: flex-start; gap: 16px; font-size: 16px; line-height: 24px; color: var(--c-text); }
    .stat-row span:last-child { text-align: right; white-space: nowrap; }
    .stat-divider { height: 1px; background: var(--c-line); border: none; }
    .score-gauge { position: relative; display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 250px; padding: 32px 0; }
    .score-ring {
      position: absolute; width: 214px; height: 214px; border-radius: 50%;
      background: conic-gradient(var(--c-blue) 0deg [[SCORE_RING_DEG]]deg, var(--c-track) [[SCORE_RING_DEG]]deg 360deg);
      -webkit-mask: radial-gradient(farthest-side, transparent calc(100% - 10px), #000 calc(100% - 9px));
      mask: radial-gradient(farthest-side, transparent calc(100% - 10px), #000 calc(100% - 9px));
    }
    .score-number { position: relative; z-index: 1; font-size: 80px; font-weight: 400; line-height: 1; color: var(--c-blue); font-family: "Roboto Condensed", sans-serif; }
    .score-label { position: relative; z-index: 1; font-size: 16px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.065em; color: var(--c-blue); margin-top: 5px; }
    .model-prescription { font-size: 16px; line-height: 24px; color: var(--c-text); }
    .model-prescription strong { font-weight: 600; }
    .block { margin-bottom: 16px; }
    .reference-block { background: var(--c-surface); padding: 20px; display: flex; flex-direction: column; gap: 7px; }
    .reference-block .ref-intro { font-size: 15px; color: var(--c-text-muted); line-height: 24px; }
    .reference-block .ref-name { font-family: "Instrument Serif", Georgia, serif; font-size: 32px; line-height: 1.6; color: var(--c-text); }
    .diff-list { list-style: none; padding-top: 5px; }
    .diff-list li { font-size: 16px; color: var(--c-text-muted); line-height: 25.6px; padding: 6px 0 7px; border-bottom: 1px solid var(--c-line); display: flex; gap: 8px; }
    .diff-list li:last-child { border-bottom: none; }
    .diff-list li::before { content: "↳"; color: var(--c-text-faint); flex-shrink: 0; }
    .target-direction { display: flex; gap: 16px; margin-bottom: 16px; }
    @media (max-width: 600px) { .target-direction { flex-direction: column; } }
    .td-pole { flex: 1; padding: 20px; display: flex; flex-direction: column; gap: 16px; }
    .td-pole.current { background: var(--c-surface); }
    .td-pole.target { background: var(--c-blue); }
    .td-pole-label { font-size: 13px; text-transform: uppercase; letter-spacing: 0.07em; line-height: 20.8px; }
    .td-pole.current .td-pole-label { color: var(--c-text-muted); }
    .td-pole.target .td-pole-label { color: rgba(255, 255, 255, 0.65); }
    .td-pole-model { font-family: "Instrument Serif", Georgia, serif; font-style: italic; font-size: 28px; line-height: 1.25; }
    .td-pole.current .td-pole-model { color: var(--c-text); }
    .td-pole.target .td-pole-model { color: #fff; }
    .section { margin-bottom: 48px; }
    .section-title { font-size: 13px; font-weight: 400; text-transform: uppercase; letter-spacing: 0.1em; color: var(--c-text-muted); margin-bottom: 20px; font-family: "Roboto Condensed", sans-serif; }
    .section-title span { color: var(--c-text-faint); margin-right: 12px; }
    .section-heading { font-family: "Instrument Serif", Georgia, serif; font-size: 48px; font-weight: 400; line-height: 1; color: var(--c-text); padding: 40px 0 8px; margin-bottom: 8px; }
    .exec-summary { background: var(--c-surface); padding: 24px 28px; margin-bottom: 16px; }
    .exec-summary p { font-size: 18px; line-height: 1.55; color: var(--c-text); margin-bottom: 8px; }
    .exec-summary p:last-child { margin-bottom: 0; }
    .model-row { display: flex; gap: 16px; margin-bottom: 16px; flex-wrap: wrap; }
    .model-badge { background: var(--c-surface); padding: 16px 20px; flex: 1; min-width: calc(50% - 8px); }
    @media (max-width: 600px) { .model-badge { min-width: 100%; } }
    .model-badge .badge-label { font-size: 13px; text-transform: uppercase; letter-spacing: 0.07em; color: var(--c-text-faint); margin-bottom: 16px; }
    .model-badge .badge-value { font-family: "Instrument Serif", Georgia, serif; font-size: 24px; line-height: 1.2; color: var(--c-text); margin-bottom: 16px; }
    .model-badge .badge-evidence { font-size: 12px; color: var(--c-text-muted); line-height: 1.45; }
    .subscores { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
    @media (max-width: 600px) { .subscores { grid-template-columns: 1fr; } }
    .subscore-card { background: var(--c-surface); padding: 20px; }
    .subscore-card .axis-name { font-size: 13px; color: var(--c-text-muted); margin-bottom: 16px; line-height: 21px; }
    .subscore-card .axis-score { font-size: 36px; font-weight: 400; line-height: 1; margin-bottom: 16px; font-family: "Roboto Condensed", sans-serif; }
    .subscore-card .axis-weight { font-size: 13px; color: var(--c-text-faint); margin-bottom: 8px; line-height: 21px; }
    .score-bar-track { height: 4px; background: var(--c-track); overflow: hidden; margin-bottom: 16px; }
    .score-bar-fill { height: 100%; }
    .subscore-card .axis-impact { font-size: 12px; color: var(--c-text-muted); line-height: 1.45; }
    .table-wrap { overflow-x: auto; -webkit-overflow-scrolling: touch; background: var(--c-surface); }
    .ap-table { width: 100%; border-collapse: collapse; font-size: 13px; min-width: 1100px; }
    .ap-table th { text-align: left; font-size: 13px; color: var(--c-text-muted); padding: 10px 12px; border-bottom: 1px solid var(--c-line); background: var(--c-surface-2); white-space: nowrap; }
    .ap-table td { padding: 12px; border-bottom: 1px solid var(--c-line); color: var(--c-text-muted); vertical-align: top; line-height: 1.45; }
    .ap-table tr:last-child td { border-bottom: none; }
    .ap-table .col-ap { font-family: "SF Mono", "Fira Code", monospace; font-size: 12px; color: var(--c-text-faint); white-space: nowrap; }
    .ap-table .col-name { color: var(--c-text); font-weight: 500; min-width: 160px; }
    .nivel-tag { display: inline-block; font-size: 13px; font-weight: 500; text-transform: uppercase; letter-spacing: 0.07em; padding: 2px 8px; border-radius: var(--radius-tag); white-space: nowrap; }
    .nivel-tag.alta  { background: var(--c-red); color: #fff; }
    .nivel-tag.media { background: var(--c-yellow); color: #111; }
    .nivel-tag.baja  { background: var(--c-green); color: #111; }
    .not-touch-card { background: var(--c-surface); padding: 24px 20px; margin-bottom: 12px; }
    .not-touch-card .nt-title { font-family: "Instrument Serif", Georgia, serif; font-size: 24px; color: var(--c-text); margin-bottom: 16px; line-height: 1.3; }
    .not-touch-card .nt-reason { font-size: 16px; color: var(--c-text-muted); margin-bottom: 16px; line-height: 1.45; }
    .not-touch-card .nt-when { font-size: 16px; color: var(--c-text-faint); line-height: 1.45; }
    .not-touch-card .nt-when strong { color: var(--c-text-muted); }
    .plan-phase { background: var(--c-surface); padding: 30px 24px 22px; margin-bottom: 12px; }
    .plan-meta-row { display: flex; flex-wrap: wrap; gap: 8px; margin-bottom: 11px; }
    .phase-chip { display: inline-flex; align-items: center; gap: 8px; background: var(--c-surface-2); border-radius: var(--radius-tag); padding: 3px 8px; font-size: 13px; letter-spacing: 0.07em; text-transform: uppercase; color: var(--c-text-muted); }
    .phase-chip strong { font-weight: 700; }
    .deliverable-tag { font-size: 12px; background: var(--c-surface-2); border-radius: var(--radius-tag); padding: 2px 8px; color: var(--c-text-muted); }
    .plan-phase .phase-name { font-family: "Instrument Serif", Georgia, serif; font-size: 24px; color: var(--c-text); margin-bottom: 11px; letter-spacing: 0.02em; }
    .plan-task-list { list-style: none; display: flex; flex-direction: column; gap: 8px; }
    .plan-task-list li { display: flex; align-items: center; gap: 8px; font-size: 13px; color: var(--c-text-muted); padding-bottom: 8px; border-bottom: 1px solid var(--c-line); line-height: 20.8px; }
    .plan-task-list li:last-child { border-bottom: none; padding-bottom: 0; }
    .task-check { width: 16px; height: 16px; flex-shrink: 0; border: 1.5px solid var(--c-text-faint); border-radius: 2px; display: flex; align-items: center; justify-content: center; font-size: 10px; color: var(--c-text); }
    .plan-risk { margin-top: 12px; font-size: 12px; color: var(--c-warn); line-height: 19.2px; opacity: 0.8; }
    .effort-summary { background: var(--c-surface); padding: 24px; display: flex; gap: 32px; flex-wrap: wrap; margin-top: 12px; }
    .effort-item dt { font-size: 13px; color: var(--c-text-muted); margin-bottom: 4px; line-height: 21px; }
    .effort-item dd { font-size: 18px; color: var(--c-text); font-family: "Roboto Condensed", sans-serif; }
    .roi-hero { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 20px; }
    @media (max-width: 600px) { .roi-hero { grid-template-columns: 1fr; } }
    .roi-stat { background: var(--c-surface); padding: 17px 20px; text-align: center; }
    .roi-stat .roi-label { font-size: 13px; color: var(--c-text-muted); margin-bottom: 8px; line-height: 21px; }
    .roi-stat .roi-value { font-size: 28px; font-weight: 400; color: var(--c-blue); font-family: "Roboto Condensed", sans-serif; line-height: 1.2; }
    .roi-stat .roi-sub { font-size: 12px; color: var(--c-text-muted); margin-top: 4px; line-height: 20px; }
    .data-table { width: 100%; border-collapse: collapse; font-size: 13px; background: var(--c-surface); }
    .data-table th { text-align: left; font-size: 12px; color: var(--c-text-muted); padding: 8px 12px; border-bottom: 1px solid var(--c-line); font-weight: 400; }
    .data-table td { padding: 10px 12px; border-bottom: 1px solid var(--c-line); color: var(--c-text-muted); vertical-align: top; }
    .data-table tr:last-child td { border-bottom: none; }
    .data-table .val-highlight { color: var(--c-text); font-weight: 500; }
    .metrics-panel { background: var(--c-surface); padding: 15px 18px 16px; }
    .metrics-head, .metrics-row { display: grid; grid-template-columns: 300px 50px 170px 1fr; gap: 8px; align-items: center; font-size: 16px; color: var(--c-text-muted); }
    @media (max-width: 700px) { .metrics-head, .metrics-row { grid-template-columns: 1fr; gap: 4px; } }
    .metrics-head { padding-bottom: 8px; border-bottom: 1px solid var(--c-line); margin-bottom: 8px; }
    .metrics-row { padding: 8px 0; border-bottom: 1px solid var(--c-line); }
    .metrics-row:last-child { border-bottom: none; }
    .metric-before { font-size: 15px; color: var(--c-text-faint); text-decoration: line-through; }
    .metric-after { font-size: 15px; color: var(--c-blue); }
    .metric-how { font-size: 15px; color: var(--c-text-faint); line-height: 20.8px; }
    .steps-panel { background: var(--c-surface); padding: 27px 24px; }
    .action-plan-summary { font-size: 16px; line-height: 1.5; color: var(--c-text-muted); margin-bottom: 12px; }
    .action-plan-list { list-style: none; }
    .action-plan-list li { display: flex; align-items: flex-start; gap: 12px; padding: 10px 0; border-bottom: 1px solid var(--c-line); font-size: 16px; color: var(--c-text-muted); line-height: 20px; }
    .action-plan-list li:last-child { border-bottom: none; }
    .action-plan-list .step-task { flex: 1; min-width: 0; }
    .action-plan-list .step-period { font-size: 13px; color: var(--c-text-faint); text-transform: lowercase; white-space: nowrap; flex-shrink: 0; padding-top: 2px; }
    .action-plan-list li.step-note { padding-left: 28px; font-size: 13px; line-height: 1.45; color: var(--c-warn); opacity: 0.9; }
    .scope-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; }
    @media (max-width: 600px) { .scope-grid { grid-template-columns: 1fr; } }
    .scope-col { background: var(--c-surface); padding: 15px 18px; }
    .scope-col h4 { font-size: 12px; color: var(--c-text-muted); margin-bottom: 10px; font-family: "Roboto Condensed", sans-serif; }
    .scope-col ul { list-style: none; }
    .scope-col ul li { font-size: 13px; color: var(--c-text-muted); padding: 6px 0; border-bottom: 1px solid var(--c-line); line-height: 21px; }
    .scope-col ul li:last-child { border-bottom: none; }
    .scope-col ul li.covered::before  { content: "✓ "; color: var(--c-green); }
    .scope-col ul li.excluded::before { content: "✗ "; color: var(--c-red); opacity: 0.6; }
    .scope-note { margin-top: 16px; font-size: 12px; color: var(--c-text-faint); line-height: 20px; }
    .signature { background: var(--c-surface); padding: 24px 28px; display: flex; justify-content: space-between; align-items: flex-start; gap: 24px; flex-wrap: wrap; }
    .sig-left .auditor-name { font-family: "Instrument Serif", Georgia, serif; font-size: 16px; color: var(--c-text); margin-bottom: 2px; }
    .sig-left .auditor-org, .sig-left .auditor-email { font-size: 13px; color: var(--c-text-muted); line-height: 21px; }
    .sig-right { text-align: right; }
    .sig-right .sig-detail { font-size: 12px; color: var(--c-text-faint); margin-bottom: 4px; line-height: 20px; }
    .sig-right .sig-version { font-size: 13px; font-family: "SF Mono", "Fira Code", monospace; color: var(--c-text-faint); }
    .download-block { background: var(--c-panel); padding: 28px 24px; display: flex; flex-direction: column; gap: 16px; }
    .download-intro { font-size: 16px; line-height: 1.5; color: var(--c-text-muted); max-width: 52ch; }
    .download-actions { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 20px; }
    .download-btn { font-family: "Roboto Condensed", sans-serif; font-size: 14px; letter-spacing: 0.04em; text-transform: uppercase; color: #fff; background: var(--c-blue); border: none; padding: 10px 18px; cursor: pointer; }
    .download-btn:hover { opacity: 0.92; }
    .download-link { font-size: 14px; color: var(--c-blue); text-decoration: underline; text-underline-offset: 3px; }
    @media print { body { padding: 20px; } .download-block { display: none; } }
  </style>
</head>
<body>
<div class="page">

  <div class="hero-top block">
    <div class="hero-panel context">
      <div>
        <div class="hero-eyebrow">Design System Audit</div>
        <div class="hero-title">[[CLIENT_NAME]]</div>
      </div>
      <div class="stats-list">
        <div class="stat-row"><span>Designers</span><span>[[STAT_DESIGNERS]]</span></div>
        <hr class="stat-divider" />
        <div class="stat-row"><span>Frontend engineers</span><span>[[STAT_FRONTEND]]</span></div>
        <hr class="stat-divider" />
        <div class="stat-row"><span>Full-stack engineers</span><span>[[STAT_FULLSTACK]]</span></div>
        <hr class="stat-divider" />
        <div class="stat-row"><span>Phase</span><span>[[COMPANY_PHASE]]</span></div>
        <hr class="stat-divider" />
        <div class="stat-row"><span>Amount of apps</span><span>[[STAT_APPS]]</span></div>
        <hr class="stat-divider" />
        <div class="stat-row"><span>Platforms</span><span>[[STAT_PLATFORMS]]</span></div>
      </div>
    </div>
    <div class="hero-panel score">
      <div class="hero-eyebrow">Health score</div>
      <div class="score-gauge">
        <div class="score-ring" aria-hidden="true"></div>
        <div class="score-number">[[SCORE_GLOBAL]]</div>
        <div class="score-label">[[SCORE_LABEL]]</div>
      </div>
      <p class="model-prescription">[[MODEL_PRESCRIPTION]]</p>
    </div>
  </div>

  <div class="reference-block block">
    <div class="ref-intro">Your system is closest to:</div>
    <div class="ref-name">[[REFERENCE_COMPANY]]</div>
    <ul class="diff-list">[[DIFF_ITEMS]]</ul>
  </div>

  <div class="target-direction block">
    <div class="td-pole current">
      <div class="td-pole-label">Current model</div>
      <div class="td-pole-model">[[CURRENT_MODEL]]</div>
    </div>
    <div class="td-pole target">
      <div class="td-pole-label">Target model</div>
      <div class="td-pole-model">[[TARGET_MODEL]]</div>
    </div>
  </div>

  <section class="section">
    <h2 class="section-heading">ROI estimated</h2>
    <div class="roi-hero">
      <div class="roi-stat">
        <div class="roi-label">Projected annual savings</div>
        <div class="roi-value">[[ROI_ANNUAL_SAVING]]</div>
        <div class="roi-sub">design + dev + QA + TTM</div>
      </div>
      <div class="roi-stat">
        <div class="roi-label">Payback period</div>
        <div class="roi-value">[[ROI_PAYBACK]]</div>
        <div class="roi-sub">months to recover investment</div>
      </div>
      <div class="roi-stat">
        <div class="roi-label">Year 1 ROI</div>
        <div class="roi-value">[[ROI_YEAR1]]</div>
        <div class="roi-sub">on implementation cost</div>
      </div>
    </div>
    <div class="table-wrap">
      <table class="data-table">
        <thead>
          <tr>
            <th>Area</th>
            <th>Est. savings/year</th>
            <th>Base assumption</th>
            <th>Reference</th>
          </tr>
        </thead>
        <tbody>[[ROI_TABLE_ROWS]]</tbody>
      </table>
    </div>
  </section>

  <h2 class="section-heading">Diagnosis</h2>

  <div class="exec-summary block">
    <p>[[EXEC_LINE_1]]</p>
    <p>[[EXEC_LINE_2]]</p>
    <p>[[EXEC_LINE_3]]</p>
  </div>

  <div class="model-row block">
    <div class="model-badge">
      <div class="badge-label">Token strategy</div>
      <div class="badge-value">[[TOKEN_MODEL]]</div>
      <div class="badge-evidence">[[TOKEN_MODEL_EVIDENCE]]</div>
    </div>
    <div class="model-badge">
      <div class="badge-label">Code architecture</div>
      <div class="badge-value">[[ARCH_MODEL]]</div>
      <div class="badge-evidence">[[ARCH_MODEL_EVIDENCE]]</div>
    </div>
  </div>

  <div class="subscores block">
    <div class="subscore-card">
      <div class="axis-name">Tokens</div>
      <div class="axis-score" style="color:[[TOKEN_SCORE_COLOR]]">[[TOKEN_SCORE]]</div>
      <div class="axis-weight">Weight: 50%</div>
      <div class="score-bar-track"><div class="score-bar-fill" style="width:[[TOKEN_SCORE]]%;background:[[TOKEN_SCORE_COLOR]]"></div></div>
      <div class="axis-impact">[[TOKEN_IMPACT]]</div>
    </div>
    <div class="subscore-card">
      <div class="axis-name">Components</div>
      <div class="axis-score" style="color:[[COMP_SCORE_COLOR]]">[[COMP_SCORE]]</div>
      <div class="axis-weight">Weight: 30%</div>
      <div class="score-bar-track"><div class="score-bar-fill" style="width:[[COMP_SCORE]]%;background:[[COMP_SCORE_COLOR]]"></div></div>
      <div class="axis-impact">[[COMP_IMPACT]]</div>
    </div>
    <div class="subscore-card">
      <div class="axis-name">Architecture</div>
      <div class="axis-score" style="color:[[ARCH_SCORE_COLOR]]">[[ARCH_SCORE]]</div>
      <div class="axis-weight">Weight: 20%</div>
      <div class="score-bar-track"><div class="score-bar-fill" style="width:[[ARCH_SCORE]]%;background:[[ARCH_SCORE_COLOR]]"></div></div>
      <div class="axis-impact">[[ARCH_IMPACT]]</div>
    </div>
  </div>

  <h2 class="section-heading">Anti-patterns detected</h2>

  <div class="table-wrap block">
    <table class="ap-table">
      <thead>
        <tr>
          <th>Level</th>
          <th>AP</th>
          <th>Anti pattern</th>
          <th>What it is</th>
          <th>Where it appears</th>
          <th>Velocity</th>
          <th>QA</th>
          <th>Tech debt</th>
          <th>Risk</th>
          <th>Effort</th>
        </tr>
      </thead>
      <tbody>[[ANTIPATTERNS_TABLE_ROWS]]</tbody>
      <!-- Formato por fila:
      <tr>
        <td><span class="nivel-tag alta">High</span></td>
        <td class="col-ap">AP-XX</td>
        <td class="col-name">Nombre</td>
        <td>Qué es</td>
        <td>Dónde aparece (rutas, archivos)</td>
        <td>Impacto velocidad</td>
        <td>Impacto QA</td>
        <td>Deuda técnica</td>
        <td>Riesgo</td>
        <td>Esfuerzo</td>
      </tr> -->
    </table>
  </div>

  <h2 class="section-heading">What not to touch now</h2>
  [[NOT_TOUCH_HTML]]
  <!-- Formato:
  <div class="not-touch-card">
    <div class="nt-title">Propuesta tentadora</div>
    <div class="nt-reason">Por qué no ahora</div>
    <div class="nt-when"><strong>When to reconsider:</strong> condición</div>
  </div> -->

  <h2 class="section-heading">Action plan</h2>
  <p class="action-plan-summary"><strong>[[TOTAL_PM]]</strong> · <strong>[[CALENDAR_DURATION]]</strong> · [[DEDICATION]]</p>
  <div class="steps-panel block">
    <ul class="action-plan-list">
      [[ACTION_PLAN_HTML]]
      <!-- Tarea:
      <li>
        <span class="task-check" aria-hidden="true"></span>
        <span class="step-task">Descripción</span>
        <span class="step-period">this week</span>
      </li>
      Riesgo:
      <li class="step-note"><span class="step-task">⚠ Risk: ...</span></li> -->
    </ul>
  </div>

  <h2 class="section-heading">Post-implementation metrics</h2>

  <div class="metrics-panel block">
    <div class="metrics-head">
      <span>Metrics</span>
      <span>Before</span>
      <span>After</span>
      <span>Parameter</span>
    </div>
    [[METRICS_ROWS_HTML]]
    <!-- Formato METRICS: <div class="metrics-row"><span>nombre</span><span class="metric-before">X</span><span class="metric-after">Y</span><span class="metric-how">cómo medir</span></div> -->
  </div>

  <section class="download-block block" aria-labelledby="download-heading">
    <h2 class="section-heading" id="download-heading">Continue in your editor</h2>
    <p class="download-intro">Download the actionable plan as Markdown — use it in Cursor or Claude with <code>@audit-result.md</code>.</p>
    <div class="download-actions">
      <button type="button" class="download-btn" id="download-audit-md">Download audit-result.md</button>
      <a class="download-link" href="audit-result.md" download="audit-result.md">Open audit-result.md</a>
    </div>
  </section>

  <section class="section">
    <h2 class="section-title"><span>09</span>Scope and limitations</h2>
    <div class="scope-grid">
      <div class="scope-col">
        <h4>Covered</h4>
        <ul>
          <li class="covered">Tokens and abstraction strategy</li>
          <li class="covered">Token architecture</li>
          <li class="covered">Anti-patterns in definition and use</li>
          <li class="covered">Weighted health score (3 axes)</li>
          <li class="covered">Component architecture (LOC, inline styles, God Component)</li>
        </ul>
      </div>
      <div class="scope-col">
        <h4>Not covered</h4>
        <ul>
          <li class="excluded">WCAG accessibility (separate audit)</li>
          <li class="excluded">CSS performance / bundle size</li>
          <li class="excluded">Figma ↔ code</li>
          <li class="excluded">Detailed organizational governance</li>
          <li class="excluded">Backend / infrastructure</li>
        </ul>
      </div>
    </div>
    <p class="scope-note">[[SCOPE_NOTE]]</p>
  </section>

  <section class="section">
    <h2 class="section-title"><span>10</span>Signature and methodology</h2>
    <div class="signature">
      <div class="sig-left">
        <div class="auditor-name">[[AUDITOR_NAME]]</div>
        <div class="auditor-org">[[AUDITOR_ORG]]</div>
        <div class="auditor-email">[[AUDITOR_EMAIL]]</div>
      </div>
      <div class="sig-right">
        <div class="sig-detail">Date: [[AUDIT_DATE]]</div>
        <div class="sig-detail">Methodology: Design System Auditor · 6 phases</div>
        <div class="sig-version">[[AUDIT_VERSION]]</div>
      </div>
    </div>
  </section>

</div>
<script type="text/plain" id="audit-md-source">[[AUDIT_RESULT_MD]]</script>
<script>
(function () {
  const btn = document.getElementById("download-audit-md");
  if (!btn) return;
  btn.addEventListener("click", async function () {
    let md = "";
    try {
      const res = await fetch("audit-result.md", { cache: "no-store" });
      if (res.ok) md = await res.text();
    } catch (_) {}
    if (!md) {
      const el = document.getElementById("audit-md-source");
      if (el) md = el.textContent.trim();
    }
    if (!md) {
      alert("Could not load audit-result.md. Open it from the same folder as this HTML file.");
      return;
    }
    const blob = new Blob([md], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "audit-result.md";
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  });
})();
</script>
</body>
</html>

```

### Template audit-result.md

Plan accionable (inglés por defecto en el reporte HTML). **No** incluir ROI, referencia a empresas ni contenido solo visual.

```markdown
# Design System Audit — [[CLIENT_NAME]]

**Date:** [[AUDIT_DATE]] · **Score:** [[SCORE_GLOBAL]] / 100 ([[SCORE_LABEL]])
**Phase:** [[COMPANY_PHASE]] · **Team:** [[STAT_DESIGNERS]] designer(s) · **Surfaces:** [[STAT_PLATFORMS]]

---

## Recommendation

[[MODEL_PRESCRIPTION_PLAIN]]

---

## Target model

| | Current | Target |
|---|---------|--------|
| **Overall** | [[CURRENT_MODEL]] | [[TARGET_MODEL]] |
| **Tokens** | [[TOKEN_MODEL]] | [[TARGET_TOKEN_MODEL]] |
| **Architecture** | [[ARCH_MODEL]] | [[TARGET_ARCH_MODEL]] |

---

## Priority anti-patterns

[[ANTIPATTERNS_MD]]

---

## Action plan

**[[TOTAL_PM]]** · **[[CALENDAR_DURATION]]** · [[DEDICATION]]

[[ACTION_PLAN_MD]]

---

## Do not do now

[[NOT_TOUCH_MD]]

---

## Success metrics (post-implementation)

[[METRICS_MD]]

---

*Generated by [[AUDIT_VERSION]] · Full visual report: `result-page.html`*
```
