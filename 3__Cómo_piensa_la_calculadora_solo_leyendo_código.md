# 3. Cómo piensa la calculadora solo leyendo código

> "No me importa la intención, solo lo que el código hace."

---

## Flujo de análisis

### 1. Escanear el repositorio

- Encontrar carpetas y archivos relacionados con tokens (`tokens`, `theme`, `variables.css`, `*.tokens.*`).
- Encontrar componentes (naming convencional: `Button.tsx`, `*.component.*`, etc.).

---

### 2. Clasificar estrategia de tokens

Contar ocurrencias de:
- Valores literales (hex, px) en componentes.
- `var(--nombre)` y patrones de nombres (`color-*`, `space-*`, `button-*`).

Reglas de clasificación:

| Señal detectada | Clasificación |
|---|---|
| >X% de usos son literales | Sin tokens / tokens inmaduros |
| Predominan `blue-*`, `gray-*` | Token-first primitivo |
| Predominan `color-text-*`, `color-bg-*` | Semantic |
| Existen claras familias por componente | Hybrid |

---

### 3. Clasificar arquitectura

- Ver si hay `design-system/tokens` y `design-system/components`.
- Ver si hay `button/button.tsx` + `button.tokens.ts`.
- Ver si hay `platform/web`, `platform/ios`, etc.

---

### 4. Aplicar reglas y anti‑patrones

- Para cada componente, listar los tipos de tokens usados y valores directos.
- Detectar mezclas peligrosas:
  - Varios niveles de tokens mezclados.
  - Uso de primitives en componentes "maduros".
  - Duplicación de tokens.

---

### 5. Generar recomendaciones sin mirar fuera

Basadas solo en reglas internas:

> *"Tu patrón de uso de tokens se parece a X, pero violás regla Y, por eso te recomiendo Z."*

> *"Tu arquitectura de carpetas sugiere modelo A, pero tenés señales de B; eso te coloca en un híbrido inestable."*
