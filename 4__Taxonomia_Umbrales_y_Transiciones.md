# 4. Taxonomía, Umbrales y Transiciones

> Lo que falta para que la calculadora no tenga que "pensar" — solo ejecutar.

---

## 4.1. Taxonomía de nombres de tokens

> Cómo distinguir el nivel de un token **solo por su nombre**.

### Reglas de clasificación por patrón

| Nivel | Patrón de nombre | Ejemplos | Regex sugerido |
|---|---|---|---|
| **Primitive** | `<tipo>-<valor>` donde valor es escala numérica, nombre de color base, o tamaño abstracto | `blue-500`, `gray-100`, `space-4`, `radius-md`, `font-sm` | `^(color-)?(blue\|red\|green\|gray\|neutral\|slate\|zinc\|stone\|orange\|amber\|yellow\|lime\|emerald\|teal\|cyan\|sky\|indigo\|violet\|purple\|fuchsia\|pink\|rose)-\d+$` o `^space-\d+$` o `^(radius\|font\|shadow)-(xs\|sm\|md\|lg\|xl\|2xl\|3xl\|\d+)$` |
| **Semantic** | `<tipo>-<contexto>-<variante>` donde contexto indica intención de uso | `color-text-primary`, `color-bg-surface`, `color-border-subtle`, `spacing-content`, `radius-interactive` | `^color-(text\|bg\|background\|border\|surface\|overlay\|icon\|link\|action\|status\|feedback)-` o `^(spacing\|radius\|shadow)-(content\|container\|interactive\|input\|card\|modal\|page)` |
| **Component** | `<componente>-<propiedad>` o `<componente>-<estado>-<propiedad>` | `button-bg`, `button-hover-bg`, `card-radius`, `input-border`, `modal-overlay` | `^(button\|card\|input\|modal\|dropdown\|tooltip\|badge\|alert\|avatar\|checkbox\|radio\|switch\|tab\|tag\|chip\|dialog\|drawer\|popover\|menu\|nav\|header\|footer\|sidebar\|table\|list)-` |

---

### Árbol de decisión para clasificar un token

```
¿El nombre contiene un nombre de componente conocido al inicio?
    ├─ SÍ → COMPONENT TOKEN
    └─ NO → ¿Contiene sufijo numérico o escala de tamaño (xs/sm/md/lg/xl)?
                ├─ SÍ → ¿El prefijo es un color base (blue, red, gray...)?
                │         ├─ SÍ → PRIMITIVE
                │         └─ NO → ¿El prefijo indica contexto de uso (text, bg, border)?
                │                   ├─ SÍ → SEMANTIC (con escala)
                │                   └─ NO → PRIMITIVE
                └─ NO → ¿Contiene palabras de intención (primary, secondary, surface, subtle, muted)?
                          ├─ SÍ → SEMANTIC
                          └─ NO → ¿Contiene contexto de uso (text, bg, border, overlay)?
                                    ├─ SÍ → SEMANTIC
                                    └─ NO → INDETERMINADO (revisar manualmente)
```

---

### Diccionario de prefijos y sufijos

**Prefijos que indican PRIMITIVE:**
- Colores base: `blue`, `red`, `green`, `gray`, `neutral`, `slate`, `zinc`, `stone`, `orange`, `amber`, `yellow`, `lime`, `emerald`, `teal`, `cyan`, `sky`, `indigo`, `violet`, `purple`, `fuchsia`, `pink`, `rose`, `black`, `white`
- Espaciado numérico: `space`, `spacing`, `gap`, `margin`, `padding` + número
- Tipografía escalada: `font`, `text` + escala

**Prefijos que indican SEMANTIC:**
- Contexto visual: `text`, `bg`, `background`, `border`, `surface`, `overlay`, `icon`, `link`
- Contexto funcional: `action`, `status`, `feedback`, `interactive`, `disabled`, `focus`, `error`, `success`, `warning`, `info`

**Prefijos que indican COMPONENT:**
- Nombres de componentes UI: `button`, `card`, `input`, `modal`, `dropdown`, `tooltip`, `badge`, `alert`, `avatar`, `checkbox`, `radio`, `switch`, `tab`, `tag`, `chip`, `dialog`, `drawer`, `popover`, `menu`, `nav`, `header`, `footer`, `sidebar`, `table`, `list`, `form`, `field`

**Sufijos que indican PRIMITIVE:**
- Escalas numéricas: `50`, `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`, `950`
- Escalas de tamaño: `xs`, `sm`, `md`, `lg`, `xl`, `2xl`, `3xl`, `4xl`
- Números directos: `0`, `1`, `2`, `4`, `8`, `12`, `16`, `24`, `32`, `48`, `64`

**Sufijos que indican SEMANTIC:**
- Jerarquía: `primary`, `secondary`, `tertiary`, `quaternary`
- Intensidad: `subtle`, `muted`, `strong`, `bold`, `light`, `dark`
- Contexto: `surface`, `canvas`, `backdrop`, `elevated`, `sunken`

---

### Casos ambiguos y cómo resolverlos

| Token | ¿Ambiguo? | Resolución |
|---|---|---|
| `color-primary` | Sí | Sin contexto de uso → tratar como **primitive con alias**. Señalar como posible deuda semántica. |
| `primary-color` | Sí | Mismo caso. Orden invertido no cambia la clasificación. |
| `text-sm` | Sí | Si se usa para tamaño de fuente → **primitive**. Si se usa como token de texto → revisar contexto. |
| `button-primary` | Sí | ¿Es el color primario del botón o el estilo "primary" del botón? Clasificar como **component** y documentar. |
| `spacing-lg` | No | **Primitive** — escala de tamaño sin contexto de uso. |
| `spacing-content` | No | **Semantic** — contexto de uso explícito. |

---

## 4.2. Umbrales de decisión

> Números concretos para que la calculadora clasifique sin ambigüedad.

### Umbrales para clasificación del modelo de tokens

| Métrica | Umbral | Clasificación resultante |
|---|---|---|
| % de valores literales en componentes | ≥60% | **Sin tokens** |
| % de valores literales en componentes | 30–59% | **Tokens inmaduros** |
| % de valores literales en componentes | <30% | Sistema con tokens |
| % de primitives sobre total de tokens usados | ≥70% | **Token-first primitivo** |
| % de semantic tokens sobre total | ≥60% | **Semantic-first** |
| Existen ≥3 niveles de tokens Y ninguno domina (>60%) | — | **Hybrid** |
| Existen tokens de componente Y se usan en ≥40% de componentes | — | **Hybrid con component layer** |

---

### Umbrales para clasificación de arquitectura

| Señal | Umbral | Clasificación |
|---|---|---|
| Tokens definidos en 1 ubicación central | 100% de definiciones en `tokens/` o `design-system/tokens/` | **Centralized** |
| Tokens definidos junto a componentes | ≥70% de componentes tienen `*.tokens.*` colocado | **Component co-located** |
| Existe `platform/` con ≥2 subdirectorios | — | **Multiplatform infra** |
| Mezcla de tokens centrales y locales | 30–70% en cada uno | **Híbrido inestable** (señalar como problema) |

---

### Umbrales para detección de problemas

| Problema | Umbral de detección |
|---|---|
| **Mezcla de niveles en un componente** | ≥2 niveles distintos de tokens para el mismo tipo de propiedad (ej: color) |
| **Primitives en componentes de alto nivel** | Componente usa ≥3 primitives directamente sin pasar por semantic/component |
| **Valores mágicos excesivos** | Componente tiene ≥4 valores literales (hex, px, rem) |
| **Token huérfano** | Token definido pero usado en 0 componentes |
| **Token sobreusado fuera de contexto** | Token de componente usado en ≥3 componentes distintos |
| **Duplicación de definición** | Mismo nombre de token definido en ≥2 archivos con valores distintos |
| **Fuentes de tokens fragmentadas** | ≥3 ubicaciones distintas definiendo tokens del mismo tipo |

---

### Tabla de puntajes para salud del sistema

| Métrica | Peso | Cálculo |
|---|---|---|
| Consistencia de nivel de tokens | 30% | `100 - (% componentes con mezcla de niveles)` |
| Cobertura de tokens | 25% | `100 - (% valores literales en componentes)` |
| Centralización de definiciones | 20% | `100 - (penalización por fuentes fragmentadas)` |
| Ausencia de tokens huérfanos | 15% | `100 - (% tokens sin uso)` |
| Ausencia de duplicaciones | 10% | `100 - (% tokens con definición duplicada)` |

**Escala de salud:**
- 90–100: Excelente
- 75–89: Bueno
- 60–74: Aceptable con áreas de mejora
- 40–59: Problemas significativos
- <40: Sistema de tokens disfuncional

---

## 4.3. Mapa modelo → reglas válidas

> Para cada modelo, qué está permitido, qué es smell, y cómo luce un componente ideal.

### A. Sin tokens

| Aspecto | Regla |
|---|---|
| **Permitido** | Valores literales en todas partes. |
| **Smell** | N/A — el modelo no tiene expectativas de tokens. |
| **Componente ideal** | No aplica. |
| **Transición recomendada** | Extraer valores repetidos a primitives. |

---

### B. Token-first primitivo

| Aspecto | Regla |
|---|---|
| **Permitido** | Primitives en componentes. Valores literales solo para casos excepcionales (≤2 por componente). |
| **Smell** | Tokens semánticos definidos pero no usados. Más de 3 valores literales en un componente. |
| **Componente ideal** | |

```css
.button {
  background: var(--color-blue-500);
  color: var(--color-white);
  padding: var(--space-2) var(--space-4);
  border-radius: var(--radius-md);
}
```

| **Transición natural** | Agrupar primitives en semantic tokens cuando aparecen patrones de uso. |

---

### C. Semantic-first

| Aspecto | Regla |
|---|---|
| **Permitido** | Semantic tokens en componentes. Primitives solo en definiciones de semantic tokens. |
| **Smell** | Primitives usados directamente en componentes (bypass del sistema). Valores literales en componentes. |
| **Componente ideal** | |

```css
.button {
  background: var(--color-action-primary);
  color: var(--color-text-on-action);
  padding: var(--spacing-interactive-y) var(--spacing-interactive-x);
  border-radius: var(--radius-interactive);
}
```

| **Transición natural** | Añadir component tokens para variantes complejas cuando un componente tiene ≥5 tokens semánticos. |

---

### D. Hybrid (primitives + semantic + component)

| Aspecto | Regla |
|---|---|
| **Permitido** | Component tokens como primera opción. Semantic tokens como fallback. Primitives solo en definiciones. |
| **Smell** | Mezcla de niveles en el mismo componente para la misma propiedad. Primitives usados directamente en componentes (excepto en definiciones de tokens). |
| **Componente ideal** | |

```css
/* tokens/components/button.css */
:root {
  --button-bg: var(--color-action-primary);
  --button-text: var(--color-text-on-action);
  --button-padding-y: var(--spacing-interactive-y);
  --button-padding-x: var(--spacing-interactive-x);
  --button-radius: var(--radius-interactive);
}

/* components/button.css */
.button {
  background: var(--button-bg);
  color: var(--button-text);
  padding: var(--button-padding-y) var(--button-padding-x);
  border-radius: var(--button-radius);
}
```

| **Principio clave** | Cada nivel solo referencia al nivel inmediatamente inferior: component → semantic → primitive. |

---

### E. Arquitectura Centralized

| Aspecto | Regla |
|---|---|
| **Permitido** | Todos los tokens en `tokens/` o `design-system/tokens/`. Componentes solo consumen, nunca definen. |
| **Smell** | Tokens definidos en carpetas de componentes. Múltiples archivos `variables.css` en distintas ubicaciones. |
| **Estructura ideal** | |

```
design-system/
  tokens/
    primitives/
      colors.css
      spacing.css
      typography.css
    semantic/
      colors.css
      spacing.css
    components/
      button.css
      card.css
  components/
    button/
      button.tsx
      button.css      ← solo consume tokens
```

---

### F. Arquitectura Component co-located

| Aspecto | Regla |
|---|---|
| **Permitido** | Cada componente define sus propios tokens. Puede existir un core mínimo compartido. |
| **Smell** | Tokens de un componente usados en otro. Definiciones duplicadas entre componentes. |
| **Estructura ideal** | |

```
components/
  button/
    button.tsx
    button.css
    button.tokens.ts  ← define --button-*
  card/
    card.tsx
    card.css
    card.tokens.ts    ← define --card-*
shared/
  primitives.css      ← solo colores base y escalas
```

---

### G. Arquitectura Multiplatform infra

| Aspecto | Regla |
|---|---|
| **Permitido** | Un core de tokens compartido. Cada plataforma puede extender pero no redefinir core. |
| **Smell** | Plataformas redefiniendo tokens core con valores distintos. Ausencia de core común. |
| **Estructura ideal** | |

```
tokens/
  core/
    primitives.json
    semantic.json
  platform/
    web/
      overrides.css
    ios/
      overrides.swift
    android/
      overrides.xml

platform/
  web/
    components/
  ios/
    components/
  android/
    components/
```

---

## 4.4. Mapa de transiciones entre modelos

> Cómo pasar de un modelo a otro sin romper todo.

### Transición: Sin tokens → Token-first primitivo

**Contexto:** El sistema tiene valores literales por todas partes.

**Pasos:**

1. **Inventariar valores únicos**
   - Extraer todos los colores hex usados → crear escala de colores (`blue-100` a `blue-900`)
   - Extraer todos los valores de spacing → crear escala (`space-1` a `space-16`)
   - Extraer todos los radios → crear escala (`radius-sm`, `radius-md`, `radius-lg`)

2. **Crear archivo de primitives**
   ```css
   :root {
     --color-blue-500: #3B82F6;
     --space-4: 1rem;
     --radius-md: 0.5rem;
   }
   ```

3. **Reemplazar valores literales progresivamente**
   - Empezar por componentes más usados
   - Un tipo de propiedad a la vez (primero colores, luego spacing, luego radios)

4. **Validar:** ≤30% de valores literales restantes

**Riesgos:**
- Crear demasiados primitives (más de 100 es señal de sobre-ingeniería)
- No establecer convención de nombres desde el inicio

---

### Transición: Token-first primitivo → Semantic-first

**Contexto:** El sistema tiene primitives pero los componentes los usan directamente.

**Pasos:**

1. **Identificar patrones de uso**
   - ¿Qué primitive se usa para texto principal? → `color-text-primary`
   - ¿Qué primitive se usa para fondos? → `color-bg-surface`
   - Documentar cada mapping

2. **Crear capa semántica**
   ```css
   :root {
     --color-text-primary: var(--color-gray-900);
     --color-bg-surface: var(--color-white);
     --color-action-primary: var(--color-blue-500);
   }
   ```

3. **Migrar componentes**
   - Reemplazar `var(--color-blue-500)` por `var(--color-action-primary)` donde aplique
   - Mantener primitives accesibles para casos excepcionales

4. **Validar:** ≥60% de usos son semantic tokens

**Riesgos:**
- Crear semantic tokens que son 1:1 con primitives (no aportan abstracción)
- No definir reglas claras de cuándo usar semantic vs primitive

---

### Transición: Semantic-first → Hybrid

**Contexto:** El sistema tiene semantic tokens pero los componentes complejos necesitan más granularidad.

**Pasos:**

1. **Identificar componentes candidatos**
   - Componentes con ≥5 semantic tokens
   - Componentes con múltiples variantes (primary, secondary, destructive)
   - Componentes con estados complejos (hover, focus, disabled)

2. **Crear component tokens**
   ```css
   :root {
     /* Component tokens referencian semantic */
     --button-bg: var(--color-action-primary);
     --button-bg-hover: var(--color-action-primary-hover);
     --button-text: var(--color-text-on-action);
   }
   ```

3. **Establecer regla de cascada**
   ```
   Component tokens → Semantic tokens → Primitives
   (nunca saltar niveles)
   ```

4. **Migrar componentes priorizados**
   - Solo componentes que se benefician de la abstracción adicional
   - No crear component tokens para componentes simples

5. **Validar:** Cada nivel solo referencia al inferior

**Riesgos:**
- Crear component tokens para todo (sobre-abstracción)
- Componentes que mezclan niveles sin criterio

---

### Transición: Centralized → Component co-located (sin perder gobernanza)

**Contexto:** El sistema tiene tokens centralizados pero los equipos necesitan más autonomía.

**Pasos:**

1. **Separar tokens en dos capas**
   - **Core tokens (centralizados):** Primitives y semantic tokens que definen la marca
   - **Component tokens (colocados):** Específicos de cada componente

2. **Mover component tokens a carpetas de componentes**
   ```
   ANTES:
   tokens/
     components/
       button.css
   components/
     button/
       button.tsx

   DESPUÉS:
   tokens/
     core/           ← primitives + semantic
   components/
     button/
       button.tsx
       button.tokens.css  ← solo --button-*
   ```

3. **Establecer contrato de importación**
   ```css
   /* button.tokens.css */
   @import '../../tokens/core/semantic.css';
   
   :root {
     --button-bg: var(--color-action-primary);
   }
   ```

4. **Definir ownership**
   - Core tokens: Design System team
   - Component tokens: Equipo del componente (con review)

5. **Validar:** 
   - Core tokens no duplicados en componentes
   - Component tokens no usados fuera de su componente

**Riesgos:**
- Equipos redefiniendo core tokens localmente
- Pérdida de consistencia visual entre componentes

---

### Transición: Single platform → Multiplatform infra

**Contexto:** El sistema funciona para web y necesita escalar a mobile/otras plataformas.

**Pasos:**

1. **Extraer tokens a formato agnóstico**
   - Convertir CSS variables a JSON o YAML
   - Usar herramienta como Style Dictionary

   ```json
   {
     "color": {
       "text": {
         "primary": { "value": "{color.gray.900}" }
       }
     }
   }
   ```

2. **Crear estructura de plataformas**
   ```
   tokens/
     core/
       primitives.json
       semantic.json
     platform/
       web/
         transform.js
       ios/
         transform.swift
       android/
         transform.kt
   ```

3. **Implementar transformaciones por plataforma**
   - Web: CSS custom properties
   - iOS: Swift constants o Asset Catalog
   - Android: XML resources o Compose tokens

4. **Establecer proceso de sincronización**
   - Cambio en core → rebuild de todas las plataformas
   - Override de plataforma → solo esa plataforma

5. **Validar:**
   - Mismo token, mismo valor semántico en todas las plataformas
   - Overrides documentados y justificados

**Riesgos:**
- Plataformas divergiendo sin control
- Complejidad de build que nadie entiende

---

### Matriz de compatibilidad de transiciones

| Desde / Hacia | Sin tokens | Primitive | Semantic | Hybrid | Centralized | Co-located | Multiplatform |
|---|---|---|---|---|---|---|---|
| **Sin tokens** | — | ✅ Directo | ⚠️ Saltar paso | ⚠️ Saltar pasos | N/A | N/A | N/A |
| **Primitive** | ❌ Regresión | — | ✅ Directo | ✅ Directo | N/A | N/A | N/A |
| **Semantic** | ❌ Regresión | ⚠️ Simplificar | — | ✅ Directo | N/A | N/A | N/A |
| **Hybrid** | ❌ Regresión | ⚠️ Simplificar | ⚠️ Simplificar | — | N/A | N/A | N/A |
| **Centralized** | N/A | N/A | N/A | N/A | — | ✅ Con reglas | ✅ Directo |
| **Co-located** | N/A | N/A | N/A | N/A | ⚠️ Consolidar | — | ⚠️ Extraer core |
| **Multiplatform** | N/A | N/A | N/A | N/A | ⚠️ Colapsar | ⚠️ Fragmentar | — |

**Leyenda:**
- ✅ Transición recomendada y bien definida
- ⚠️ Posible pero con riesgos o pasos adicionales
- ❌ Regresión — evitar salvo razones muy específicas
- N/A — Ejes distintos, no aplica comparación directa

---

## Apéndice: Checklist de transición

Antes de iniciar cualquier transición:

- [ ] Inventario completo de tokens actuales (nombres, valores, ubicaciones)
- [ ] Mapa de uso: qué componentes usan qué tokens
- [ ] Identificación de deuda actual (duplicados, huérfanos, mezclas)
- [ ] Definición de estado objetivo (qué modelo, qué umbrales)
- [ ] Plan de migración incremental (no big bang)
- [ ] Métricas de éxito (umbrales de la sección 4.2)
- [ ] Ownership definido (quién aprueba cambios en cada capa)
