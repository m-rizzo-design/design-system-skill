# Design System Auditor

Herramienta de diagnóstico personal para auditar Design Systems analizando código fuente. El objetivo es evaluar la madurez de un DS en ~20 minutos y determinar qué hay que hacer y quién debe hacerlo.

Contexto de uso: consultoría y proyectos propios. No es un producto público (todavía).

---

## Qué hace

1. Recopila contexto de la empresa (equipo, fase, plataformas, prioridades)
2. Escanea el repositorio buscando tokens, componentes y estilos
3. Clasifica el modelo de tokens y la arquitectura de código
4. Detecta anti-patrones con severidad
5. Genera un score de salud ponderado
6. Produce un reporte con diagnóstico, plan de cambios e impacto esperado

Funciona como Claude Skill (SKILL.md) y opcionalmente con un scanner Python (scanner.py) que automatiza la fase de recolección de datos.

---

## Mapa de archivos

### Operativos — los que Claude usa en runtime

| Archivo | Rol | Estado |
|---------|-----|--------|
| `SKILL.md` | Skill principal. Autocontenida. Define las 6 fases de auditoría, lógica de clasificación, anti-patrones, scoring y template de reporte | ✅ Operativo |
| `scanner.py` | Script Python que automatiza la Fase 1 (escaneo del repo). Produce JSON con métricas para pasarle a Claude como contexto | ✅ Funcional |

### Base de conocimiento — fuente de verdad para razonar

| Archivo | Contenido | Estado |
|---------|-----------|--------|
| `1__Diccionario_de_modelos_de_Design_System.md` | Definición completa de cada modelo de tokens (sin tokens, primitive, semantic, hybrid) y cada modelo de arquitectura (centralized, co-located, multiplatform). Incluye señales en código, cuándo funciona, cuándo deja de ser ese modelo y mezclas peligrosas | ✅ Completo |
| `2__Reglas_y_anti-patrones_para_el_analizador.md` | Reglas concretas de consistencia, arquitectura y pipeline que la Skill puede aplicar leyendo solo código. Lista de anti-patrones detectables | ✅ Completo |
| `3__Cómo_piensa_la_calculadora_solo_leyendo_código.md` | Flujo de análisis de 5 pasos: escaneo → clasificación → arquitectura → anti-patrones → recomendaciones. Principio base: "no me importa la intención, solo lo que el código hace" | ✅ Completo |
| `4__Taxonomia_Umbrales_y_Transiciones.md` | Taxonomía de nombres de tokens con regex, árbol de decisión, umbrales numéricos para clasificación, tabla de puntajes, mapa modelo→reglas, y guías de migración paso a paso entre modelos | ✅ Completo |
| `DS-Real-Cases.md` | Casos reales de migración e implementación de DS con ROI documentado: PedidosYa, empresa B2B SaaS, migración legacy, y big tech (Google, IBM, Shopify, Adobe) | ✅ Completo |
| `Design_Systems_Modernos___Clasificaciones_y_Análisis_Comparativo.md` | Análisis comparativo de modelos modernos. Empresas multiplataforma: Spotify, Disney, Notion, Tesla. Referencia para benchmarks | ✅ Completo |
| `compass_artifact_wf-1ccab4e0-2272-4a14-b245-bf87ae875f8a_text_markdown.md` | Research profundo sobre métricas de negocio, arquitectura de componentes, patrones modernos (Atomic, Compound, Headless), herramientas de análisis y ROI de migraciones. Fuente principal para docs 7 y 10 | ✅ Solo research — no destilado aún |

### Gestión del proyecto

| Archivo | Contenido | Estado |
|---------|-----------|--------|
| `ds-matrix-plan-18-may.md` | Plan de trabajo con gaps pendientes, orden de ejecución y actualizaciones necesarias en SKILL.md | ✅ Referencia activa |

---

## Documentos pendientes de crear

Estos 4 documentos están planificados pero no existen todavía. Son el trabajo pendiente principal.

### `7__Arquitectura_de_Componentes.md`
**Qué es:** Framework de análisis de estructura de componentes — el segundo eje de auditoría además de tokens.

**Qué debe incluir:**
- Métricas accionables: LOC por componente (healthy <300, crítico >500), complejidad ciclomática, reuse rate (target >80%)
- 5 anti-patrones detectables con síntomas y solución: God Component, Prop Drilling, Component Duplication, Over-Abstraction, Tight Coupling
- Patrones modernos de referencia: Atomic Design, Compound Components, Headless Components (Radix, React Aria, Ark UI)
- Herramientas de detección automática: jscpd, dependency-cruiser, Omlet.dev, react-component-analyzer
- Umbrales de detección por métrica

**Fuente principal:** `compass_artifact_wf-*.md` sección AREA 2

**Impacto en SKILL.md:** Añadir Fase 1b entre el escaneo actual y la clasificación de tokens

---

### `9__Discovery_Questions.md`
**Qué es:** Banco de preguntas de contexto estructuradas por dimensión, para reemplazar las 5 preguntas genéricas actuales de la Fase 0.

**Qué debe incluir:**
- Preguntas agrupadas en 4 dimensiones: Equipo, Producto, Técnica, Negocio
- Preguntas mínimas obligatorias (siempre se hacen, independiente de la fase)
- Preguntas opcionales con condición de activación (ej: "solo si tiene más de 2 productos")
- Guía de selección por fase de empresa: Pre-seed vs Seed/Serie A vs Serie B+ vs Enterprise
- Señales de alerta que cambian el enfoque de la auditoría

**Impacto en SKILL.md:** Reemplazar Fase 0 completa

---

### `10__Scoring_Formula.md`
**Qué es:** Fórmula extendida de scoring que contempla los 3 ejes del sistema y contextualiza el resultado por fase de empresa.

**Qué debe incluir:**
- Fórmula de 3 ejes: tokens (50%) + componentes (30%) + arquitectura (20%) — pesos a confirmar
- Cálculo detallado de cada sub-score con sus métricas y pesos internos
- Tabla de interpretación contextualizada por fase (score 60 en Seed ≠ score 60 en Serie B)
- Lógica de penalizaciones por anti-patrones críticos (AP-01, AP-04, AP-05, AP-09)
- Formato de salida legible para no-técnicos: label (Disfuncional/Aceptable/Bueno/Excelente) + semáforo + sub-scores

**Decisión pendiente antes de escribir:** confirmar si el score es único o 3 sub-scores independientes

**Impacto en SKILL.md:** Reemplazar Fase 5 completa

---

### `11__Report_Template.md`
**Qué es:** Template completo de reporte profesional, listo para entregar a un CTO o equipo de producto sin edición manual.

**Qué debe incluir:**
- Executive summary de 3 líneas para no-técnicos (CEO/CTO)
- Score visual con interpretación contextualizada por fase
- Diagnóstico técnico: modelo detectado, comparación con empresa de referencia, diferencias clave
- Anti-patrones críticos con impacto de negocio traducido (no solo técnico)
- Sección "qué no tocar ahora" (evitar sobre-ingeniería)
- Plan de cambios con estimación de esfuerzo realista (semanas/meses)
- Estimación de ROI con benchmarks citados y fuentes
- Métricas de negocio a medir post-implementación
- Firma, fecha, versión del auditor

**Dependencia:** requiere Doc 10 (scoring) y Doc 9 (discovery) finalizados primero

**Impacto en SKILL.md:** Reemplazar Fase 6 completa

---

## Orden de lectura para un agente nuevo

Si sos un agente entrando a este proyecto por primera vez, leé en este orden:

1. `README.md` — este archivo. Contexto completo del proyecto
2. `SKILL.md` — para entender qué produce el sistema y cómo funciona hoy
3. `ds-matrix-plan-18-may.md` — para entender qué está pendiente y por qué
4. El doc de conocimiento relevante para la tarea asignada (ver mapa arriba)
5. `compass_artifact_wf-*.md` — solo si necesitás material de research para construir docs 7 o 10

No es necesario leer todos los docs de conocimiento para trabajar en una tarea específica.

---

## Orden de ejecución de tareas pendientes

| Prioridad | Tarea | Bloqueante de |
|-----------|-------|---------------|
| 1 | Crear `10__Scoring_Formula.md` | Doc 11 |
| 2 | Crear `9__Discovery_Questions.md` | Doc 11, SKILL.md Fase 0 |
| 3 | Crear `11__Report_Template.md` | Entregable final |
| 4 | Crear `7__Arquitectura_de_Componentes.md` | SKILL.md Fase 1b |
| 5 | Actualizar `SKILL.md` con las 4 fases modificadas | — |

---

## Cómo usar el scanner

```bash
# Instalar dependencias (ninguna externa — solo stdlib de Python)
python3 scanner.py --root /path/al/repo

# Con output a archivo JSON
python3 scanner.py --root /path/al/repo --output resultado.json

# El JSON resultante se pega como contexto a Claude con el SKILL.md activo
```

El scanner automatiza la Fase 1 del SKILL.md. Si no se usa el scanner, la Fase 1 se puede ejecutar manualmente con los comandos bash incluidos en el SKILL.md.

---

## Principios del proyecto

- **Distillar, no documentar:** cada doc contiene solo lo necesario para que Claude razone bien — no referencia exhaustiva
- **Claims verificables:** los benchmarks y casos reales tienen fuente citada
- **Un archivo, un propósito:** no mezclar roles entre documentos
- **Scope front-end:** el audit no cubre backend, infraestructura ni pipelines de datos
- **Agnóstico de framework:** funciona con CSS, SCSS, CSS-in-JS, Tailwind
