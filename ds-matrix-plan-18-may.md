# DS Auditor — Plan de trabajo
**Fecha:** 18 de mayo de 2026

---

## Estado actual

| Archivo | Estado |
|---------|--------|
| `1__Diccionario_de_modelos_de_Design_System.md` | ✅ Completo |
| `2__Reglas_y_anti-patrones_para_el_analizador.md` | ✅ Completo |
| `3__Cómo_piensa_la_calculadora_solo_leyendo_código.md` | ✅ Completo |
| `4__Taxonomia_Umbrales_y_Transiciones.md` | ✅ Completo |
| `DS-Real-Cases.md` | ✅ Completo |
| `Design_Systems_Modernos___Clasificaciones_y_Análisis_Comparativo.md` | ✅ Completo |
| `SKILL.md` | ✅ Operativo — requiere actualizaciones tras completar docs 9, 10, 11 |
| `scanner.py` | ✅ Funcional |
| `7__Arquitectura_de_Componentes.md` | ❌ No existe — material disponible en research |
| `9__Discovery_Questions.md` | ❌ No existe |
| `10__Scoring_Formula.md` | ❌ No existe |
| `11__Report_Template.md` | ❌ No existe |

---

## Gaps pendientes

### Doc 7 — Análisis de arquitectura de componentes

**Problema:** El SKILL.md detecta anti-patrones de tokens pero el análisis de estructura de componentes no está integrado como fase propia. El material existe en el research (compass_artifact) pero no está destilado.

**Qué incluir:**
- Métricas accionables: LOC por componente, complejidad ciclomática, reuse rate
- 5 anti-patrones detectables: God Component, prop drilling, duplicación, over-abstraction, tight coupling
- Patrones modernos de referencia: Atomic Design, Compound Components, Headless Components
- Herramientas de detección: jscpd, dependency-cruiser, Omlet.dev

**Impacto en SKILL.md:** Añadir Fase 1b de análisis de componentes entre el escaneo y la clasificación de tokens.

**Esfuerzo estimado:** 1 sesión. El material ya existe.

---

### Doc 9 — Discovery questions

**Problema:** Las 5 preguntas actuales de la Fase 0 son insuficientes para una auditoría profesional. Falta contexto crítico sobre deuda técnica, ownership, pipeline Figma→código, historial de rebrands y roadmap.

**Qué incluir:**
- Banco de preguntas agrupadas por dimensión:
  - Equipo (roles, ownership, governance)
  - Producto (número de apps, plataformas, usuarios)
  - Técnica (stack, deuda existente, pipeline Figma→código)
  - Negocio (roadmap, rebrand en horizonte, presupuesto para DS)
- Guía de cuáles hacer según fase de empresa (Pre-seed vs Serie B vs Enterprise)
- Preguntas mínimas obligatorias (las que siempre se hacen)
- Preguntas opcionales según contexto

**Impacto en SKILL.md:** Reemplazar las 5 preguntas fijas de la Fase 0 por referencia al banco de preguntas con lógica de selección por fase.

**Esfuerzo estimado:** 1 sesión.

---

### Doc 10 — Scoring formula

**Problema:** La fórmula actual es funcional pero incompleta. No contempla el eje de arquitectura de componentes, no tiene penalizaciones por fase (score 60 en Seed está bien, score 60 en Serie B es una alerta), y no produce un número legible para un CTO sin contexto técnico.

**Qué incluir:**
- Fórmula extendida con 3 ejes: tokens + componentes + arquitectura
- Pesos por eje (requiere decisión)
- Tabla de interpretación contextualizada por fase de empresa
- Lógica de penalizaciones por anti-patrones críticos
- Formato de score legible para no-técnicos (semáforo, tier, label)

**Decisiones pendientes antes de escribir:**
- ¿Qué peso tiene el eje de componentes vs tokens? (propuesta: tokens 50%, componentes 30%, arquitectura 20%)
- ¿El score es único o son 3 sub-scores independientes?

**Impacto en SKILL.md:** Reemplazar Fase 5 completa.

**Esfuerzo estimado:** 1 sesión con decisiones previas resueltas.

---

### Doc 11 — Report template

**Problema:** El template actual en la Fase 6 del SKILL.md es un esqueleto funcional pero no está al nivel de entregable profesional. No tiene executive summary para no-técnicos, ni estimación de esfuerzo de migración, ni sección de "qué no tocar", ni estructura para fechar y firmar.

**Qué incluir:**
- Executive summary de 3 líneas (para CEO/CTO no técnico)
- Score visual con interpretación contextualizada por fase
- Diagnóstico técnico (modelo detectado, comparación con referencia)
- Anti-patrones críticos con impacto de negocio traducido
- Sección "qué no tocar ahora" (para evitar sobre-ingeniería)
- Plan de cambios con estimación de esfuerzo (semanas/meses)
- Estimación de ROI esperado con benchmarks citados
- Métricas de negocio a medir post-implementación
- Firma, fecha, versión del auditor

**Impacto en SKILL.md:** Reemplazar Fase 6 completa.

**Esfuerzo estimado:** 1 sesión — con scoring y discovery resueltos, el template se escribe solo.

---

## Orden de ejecución recomendado

| Prioridad | Doc | Razón |
|-----------|-----|-------|
| 1 | **Doc 10** — Scoring formula | Define la columna vertebral del reporte. Sin el score correcto, el template no tiene sentido |
| 2 | **Doc 9** — Discovery questions | Mejora la Fase 0, que es lo primero que toca cualquier usuario nuevo |
| 3 | **Doc 11** — Report template | Con scoring y discovery resueltos, el template se construye sobre base sólida |
| 4 | **Doc 7** — Arquitectura de componentes | Extensión del análisis, no bloqueante de los demás |

---

## Actualizaciones necesarias en SKILL.md al finalizar

| Sección | Cambio |
|---------|--------|
| Fase 0 | Reemplazar 5 preguntas fijas → lógica de selección del banco (Doc 9) |
| Fase 1 | Añadir Fase 1b de análisis de componentes (Doc 7) |
| Fase 5 | Reemplazar fórmula actual → fórmula extendida de 3 ejes (Doc 10) |
| Fase 6 | Reemplazar template esqueleto → template profesional completo (Doc 11) |

---

## Nivel de calidad actual vs objetivo

| Dimensión | Ahora | Objetivo |
|-----------|-------|---------|
| Análisis de tokens | ✅ Completo y preciso | — |
| Análisis de componentes | 🟡 Básico (solo anti-patrones) | Framework de 3 niveles con métricas |
| Discovery | 🟡 5 preguntas genéricas | Banco por dimensión + lógica por fase |
| Scoring | 🟡 Fórmula simple de 5 métricas | Fórmula de 3 ejes contextualizada por fase |
| Reporte | 🟡 Esqueleto funcional | Entregable profesional directo al cliente |
| **Entregable global** | **Consultor junior bien entrenado** | **Entregable de agencia sin edición manual** |
