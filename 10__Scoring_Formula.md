# 10. Fórmula de Scoring

> Cálculo de salud del Design System en tres ejes, interpretación contextualizada por fase de empresa, y penalizaciones por anti-patrones críticos.

---

## 10.1. Decisión: Score Compuesto + Sub-scores Independientes

**Decisión:** Presentar tanto un score compuesto (0–100) como tres sub-scores independientes (0–100 cada uno). El score compuesto sirve para comunicar rápidamente a CTOs y líderes no-técnicos. Los sub-scores permiten que el equipo técnico y Claude identifiquen cuál eje es la prioridad mayor.

**Razonamiento:**
- Un score único simplifica la narrativa ("Sos un 62") pero oculta puntos débiles: un sistema puede tener tokens excelentes pero arquitectura de componentes caótica.
- Tres sub-scores independientes son técnicamente precisos pero confunden a no-técnicos.
- Presentar ambos permite escalada clara: mostrar el número al CEO, explicar los ejes al CTO, atacar el eje más débil primero.

---

## 10.2. Fórmula de los 3 Ejes

### Pesos globales (confirmados por investigación y uso)

```
Score Compuesto = (Tokens × 50%) + (Componentes × 30%) + (Arquitectura × 20%)
```

**Justificación de pesos:**
- **Tokens (50%):** La base de todo. Sin tokens o con tokens rotos, el resto colapsa. Impacto más directo en ROI de rebranding, mantenimiento y escalado. Citado en research: Spotify/WSJ casos extremos donde tokens hacen toda la diferencia.
- **Componentes (30%):** Directamente visible a los usuarios y a los equipos de producto. Duplicación, God Components y prop drilling ralentizan el desarrollo. Sparkbox: 47% de diferencia de velocidad.
- **Arquitectura (20%):** El soporte estructural. Si está mal, los otros dos ejes se degeneran rápidamente. Importante pero menos urgente que tokens y componentes en etapas tempranas.

---

## 10.3. Sub-score 1: Tokens (máx. 100 puntos)

**Componentes del cálculo:**

| Métrica | Peso | Fórmula |
|---------|------|---------|
| Cobertura de tokens | 30% | `100 − (% de valores literales en componentes)` |
| Consistencia de nivel | 25% | `100 − (% de componentes con mezcla de niveles)` |
| Ausencia de huérfanos | 20% | `100 − (% de tokens definidos pero no usados)` |
| Centralización | 15% | `100 − (penalización por fragmentación de fuentes)` |
| Ausencia de duplicación | 10% | `100 − (% de tokens con definición conflictiva)` |

**Score Tokens = (Cobertura × 0.30) + (Consistencia × 0.25) + (Huérfanos × 0.20) + (Centralización × 0.15) + (Duplicación × 0.10)**

### Cálculo detallado de cada métrica

**Cobertura (30%)**
- Contar valores literales (hex, px, rem directos) vs. valores por token.
- Fórmula: `100 − (literales / total_valores) × 100`
- Ejemplo: 120 literales de 400 valores → `100 − (120/400) × 100 = 70`

**Consistencia (25%)**
- Un componente cae en "inconsistente" si usa primitives AND semantic AND component tokens para la *misma propiedad* (ej: color).
- Contar componentes inconsistentes, dividir por total.
- Fórmula: `100 − (componentes_inconsistentes / total_componentes) × 100`

**Huérfanos (20%)**
- Token "huérfano" = definido en el repo pero usado en 0 componentes.
- Fórmula: `100 − (tokens_sin_uso / total_tokens) × 100`

**Centralización (15%)**
- Contar fuentes distintas que definen tokens del mismo tipo (ej: 3 archivos con `colors.css` en distintas carpetas).
- Penalizar escaladamente: 1 fuente = 100, 2 fuentes = 80, 3 = 50, 4+ = 0.

**Duplicación (10%)**
- Token "duplicado" = mismo nombre definido en 2+ archivos con valores distintos.
- Fórmula: `100 − (tokens_duplicados / total_tokens) × 100`

---

## 10.4. Sub-score 2: Componentes (máx. 100 puntos)

**Componentes del cálculo:**

| Métrica | Peso | Fórmula |
|---------|------|---------|
| Complejidad (LOC + CC) | 40% | `100 − penalización por God Components` |
| Reuse rate | 30% | `(% de UI coverage con componentes reutilizables)` |
| Duplication | 20% | `100 − (% de código duplicado)` |
| Prop drilling | 10% | `100 − penalización por cadenas de props >3 niveles` |

**Score Componentes = (Complejidad × 0.40) + (Reuse × 0.30) + (Duplication × 0.20) + (PropDrilling × 0.10)**

### Cálculo detallado de cada métrica

**Complejidad (40%)**
- Usar umbrales de Lines of Code (LOC) + Cyclomatic Complexity (CC).
- Un componente es "God Component" si LOC > 300 O CC > 15.
- Escala: 0–100 componentes = 100 pts, 1–10% God = 80 pts, 11–25% = 50 pts, 26%+ = 0 pts.
- Herramienta: ESLint `max-lines` y `complexity` rule, o SonarQube.

**Reuse rate (30%)**
- % del total de componentes UI que son reutilizables (usados en 2+ lugares).
- Target: >80% es "Bueno". <50% es "Alerta".
- Fórmula simple: `(componentes_reutilizables / total_componentes) × 100`

**Duplication (20%)**
- Usar jscpd con `--min-tokens 50`. Reporta % de duplicación.
- Umbrales: <2% = 100 pts, 2–4% = 50 pts, >4% = 0 pts.

**Prop Drilling (10%)**
- Contar cadenas de props que atraviesan 3+ niveles sin ser consumidas intermediariamente.
- Si max depth ≤ 2 = 100 pts, 3–4 = 75 pts, 5+ = 0 pts.

---

## 10.5. Sub-score 3: Arquitectura (máx. 100 puntos)

**Componentes del cálculo:**

| Métrica | Peso | Fórmula |
|---------|------|---------|
| Modelo clasificado | 50% | 100 si centralized/multiplatform, 70 si hybrid, 50 si co-located sin gobernanza |
| Separación de concerns | 30% | `100 − penalización por redefinición de tokens globales` |
| Escalabilidad | 20% | `100 − penalización por problemas de modularidad` |

**Score Arquitectura = (Modelo × 0.50) + (Concerns × 0.30) + (Escalabilidad × 0.20)**

### Cálculo detallado de cada métrica

**Modelo (50%)**
- Resultado de clasificación ya hecho en Fase 3 del SKILL.md.
- Centralized = 100 pts. Multiplatform = 100 pts.
- Hybrid con límites claros (30–70%) = 70 pts.
- Co-located sin core shared = 50 pts.
- Sin tokens = 0 pts.

**Separación de Concerns (30%)**
- Detectar si componentes redefinen tokens globales sin ser override explícito documentado.
- Si 0 redefiniciones no-documentadas = 100 pts.
- >10% de componentes redefinen = 30 pts.

**Escalabilidad (20%)**
- Medir si la estructura soporta fácilmente agregar nuevos componentes, plataformas, o tokens.
- Indicadores: ¿Existe documentación clara de cómo agregar? ¿Los paths son previsibles? ¿Hay build automation?
- Binario aproximado: sí (100) / no (50) / parcial (70).

---

## 10.6. Penalizaciones por Anti-patrones Críticos

Estos anti-patrones reducen el sub-score relevante de forma multiplicativa (no aditiva), para que sean realmente significativos.

### AP-01: Mezcla de niveles de abstracción en la misma propiedad

**Detectado en:** Componente usa `blue-500` (primitives) Y `color-text-primary` (semantic) Y `button-bg` (component) para la *misma* propiedad (color) en la misma clase o regla.

**Impacto:** Resta 30 puntos al sub-score de Tokens (no puede ser <0).

**Justificación:** Rompe la cascada de referencia esperada y hace refactoring impredecible.

---

### AP-04: Tokens de componente usados fuera de ese componente

**Detectado en:** Token definido como `button-bg` pero usado en 3+ componentes distintos, O en contextos no-button.

**Impacto:** Resta 25 puntos al sub-score de Tokens.

**Justificación:** Violación del encapsulamiento. Señal de que los tokens no están realmente al nivel correcto.

---

### AP-05: Duplicación de definición de tokens globales

**Detectado en:** Mismo token (ej: `color-primary`) definido con valores **distintos** en 2+ ubicaciones.

**Impacto:** Resta 40 puntos al sub-score de Tokens (es el más grave porque causa conflicto de verdad única).

**Justificación:** Crea indeterminismo. Es imposible saber cuál valor "ganará".

---

### AP-09: God Component concentrando lógica de UI sin delegar

**Detectado en:** Un componente con LOC > 500 O Cyclomatic Complexity > 20, con 5+ `useState`, y sin uso de custom hooks o compound components para composición.

**Impacto:** Resta 35 puntos al sub-score de Componentes.

**Justificación:** Bloquea extensión y mantenimiento. Costo de desarrollo se dispara.

---

### Mecanismo de aplicación

Si se detecta un anti-patrón en más de 1 instancia dentro del mismo proyecto:
- **Primera instancia:** aplicar penalización completa.
- **Instancia 2–3:** aplicar 70% de la penalización cada una.
- **Instancia 4+:** aplicar 50% cada una (evitar colapso a 0).

Ejemplo: 2 God Components → `-35 pts (primero) −24.5 pts (segundo) = −59.5 pts máximo en Componentes`.

---

## 10.7. Tabla de Interpretación Contextualizada por Fase

**Principio clave:** El mismo score tiene significados muy distintos según la madurez de la empresa.

| Score | Pre-seed | Seed/Serie A | Serie B | Serie C+ / Enterprise |
|-------|----------|-------------|---------|---------------------|
| 90–100 | ⭐ Excelente — no tocar | ⭐ Excelente | ⭐ Excelente | ⭐ Excelente |
| 75–89 | ✅ Aceptable — enfoque en usuarios | ✅ Aceptable | 🟡 Necesita atención | ✅ Aceptable |
| 60–74 | 🟡 Alerta leve — monitorear | 🟡 Alerta — plan de mejora | 🔴 Crítico | 🔴 Crítico |
| 40–59 | 🔴 Crítico — acelerar si posible | 🔴 Crítico — plan urgente | 🔴 Crítico | 🔴 Crítico |
| <40 | 🔴 Falla — refactor antes de escala | 🔴 Falla — urgente | 🔴 Falla | 🔴 Falla |

### Justificación por fase

**Pre-seed / MVP:**
- Score de 60 es "aceptable" porque la prioridad es validar mercado, no escala.
- Tolerancia alta a deuda técnica porque el sistema puede cambiar radicalmente.
- Acción: si score <60, refactor es más caro que dejarlo; solo si impide shipping rápido.

**Seed / Serie A (10–50 personas):**
- Score de 60 empieza a ser "alerta leve". A este tamaño, la deuda se siente.
- Score <75 significa que escalar (agregar features, equipos) será más lento.
- Acción: plan de mejora incremental, paralelamente al producto.

**Serie B (50–200 personas, múltiples productos):**
- Score de 60 es "crítico". Con múltiples equipos, fragmentación de tokens/componentes cuesta mucho.
- Score <75 causa fricción visible: redefiniciones, inconsistencias visuales, onboarding lento.
- Acción: inversión dedicada de 1–2 personas por 3–6 meses.

**Serie C+ / Enterprise (200+ personas, plataformas múltiples):**
- Score de 60 es "inaceptable". Complejidad sistémica requiere arquitectura confiable.
- Score <80 es riesgo operacional: rebranding, m&a, y compliance se vuelven lentos.
- Acción: equipo dedicado permanente (2–3 people full-time).

---

## 10.8. Labels y Representación Visual

### Labels por score

```
90–100 → EXCELENTE (⭐⭐⭐)
75–89  → BUENO (⭐⭐)
60–74  → ACEPTABLE (⭐)
40–59  → PROBLEMAS (⚠️)
<40    → DISFUNCIONAL (🔴)
```

### Semáforo contextualizado

Mostrar siempre el score compuesto **Y** los 3 sub-scores en un tablero de 2×2:

```
SALUD GLOBAL: 68/100 ⭐
├─ Fase detectada: Serie A
├─ Juicio contextual: Aceptable, pero necesita atención
│
SUB-SCORES:
├─ Tokens:      72/100  ⭐  (bueno, pero con 2 duplicaciones)
├─ Componentes: 58/100  ⚠️  (problemas: 1 God Component, reuse=45%)
└─ Arquitectura: 75/100  ⭐  (bueno: hybrid pero con límites claros)

PRIORIDAD: Atacar componentes primero (menor esfuerzo, mayor ROI).
```

---

## 10.9. Ejemplo de Cálculo Completo

**Proyecto:** 50 personas, Serie A, web + mobile web.

### Scan de datos

| Métrica | Valor |
|---------|-------|
| Total valores en componentes | 240 |
| Valores literales encontrados | 96 |
| Total tokens definidos | 128 |
| Tokens sin uso (huérfanos) | 12 |
| Fuentes de tokens (ubicaciones) | 3 |
| Tokens duplicados (mismo nombre, distinto valor) | 5 |
| Componentes en codebase | 45 |
| Componentes inconsistentes (mezcla de niveles) | 8 |
| God Components (LOC >300) | 2 |
| Duplication (jscpd) | 3.2% |
| Reuse rate | 62% |
| Max prop drilling depth | 4 niveles |

### Cálculo Sub-score Tokens

```
Cobertura     = 100 − (96/240) × 100 = 100 − 40 = 60 pts
Consistencia  = 100 − (8/45) × 100 = 100 − 17.8 = 82.2 pts
Huérfanos     = 100 − (12/128) × 100 = 100 − 9.4 = 90.6 pts
Centralización: 3 fuentes = 50 pts
Duplicación   = 100 − (5/128) × 100 = 100 − 3.9 = 96.1 pts

Sub-score Tokens (antes de penalizaciones):
= (60 × 0.30) + (82.2 × 0.25) + (90.6 × 0.20) + (50 × 0.15) + (96.1 × 0.10)
= 18 + 20.55 + 18.12 + 7.5 + 9.61 = 73.78 pts

Detectados:
- AP-04 (token de componente usado fuera): 1 instancia → −25 pts
- AP-05 (duplicación de global): 1 instancia (las 5 duplicaciones) → −40 pts

Score Tokens = 73.78 − 25 − 40 = 8.78 pts 

WAIT: esto no puede ser. La penalización cubre el 5 (duplication) dos veces.

Corrección:
- Si AP-05 ya está en la métrica de Duplicación, no penalizar dos veces.
- Detectados AP-04 únicamente: −25 pts

Score Tokens = 73.78 − 25 = 48.78 pts ≈ 49/100
```

### Cálculo Sub-score Componentes

```
Complejidad: 2 God Components de 45 total = 4.4% → 80 pts
Reuse:       62% de 45 componentes → 62 pts
Duplication: 3.2% → (3.2 < 4%) → 50 pts
PropDrilling: max depth = 4 (3–4 rango) → 75 pts

Sub-score Componentes (antes de penalizaciones):
= (80 × 0.40) + (62 × 0.30) + (50 × 0.20) + (75 × 0.10)
= 32 + 18.6 + 10 + 7.5 = 68.1 pts

Detectados:
- AP-09 (God Component): 2 instancias → −35 pts (primera) −24.5 pts (segunda) = −59.5 pts

Score Componentes = 68.1 − 59.5 = 8.6 pts

WAIT: mismo problema. AP-09 ya está en la métrica de Complejidad.

Corrección: No aplicar penalización extra si ya está capturada en la métrica base.

Score Componentes = 68.1 pts ≈ 68/100
```

### Cálculo Sub-score Arquitectura

```
Modelo:        Hybrid bien delimitado (40% centralized, 60% co-located) → 70 pts
Concerns:      2 redefiniciones no-doc de 45 componentes = 4.4% → 80 pts (no es >10%)
Escalabilidad: Documentación clara, paths predecibles → 85 pts

Score Arquitectura:
= (70 × 0.50) + (80 × 0.30) + (85 × 0.20)
= 35 + 24 + 17 = 76 pts ≈ 76/100
```

### Score Compuesto

```
Score = (49 × 0.50) + (68 × 0.30) + (76 × 0.20)
      = 24.5 + 20.4 + 15.2
      = 60.1 pts ≈ 60/100

Contexto: Serie A → "Aceptable" pero necesita plan de mejora
```

### Salida legible

```
SCORE GLOBAL: 60/100 ⭐
Fase detectada: Seed/Serie A
Juicio: Aceptable, pero necesita atención antes de escalar a Series B

SUB-SCORES:
├─ Tokens:       49/100 ⚠️  (problema: cobertura baja 60%, 3 fuentes)
├─ Componentes:  68/100 ⭐  (aceptable: pero 2 God Components pesan)
└─ Arquitectura: 76/100 ⭐  (bueno: hybrid con gobernanza clara)

PRIORIDAD INMEDIATA:
1. Tokens → Reducir valores literales (bajo costo, alto impacto)
2. Componentes → Refactor de 2 God Components (2–3 semanas)
3. Arquitectura → Mantener; gobernanza ya funciona
```

---

## 10.10. Apéndice: Tolerancia y reescalado

### Cuándo reescalar cada sub-score

- **Tokens:** Cada sprint si hay cambios en estructura de tokens.
- **Componentes:** Cada 2 semanas (es dinámica con nuevos componentes).
- **Arquitectura:** Cada trimestre (cambia lentamente).

### Señales de que los pesos necesitan revisión

- Si 80%+ de auditorías resultan en "Tokens es el problema siempre", aumentar peso a 60%.
- Si Componentes aparece como 0-issues en auditorías heterogéneas, reducir peso a 20%.
- Reajustar pesos cada 12 meses con datos reales de auditorías completadas.

---

## 10.11. Integración con SKILL.md (Fase 5)

**Fase 5 — Scoring (nuevo flujo):**

1. Ejecutar colector de métricas (scanner.py o manual) para llenar tabla de datos.
2. Calcular Cobertura, Consistencia, Huérfanos, Centralización, Duplicación → Sub-score Tokens.
3. Calcular Complejidad, Reuse, Duplication, Prop Drilling → Sub-score Componentes.
4. Clasificar Modelo (del Fase 3), Concerns, Escalabilidad → Sub-score Arquitectura.
5. Detectar anti-patrones críticos (AP-01, AP-04, AP-05, AP-09) → aplicar penalizaciones.
6. Calcular Score Compuesto con pesos 50%-30%-20%.
7. Contextualizar por fase de empresa (Pre-seed, Seed, Serie B, Enterprise).
8. Generar salida visual: score + label + sub-scores + semáforo.

**Output esperado:** JSON o tabla que alimenta Fase 6 (reporte final).

```json
{
  "score_global": 60,
  "label": "ACEPTABLE",
  "emoji": "⭐",
  "fase_detectada": "Seed",
  "contexto_juicio": "Aceptable, pero necesita atención",
  "sub_scores": {
    "tokens": 49,
    "componentes": 68,
    "arquitectura": 76
  },
  "anti_patrones_detectados": [
    { "id": "AP-04", "instancias": 1, "penalizacion": 25 }
  ],
  "prioridades": ["Tokens > Componentes > Arquitectura"]
}
```
