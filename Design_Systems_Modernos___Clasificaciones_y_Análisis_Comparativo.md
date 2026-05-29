# Design Systems Modernos — Clasificaciones y Análisis Comparativo

> Donde el diseño sistemático se vuelve más interesante.

---

## Introducción: Dos ejes que suelen confundirse

Cuando se habla de Design Systems modernos, se mezclan frecuentemente dos clasificaciones distintas:

1. **Cómo se definen los estilos** (tokens vs semántico vs híbrido)
2. **Cómo se organiza el código del sistema** (tokens separados vs componentes autocontenidos)

Son dos ejes distintos. A continuación se ordenan por separado.

---

## 1. Modelos de definición de estilos (Design Token Strategy)

### 1️⃣ Token-first systems

El sistema se basa en design tokens como fuente de verdad. Los componentes consumen tokens, no estilos directos.

Ejemplo de tokens:

```
--color-primary
--spacing-sm
--radius-md
--font-body
```

Arquitectura típica:

```
tokens/
  colors/
  spacing/
  typography/
  radius/

components/
  button/
  card/
  modal/
```

Ejemplo CSS:

```css
.button {
  background: var(--color-primary);
  padding: var(--spacing-sm);
  border-radius: var(--radius-md);
}
```

**Empresas que usan este enfoque:**

| Empresa | Sistema |
|---|---|
| Shopify | Polaris |
| IBM | Carbon |
| Salesforce | Lightning |
| Adobe | Spectrum |

**Ventajas:** escalable · multiplataforma · fácil theming · fácil dark mode
**Desventaja:** más complejidad inicial

---

### 2️⃣ Semantic systems

Los tokens no representan propiedades, sino **intención**.

```
color-text-primary
color-text-secondary
color-background-surface
color-border-subtle
```

No se habla de `blue-500` o `gray-100`. La arquitectura sigue tres niveles:

```
Primitive tokens
      ↓
Semantic tokens
      ↓
Components
```

Ejemplo concreto:

```
blue-500
   ↓
color-text-primary
   ↓
Button
```

**Empresas que usan mucho esto:**

| Empresa | Comentario |
|---|---|
| Apple | Human Interface Guidelines |
| Spotify | Encore |
| Atlassian | Atlassian Design System |

**Ventajas:** UI más consistente · desacopla diseño de colores reales · permite cambiar branding fácilmente

---

### 3️⃣ Hybrid systems (el estándar moderno)

Hoy casi todas las empresas grandes usan 3 niveles:

```
Primitive tokens  →  blue-500 / gray-200 / space-4
Semantic tokens   →  color-text-primary / color-bg-surface
Component tokens  →  button-bg / button-padding / card-radius
```

**Empresas que usan este modelo:**

| Empresa | Sistema |
|---|---|
| Shopify | Polaris |
| Vercel | Geist |
| Microsoft | Fluent |
| GitHub | Primer |

> Este modelo es el **dominante en 2025–2026**.

---

## 2. Modelos de arquitectura del Design System (Code Structure)

### 1️⃣ Centralized token architecture (clásica)

```
design-system/
  tokens/
    colors.css
    spacing.css
    typography.css

  components/
    button/
    card/
    modal/
```

Los componentes leen tokens globales:

```css
.button {
  color: var(--color-text-primary);
}
```

Usado en: Polaris · Carbon · Spectrum

---

### 2️⃣ Component-co-located architecture

Nueva tendencia. Cada componente tiene todo dentro:

```
button/
  button.tsx
  button.css
  button.tokens.ts
  button.test.ts
```

Muy usado con React · Next · Tailwind · TypeScript.

**Empresas cercanas a este modelo:**

| Empresa | Comentario |
|---|---|
| Vercel | Geist UI |
| Notion | UI modular |
| Linear | Estructura similar |

**Ventajas:** alta mantenibilidad · fácil versionado · componente portable
**Desventaja:** tokens menos centralizados

---

## 3. Las 4 arquitecturas modernas en empresas

| Arquitectura | Ejemplo |
|---|---|
| Token-first | Shopify |
| Semantic system | Apple |
| Hybrid token system | Microsoft |
| Component co-located | Vercel / Notion |

---

## 4. Cómo lo están haciendo las empresas más avanzadas hoy

Arquitectura dominante:

```
design-system/

  tokens/
    primitives/
    semantic/
    themes/

  components/
    button/
      button.tsx
      button.css
    card/
    modal/
```

Pipeline completo:

```
Figma
   ↓
Design Tokens
   ↓
CSS variables
   ↓
Components
```

---

## 5. La tendencia fuerte 2024–2026

**1️⃣ Tokens como API del diseño** — el design system expone tokens, no CSS.

**2️⃣ Component driven development** — los componentes son la unidad principal.

**3️⃣ Figma → tokens → code pipeline** — usando herramientas como Style Dictionary y Tokens Studio.

---

## 6. Tabla Comparativa — Empresas Multiplataforma

> Donde el diseño sistemático se vuelve más interesante: cuando el mismo sistema tiene que funcionar en web, mobile, TV, y hardware.

| Empresa | Design System | Estrategia de Tokens | Arquitectura del código | Multiplataforma | Particularidad clave |
|---|---|---|---|---|---|
| **Spotify** | Encore | Semantic tokens + primitives | Tokens centralizados + librerías por plataforma | Web, iOS, Android, TV, Desktop | Los tokens semánticos permiten adaptar el mismo UI a contextos muy distintos (car, TV, mobile) |
| **The Walt Disney Company** | Disney Design System | Hybrid tokens (primitives + semantic) | Tokens globales + componentes por producto | Web, apps, parques, TV, streaming | Sistema pensado para coherencia de marca global en muchos productos distintos |
| **Notion** | Notion UI System | Hybrid ligero | Component-centric (componentes autocontenidos) | Web, Desktop, Mobile | Arquitectura muy cercana al código de React; prioriza velocidad de producto |
| **Tesla** | Tesla UI Platform | Semantic tokens | Framework UI interno con componentes por dispositivo | Auto UI, mobile app, web | El mismo lenguaje visual se adapta a pantallas del coche, app y web |

---

## 7. Diferencia Estructural

| Empresa | Prioridad del sistema |
|---|---|
| **Spotify** | Escalar UI a muchos contextos de consumo (TV, coche, móvil) |
| **Disney** | Mantener consistencia de marca global |
| **Notion** | Velocidad de desarrollo del producto |
| **Tesla** | UX consistente entre hardware y software |

---

## 8. Arquitectura Típica por Empresa

### Spotify — Encore

```
tokens/
  primitives/
  semantic/

platform/
  web/
  ios/
  android/
  tv/

components/
  button/
  card/
  player-controls/
```

> **Idea clave:** `tokens → platform implementation → components`

---

### The Walt Disney Company

```
tokens/
  colors/
  typography/
  motion/

themes/
  marvel/
  disney/
  starwars/

components/
  button/
  navigation/
  media-card/
```

> **Idea clave:** Escala de branding — mismo sistema, múltiples universos visuales.

---

### Notion

```
components/
  button/
    button.tsx
    button.css
  menu/
  editor/
```

> **Idea clave:** Component-driven UI. Muy poco sistema abstracto; máxima velocidad de producto.

---

### Tesla

```
tokens/
  semantic/

platform/
  car-os/
  mobile/
  web/

components/
  navigation/
  media/
  vehicle-controls/
```

> **Idea clave:** Hardware + software UI — un mismo lenguaje visual que cruza la pantalla del coche, la app y la web.

---

## Conclusión

Las empresas multiplataforma **no usan el mismo tipo de design system**.

| Tipo de empresa | Arquitectura dominante |
|---|---|
| Media / streaming | Semantic tokens *(Spotify)* |
| Brand global | Hybrid tokens *(Disney)* |
| Product SaaS | Component-centric *(Notion)* |
| Hardware + software | Semantic platform tokens *(Tesla)* |

---

## Insight Clave

> Cuando una empresa es multiplataforma, el Design System **deja de ser una librería de componentes** y pasa a ser una **infraestructura de diseño**.

Por eso casi todos terminan convergiendo en la misma stack:

```
Primitive tokens
      ↓
Semantic tokens
      ↓
Platform layer
      ↓
Components
```

---

*Próximo paso sugerido: arquitectura real de 6 design systems famosos (Stripe, Apple, Shopify, Spotify, Vercel, Airbnb) — la evolución histórica desde 2016 hasta 2026.*
