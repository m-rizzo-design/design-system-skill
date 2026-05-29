# 2. Reglas y anti‑patrones para el analizador

> Estas son reglas que la calculadora puede usar directamente, leyendo solo código.

---

## 2.1. Reglas de consistencia de tokens

**Regla 1: "Un componente debe consumir un solo nivel de tokens por tipo de decisión"**

- Ejemplo correcto:
  - Colores: solo semantic o solo component tokens.
  - Spacing: solo primitives.
- Anti‑patrón: `button` usa `blue-500`, `color-text-primary` y `button-bg` a la vez.

---

**Regla 2: "Tokens primitives no deberían usarse en componentes de alto nivel"**

- Permitido en: variables internas, implementación de semantic tokens.
- Señal de problema: primitives usados directamente en muchos componentes distintos.

---

**Regla 3: "Tokens de componente no deben usarse fuera de ese componente"**

- `button-bg` solo en el botón.
- Anti‑patrón: `card` usando `button-radius` porque "ya existía".

---

**Regla 4: "Cada token semántico debe tener un mapping claro a primitives"**

- Si el analizador encuentra `color-text-primary` sin definición en ningún lado → deuda.
- Si hay dos definiciones distintas en distintos archivos → conflicto.

---

## 2.2. Reglas de arquitectura

**Regla 1: "Tokens se definen en un número limitado de lugares"**

- Ideal: 1 fuente por tipo de token (una carpeta / paquete).
- Anti‑patrón: el analizador detecta 3–4 carpetas distintas que definen `tokens/colors` incompatibles.

---

**Regla 2: "Componentes no deben redefinir tokens ya definidos globalmente salvo para casos bien marcados (override/variant)"**

- Si hay `button.tokens.ts` redefiniendo cosas que ya existen en `tokens/components/button` → mala señal.

---

**Regla 3: "No mezclar inline styles con sistema de tokens en componentes reutilizables"**

- Inline style con valores mágicos es señal de bypass del sistema.

---

**Regla 4: "En multiplataforma, hay una fuente de tokens core referenciada por todas las plataformas"**

- Anti‑patrón: `web/tokens` y `mobile/tokens` sin dependencia de un core común.

---

## 2.3. Reglas de pipeline diseño→código

*(Aunque la app mire solo código)*

**Señal de pipeline inmaduro**
- Tokens definidos en muchos formatos ad‑hoc (TS, SCSS, JSON) sin patrón claro.
- Falta de archivos generados o de scripts de build relacionados con tokens.

**Señal de pipeline sano**
- Archivos marcados como "generated" o rutas tipo `tokens/build/` que el código consume.
- Scripts o comments en repo que indican generación a partir de fuentes (aunque no se vea Figma).

---

## 2.4. Anti‑patrones concretos que la calculadora debería detectar

- Mezcla de Tailwind utilities + tokens + valores mágicos en los mismos componentes.
- Temas múltiples implementados como "copias" del CSS base en lugar de variar tokens.
- Tokens con nombres semánticos pero usados como primitives (misma definición repetida para muchos tokens distintos).
- Componentes con más de N valores directos (ej: más de 3 colores literales) → sugerir "extraer a tokens".
