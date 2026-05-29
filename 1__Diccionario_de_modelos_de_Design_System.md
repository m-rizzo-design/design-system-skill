# 1. Diccionario de modelos de Design System

---

## 1.1. Modelos de tokens (Eje "cómo se definen los estilos")

### A. Sin tokens (estilos directos)

**Definición**
Estilos escritos como valores literales (hex, px, rem) o clases utilitarias sin capa de abstracción. No existe una capa clara de `tokens/` ni de CSS variables de diseño.

**Señales en código**
- CSS con `#1A73E8`, `16px`, `border-radius: 8px` repetidos en muchos sitios.
- Componentes que nunca usan `var(--algo)` ni constantes de tema.

**Cuándo deja de ser este modelo**
En el momento en que existe una colección mínima de constantes o variables de diseño reutilizadas de forma sistemática.

**Anti‑patrones típicos**
- Mezclar utilidades tipo Tailwind con valores "a mano" sin una estrategia (ej: `text-blue-500` + `#1976d2`).
- "Theme" que solo es un JSON de colores sueltos sin mapear a intención.

---

### B. Token‑first primitivo

**Definición**
Tokens representan valores crudos: colores, espacios, tipografías, radios. Nombres tipo `color-blue-500`, `space-4`, `radius-md`, `font-body`.

**Señales en código**
- Archivos `tokens/colors`, `tokens/spacing`, etc.
- Uso extensivo de `var(--color-blue-500)`, `var(--space-4)` en componentes.

**Cuándo deja de ser token‑first primitivo**
Cuando aparecen capas sistemáticas de intención (`color-text-primary`) y/o tokens de componente (`button-bg`) que se usan de forma predominante.

**Cuándo funciona bien**
- Productos pequeños/medianos, una sola marca, poca necesidad de re‑branding.
- Equipos que priorizan control fino sobre el look & feel.

**Riesgos de mezclar mal**
Usar primitives directamente en componentes críticos mientras también existen tokens semánticos → duplicación de lógica de color/espacio y UI inconsistente.

---

### C. Semantic‑first

**Definición**
Tokens nombran intención, no valores físicos. Ejemplos: `color-text-primary`, `color-bg-surface`, `border-subtle`.

**Señales en código**
- Uso dominante de tokens semánticos en componentes.
- Una capa (aunque sea implícita) de mapeo desde valores crudos a tokens semánticos.

**Cuándo deja de ser semantic‑first**
- Cuando los componentes empiezan a depender directamente de `blue-500` y compañía para casos normales (no excepciones).
- Cuando aparecen muchos tokens por componente (`button-bg`, `card-radius`) usados como primera elección.

**Cuándo funciona bien**
- Empresas donde branding y contexto cambian: múltiples productos, temas, modos.
- Diseños que deben adaptarse a TV, coche, mobile, etc.

**Mezcla peligrosa**
Semantic tokens definidos, pero los componentes siguen usando mostly primitives → el sistema "cree" ser semántico, pero en la práctica no lo es.

---

### D. Hybrid tokens (primitives + semantic + component tokens)

**Definición**
Tres niveles claros:
- **Primitives:** `blue-500`, `space-4`
- **Semantic:** `color-text-primary`, `color-bg-surface`
- **Component:** `button-bg`, `card-radius`

**Señales en código**
- Carpetas/archivos diferenciados: `tokens/primitives`, `tokens/semantic`, `tokens/components`.
- Componentes leen sobre todo component tokens o semánticos, raramente primitives directas.

**Cuándo deja de ser "buen híbrido"**
- Cuando cualquier componente puede usar cualquier nivel sin reglas → caos.
- Cuando se crean tokens de componente para todo pero nadie los mantiene ni documenta.

**Cuándo funciona bien**
- Design systems multiplataforma y multiequipo.
- Cuando hay alguien que gobierna taxonomía y escalabilidad de tokens.

**Mezclas a evitar**
- Componentes que mezclan en el mismo archivo: `blue-500`, `color-text-primary` y `button-bg` sin una prioridad clara.
- Tokens de componente que se comportan como primitives (mismos valores, reutilización fuera del componente).

---

## 1.2. Modelos de arquitectura de código (Eje "cómo se organiza el sistema")

### A. Centralized token architecture

**Definición**
Repo o paquete `design-system/` con `tokens/` globales y `components/` que los consumen.

**Señales en código**
```
design-system/
  tokens/
  components/
```
Pocas definiciones de tokens fuera de ese paquete.

**Deja de ser este modelo cuando**
- Los equipos empiezan a definir tokens locales dentro de componentes o repos externos ("tokens shadow").
- Varias fuentes de tokens compiten.

**Cuándo funciona bien**
- Organización con gobierno central fuerte (brand team, design system team).
- Necesidad de consistencia global por encima de velocidad local.

**Peligros**
- Si se intenta mezclar con co‑location sin reglas, aparecen "tokens duplicados": globales y locales contradictorios.
- Capa de tokens se convierte en cuello de botella (todo cambio pasa por un único equipo).

---

### B. Component‑co‑located

**Definición**
Cada componente tiene su carpeta con lógica, estilos, tokens y tests.

**Señales en código**
```
button/
  button.tsx
  button.css
  button.tokens.ts
  button.test.ts
```

**Deja de ser puro co‑located cuando**
- Aparece un directorio de tokens globales que los componentes usan más que sus propios tokens locales.
- El sistema introduce un build step que centraliza tokens para varias plataformas.

**Cuándo funciona bien**
- Productos SaaS con foco en velocidad.
- Equipos que quieren versionar componentes como unidades portables.

**Riesgos al combinar con tokens centralizados**
- Doble autoridad: tokens globales que dicen una cosa, tokens locales que dicen otra.
- Dificultad para saber "quién manda" cuando hay conflicto.

---

### C. Multiplatform infra (tokens + platform layer + components)

**Definición**
Arquitectura estructurada en tres capas:

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
```

**Señales en código**
- Presencia de `platform/` o `packages/web`, `packages/native`, etc. consumiendo la misma fuente de tokens.
- Adaptaciones por plataforma que derivan de tokens semánticos.

**Deja de ser este modelo cuando**
- Las plataformas empiezan a duplicar tokens "porque necesitan algo especial" y esa especialización no se modela bien.
- Cada plataforma define su propio sistema de tokens sin un core común.

**Cuándo funciona bien**
- Empresas multimedia, hardware/software, múltiples dispositivos.
- Cuando hay disciplina para mantener tokens core y variaciones por plataforma bien separadas.
