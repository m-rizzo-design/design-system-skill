# 7. Arquitectura de Componentes

> Framework de análisis de estructura de componentes — el segundo eje de auditoría además de tokens. Define anti-patrones detectables, métricas de salud y patrones de referencia modernos.

---

## 7.1. Métricas accionables

Estas métricas pueden medirse directamente del código mediante análisis estático. Cada una tiene un umbral específico que señala deterioro.

| Métrica | Healthy | Warning | Crítico | Herramienta |
|---------|---------|---------|---------|------------|
| LOC por componente | < 200–300 | 300–500 | > 500 | ESLint `max-lines`, SonarQube |
| Complejidad ciclomática | < 10 por función | 10–20 | > 20 | ESLint `complexity` rule |
| Complejidad cognitiva | < 15 | 15–25 | > 25 | SonarQube |
| Props por componente | < 7–10 | 10–15 | > 15 | Custom ESLint rules |
| `useState` por componente | < 3 | 3–5 | > 5 | Manual review o AST |
| Reuse rate (cobertura UI) | > 80% | 50–80% | < 50% | Omlet.dev, Figma Analytics |
| Code duplication | < 2% | 2–4% | > 4% | jscpd, SonarQube CPD |
| Dependencies (fan-out) | Moderado | Alto | Circular | dependency-cruiser |
| Test coverage DS | > 80% | 60–80% | < 60% | Jest, Istanbul |

**Interpretación:** un componente con 600+ LOC, 5+ `useState` y complejidad > 20 es un God Component. Una reuse rate < 50% indica duplicación o adopción pobre. Duplication > 4% sugiere equipos independientes resolviendo problemas idénticos.

---

## 7.2. Los 5 anti-patrones detectables

### AP-6: God Component

**Qué es:** Un componente que concentra lógica de validación, fetching, state management, error handling y rendering en un único archivo.

**Síntomas:**
- Archivo > 500 LOC
- Más de 3–4 `useState` desconectados
- Métodos internos `renderThing()`, `handleThing()`, `validateThing()`
- Props complejos (objects anidados, callbacks múltiples)
- Imposible de testear en aislamiento

**Impacto:** Bottleneck de desarrollo. Bug fix en validación requiere entender todo el componente. Re-renders innecesarios. Imposible reutilizar lógica independientemente.

**Solución:**
- Extraer lógica en custom hooks (uno por responsabilidad: `useValidation`, `useFetch`, etc.)
- Dividir en componentes más pequeños con responsabilidades claras
- Usar compound component pattern si la UI tiene estructura compleja
- Considerar `useReducer` para múltiples estados relacionados

**Detección:** ESLint `max-lines` (umbral 300), SonarQube, conteo de `useState`.

---

### AP-7: Prop Drilling

**Qué es:** Pasar datos (props) a través de múltiples componentes intermediarios que no los consumen.

**Síntomas:**
- Props viajan > 3 capas sin ser usados en intermedios
- Cambios a una prop ripple a través de muchos componentes
- Intermediarios solo hacen `<Child {...props} />`
- Feedback: "tengo que editar 5 componentes para agregar una propiedad"

**Impacto:** Fragilidad. Cualquier cambio de tipo propaga a toda la cadena. Imposible refactorizar un componente sin revisar todas sus instancias. Reduces reutilización.

**Solución:**
- Context API para datos que cruzan muchas capas (themes, auth, localization, UI state)
- Compound components con estado compartido vía context interno
- Composition: pasar componentes como children en lugar de props
- Hooks: extraer data en un hook, inyectarla en componentes finales

**Detección:** Manual o con herramientas de static analysis que rastreen prop usage. dependency-cruiser puede visualizar cadenas profundas.

---

### AP-8: Component Duplication

**Qué es:** Múltiples equipos crean versiones independientes del mismo componente.

**Síntomas:**
- jscpd reporta 4%+ code duplication
- Búsqueda de "tag", "badge", "button" find 6+ variantes similares
- Componentes esparcidos en diferentes repos/carpetas sin cross-repo awareness
- Mismo comportamiento implementado diferente (accessibility, keyboard handling)

**Impacto:** Mantenimiento fragmentado. Bug en un lugar no se propaga a otros. Mejoras de UX solo llegan a algunas versiones. Inconsistencia perceptual y conductual.

**Caso real:** Shopify's Deliver team encontró **6 componentes de "tag" independientes** que consolidaron en Polaris.

**Solución:**
- Scan cross-repo con jscpd (`--min-tokens 50`)
- Centralizar en single source of truth (npm package, monorepo)
- Si es multi-equipo: shared library con governance clara
- CI/CD check que bloquea componentes nuevos demasiado similares a existentes

**Detección:** jscpd, Omlet.dev (adoption tracking), búsquedas manuales en codebase.

---

### AP-9: Over-Abstraction

**Qué es:** Componentes tan genéricos que son más difíciles de usar que escribir HTML/CSS directo.

**Síntomas:**
- Componente toma > 15 props con 10+ booleans/flags
- Documentación requerida es más larga que el código del usuario
- "Es más fácil hacer `<div>` que aprender este componente"
- Casos especiales requieren props esotéricas

**Impacto:** Bajo adoption. Equipos bypasean el componente y escriben lo suyo. Inversión sin retorno.

**Principio:** Dan Abramov: "Duplication is far cheaper than the wrong abstraction." Mejor duplicar un little-used case que crear abstracción prematura.

**Solución:**
- Diseñar para el 80% de casos, no el 100%
- Separar en múltiples componentes simples (composition) en lugar de un mega-componente configurable
- Proveer slots/children para casos edge
- Usar compound pattern: `<Dialog><Dialog.Header><Dialog.Content /></Dialog>`

**Detección:** Métricas de props, prueba de uso (¿qué porcentaje de props usa cada instancia?), feedback de usuarios.

---

### AP-10: Tight Coupling

**Qué es:** Cambios en un componente requieren cambios en muchos otros; dependencias circulares; imposible testear en aislamiento.

**Síntomas:**
- Dependencias circulares (A importa B, B importa A)
- Componente expone detalles de implementación en su API
- Cambios a un componente fuerzan cambios en 5+ lugares
- Componentes asumen estructura interna de otros

**Variante:** Leaky Abstractions — API del componente espeja DOM API o expone detalles internos.

**Impacto:** Refactoring paralizante. Cada cambio trae riesgo de cascade de bugs. Imposible evolucionar el componente sin breaking changes.

**Solución:**
- Componentes independientes, sin asumir estructura interna de otros
- Dependency inversion: pasar comportamiento como props/context, no asumir implementación
- Testing en aislamiento con mocks
- API clara y estable (cambios son breaking, versionar)
- dependency-cruiser para detectar high fan-out y ciclos

**Detección:** dependency-cruiser, análisis manual de imports, test con mocks.

---

## 7.3. Patrones modernos de referencia

### Atomic Design (Brad Frost, 2013)

**Estructura:** Atoms → Molecules → Organisms → Templates → Pages

**Cuándo funciona:** Proyectos con mucho UI y bajo business logic. UI-centric design.

**Qué es en 2025:** Las categorías de química son menos importantes que el principio subyacente: **composición jerárquica**. El model actual incluye **tokens como capa subatómica** (Frost no la contemplaba).

**Implementación sana:**
- Naming: semantic/purposeful, no literal chemistry (ej: `Card`, `TextField`, no `Atom1`, `Molecule3`)
- Atoms: componentes sin dependencias, altamente reutilizables
- Molecules: componen atoms, resuelven un problema específico
- Organisms: componen molecules, representan secciones de page
- Cada nivel respeta single responsibility

**Riesgo:** Rigidez. Algunos equipos fuerzan todo en categorías Atomic, criando discusiones esteriles sobre qué va donde.

---

### Compound Components

**Qué es:** Parent component maneja state/behavior, children consumen state vía context.

**Patrón:**
```jsx
<Modal>
  <Modal.Trigger>Open</Modal.Trigger>
  <Modal.Content>
    <Modal.Header>Title</Modal.Header>
    <Modal.Body>Content</Modal.Body>
    <Modal.Footer>
      <Modal.Close>Cancel</Modal.Close>
    </Modal.Footer>
  </Modal.Content>
</Modal>
```

**Ventajas:**
- API intuitiva (espeja patterns HTML nativos: `<select>/<option>`)
- Consumer controla layout y estructura
- State centralizado, no prop drilling
- Cada child es simple y testeable

**Dónde brilla:** Modals, dropdowns, tabs, disclosure patterns. Donde hay comportamiento acoplado pero layout variable.

**Trade-off:** No apto para componentes triviales (Button simple). Cuando layout order debe ser estricto, usar slot patterns en lugar.

**Ecosistema:** Radix UI, Headless UI, Chakra UI, MUI todos usan esto extensamente.

---

### Headless Components

**Qué es:** Componentes que proveen lógica, state management, keyboard navigation y accessibility **sin prescribir UI**. El consumer estila.

**Capas (modelo Adobe React Spectrum):**
1. **Behavior/Logic** (React Aria hooks) — keyboard, a11y, state machine
2. **State management** (React Stately) — shared state coordination
3. **Themed UI** (React Spectrum) — estilos específicos de marca

**Ventaja crucial:** Logic y UI están desacoplados. Puedes cambiar estilos sin afectar accessibility.

**Referentes:**
- **Radix UI** (32 componentes WAI-ARIA, built on state machines)
- **React Aria** (Adobe, hooks-based behavior layer)
- **Headless UI** (equipo Tailwind, minimal)
- **Ark UI** (45+ componentes, multi-framework: React/Solid/Vue/Svelte)
- **shadcn/ui** (copy-paste Radix + Tailwind, demostró que outcompete npm libraries)

**Impacto 2024–2026:** Ha catalizado migración de MUI, Chakra y otros a arquitectura headless. Incluso Material Design evoluciona hacia opciones headless.

**ROI:** Gloat migró de Material UI a Headless UI; refactoring complejo que habría tomado **meses** se completó en **horas**.

---

## 7.4. Herramientas de detección automática

### jscpd — Copy/paste detection

**Uso:**
```bash
jscpd --min-tokens 50 --languages javascript ./src
```

**Qué detecta:** Bloques de código duplicados. La métrica es tokens (palabras), no caracteres.

**Umbrales recomendados:**
- `--min-tokens 50` para scan inicial (detecta duplicación real)
- 2% warning, 4% block en CI/CD

**Output:** Archivo por archivo, agrupados por duplicación%. Identifica qué líneas están duplicadas.

**Falsos positivos:** Similar structure pero semántica diferente (ej: dos loops independientes). Revisar antes de accionar.

---

### dependency-cruiser — Dependency graphs y enforcement

**Uso:**
```bash
depcruise --output-type text src/
```

**Qué detecta:**
- Dependencias circulares
- Fan-out (cuántos componentes dependen de uno)
- Violaciones de arquitectura (ej: atoms no deben importar organisms)
- Capas prohibidas

**Configuración:** `.dependency-cruiser.js` define reglas de arquitectura.

**Output:** Visualización de grafo (DOT, SVG). Útil para entender coupling.

---

### Omlet.dev — Design system adoption tracking

**Qué es:** SaaS que rastrea qué componentes de DS se usan en dónde, en qué versión, adoption rate.

**Métricas:**
- Component adoption % (target: 80%+)
- Figma detachment rate (high = componentes demasiado rígidos)
- Version distribution (qué % está en latest)

**ROI:** Cuando descubres que 60% de codebase ignora el DS, tienes dato concreto para argumentar inversión en "mejorar DSX".

---

### react-component-analyzer — React-specific metrics

**Qué hace:** Analiza componentes React y calcula:
- Cohesión (¿qué tan relacionadas están las responsibility?)
- Acoplamiento (cuántas dependencias externas)
- Prop drilling (qué tan profundo)
- Health score 0–100%

**Output:** JSON con componentes rankeados por health. Ideal para CI/CD.

---

### SonarQube — Comprehensive code quality

**Qué detecta:**
- Complejidad ciclomática y cognitiva
- Code duplication (pero con false positives en React — excluir component dirs)
- Security hotspots
- Test coverage

**Cuidado:** SonarQube's duplication detector es aggressive en React (strips strings), creando 70–80% false positives. Usar jscpd primero, SonarQube para profundidad.

---

## 7.5. Umbrales de detección por métrica

**Regla de oro:** Umbrales absolutos son menos útiles que tendencias. Un componente con 350 LOC en aislamiento es probably fine; si hay 10 así y crecen 50 LOC/trimestre, es signal de degradation.

### Por métrica:

**LOC por componente:**
- < 200: excelente
- 200–300: bueno, límite pragmático
- 300–500: warning, revisar complejidad
- > 500: crítico, god component probable

**Complejidad ciclomática:**
- < 10: sano
- 10–20: revisar, considerar refactor
- > 20: crítico, muy difícil de testear

**Reuse rate:**
- > 80%: excelente, DS adoption real
- 50–80%: oportunidad, hay duplicación
- < 50%: crítico, equipos bypassing el DS

**Code duplication:**
- < 2%: sano
- 2–4%: warning, scan con jscpd
- > 4%: crítico, múltiples quasi-duplicates

**Test coverage:**
- > 80%: sano para DS components
- 60–80%: warning
- < 60%: crítico, regressions probable

---

## 7.6. Protocolo de análisis de componentes

**Fase 1: Scan estático**
1. Ejecutar jscpd con `--min-tokens 50`, reportar % duplication
2. Ejecutar ESLint con reglas de complejidad, máx LOC, props
3. Ejecutar dependency-cruiser, buscar ciclos y high fan-out
4. Compilar lista de componentes con métricas fuera de threshold

**Fase 2: Clasificación**
- God Components (LOC > 500 O (useState > 4 AND complexity > 15))
- Prop Drilling (trace imports > 3 profundidad sin uso)
- Duplicates (jscpd > 70% similarity en múltiples files)
- Over-Abstraction (props > 15 OR boolean flags > 10)
- Tight Coupling (circular deps OR high fan-out)

**Fase 3: Patrón moderno**
- ¿Usan Atomic Design, Compound Components, Headless patterns?
- ¿Qué patrones están ausentes? (ej: todo es monolítico, sin composition)

**Fase 4: Recomendaciones** (ver Doc 7 en impacto a SKILL.md)
