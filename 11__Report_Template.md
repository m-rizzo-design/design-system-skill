# Design System Audit Report

**Auditado:** [CLIENT_NAME]  
**Fecha:** [DATE]  
**Versión del auditor:** Fase 6 — Design System Auditor v1.0  
**Auditor:** [AUDITOR_NAME / ORGANIZATION]

---

## RESUMEN EJECUTIVO

Para CTOs, CEOs, Product Leaders — sin jerga técnica.

[EXECUTIVE_SUMMARY_LINE_1: Estado actual en una frase. Ej: "Tu Design System tiene fundamentos sólidos pero está fragmentado entre productos."]

[EXECUTIVE_SUMMARY_LINE_2: Principal oportunidad de mejora. Ej: "Unificar los tokens semánticos ganaría consistencia visual y reduciría deuda técnica en QA."]

[EXECUTIVE_SUMMARY_LINE_3: Esfuerzo y plazo. Ej: "Es factible en 8–12 semanas con 1–2 personas dedicadas, post-Fase B si es necesario."]

---

## 1. SCORE DE SALUD

### Score Global: [SCORE]/100 [EMOJI]

**Interpretación contextualizada:**
- Fase detectada: [COMPANY_PHASE] (Pre-seed / Seed / Serie A / Serie B / Enterprise)
- Juicio: [CONTEXTUAL_JUDGMENT — ver tabla 10.7 del Scoring Formula]
- Acción esperada: [ACTION — "Monitorear" / "Plan de mejora" / "Inversión urgente" / etc.]

### Sub-scores por eje:

| Eje | Score | Estado | Impacto |
|-----|-------|--------|---------|
| **Tokens** | [TOKEN_SCORE]/100 | [⭐/🟡/🔴] | [Breve explicación del impacto en desarrollo y consistencia] |
| **Componentes** | [COMPONENT_SCORE]/100 | [⭐/🟡/🔴] | [Breve explicación del impacto en velocidad de UI] |
| **Arquitectura** | [ARCH_SCORE]/100 | [⭐/🟡/🔴] | [Breve explicación del impacto en escalabilidad] |

**Prioridad de ataque:** 
1. [EJE_MÁS_DÉBIL] → [estimación baja/media/alta de esfuerzo]
2. [EJE_SEGUNDO] → [estimación]
3. [EJE_TERCERO] → [estimación]

---

## 2. DIAGNÓSTICO TÉCNICO

### Modelo Detectado

**Estrategia de Tokens:** [Sin tokens / Primitivos / Semánticos / Híbrido]  
**Evidencia:** [Cita específica del código: % de valores literales, fuentes de tokens, nombres encontrados, ejemplo de token real]

**Modelo de Arquitectura:** [Centralized / Co-located / Multiplatform / Híbrido inestable]  
**Evidencia:** [Estructura de carpetas encontrada, ubicación de tokens, dispersión de definiciones]

### Comparación con Empresa de Referencia

Tu sistema se parece más a: **[REFERENCIA_1]** porque [RAZÓN_TÉCNICA].

Ejemplo real:
- [REFERENCIA_1]: [Descripción de estado/estructura similar]
- Tu sistema: [Tu estado/estructura específico]

Difiere en: [DIFERENCIAS_CLAVE]
- Diferencia 1: [Tu enfoque] vs [Referencia: enfoque]. Impacto: [consecuencia técnica]
- Diferencia 2: [...]

Modelo alternativo considerado pero no adecuado: [REFERENCIA_2] porque [RAZÓN_RECHAZO].

---

## 3. MODELO OBJETIVO

> Referencia: `5__Modelo_Objetivo_y_Decision.md`
> Generado en Fase 3b. Responde: "¿dónde debería estar este sistema, dado su contexto?"

### Modelo actual → Modelo objetivo

| Dimensión | Modelo actual | Modelo objetivo |
|-----------|--------------|-----------------|
| Tokens | [CURRENT_TOKEN_MODEL] | [TARGET_TOKEN_MODEL] |
| Arquitectura | [CURRENT_ARCH_MODEL] | [TARGET_ARCH_MODEL] |

### Por qué este objetivo y no uno más ambicioso

**[RAZÓN_1 — señal de contexto, ej: "1 marca, sin rebrand en roadmap"]**
[Explicación de por qué esa señal determina el modelo objetivo. Sin generalidades — anclado en el contexto real del usuario.]
→ [Conclusión específica]

**[RAZÓN_2 — señal de contexto]**
[Explicación]
→ [Conclusión]

**[RAZÓN_3 — señal de contexto]**
[Explicación]
→ [Conclusión]

### Lo que NO necesitás todavía

#### [ITEM_1 — nombre de la técnica o herramienta]
**Por qué no ahora:** [razón concreta en el contexto del usuario]
**Cuándo reconsiderar:** [condición concreta — ej: "cuando dark mode esté en roadmap"]

#### [ITEM_2]
[Misma estructura]

#### [ITEM_3]
[Misma estructura]

### Qué ganás al llegar al modelo objetivo

- [Beneficio 1 — en lenguaje concreto, no técnico]
- [Beneficio 2]
- [Beneficio 3]
- [Beneficio 4]

### Cuándo evolucionar más allá

| Trigger | Qué activa |
|---------|-----------|
| [Condición concreta 1] | [Qué modelo/herramienta activa] |
| [Condición concreta 2] | [Qué activa] |
| [Condición concreta 3] | [Qué activa] |
| [Condición concreta 4] | [Qué activa] |

---

## 5. ANTI-PATRONES CRÍTICOS DETECTADOS

### Impacto traducido a negocio (no solo técnico)

#### 🔴 [ANTI-PATRÓN_1 — Código de severidad AP-XX]
**Qué es:** [Descripción técnica — qué lo causa]

**Dónde aparece:** [N instancias encontradas — rutas específicas]

**Síntoma visible:**
- [Síntoma 1 — qué ven los usuarios/equipos en desarrollo]
- [Síntoma 2]

**Impacto de negocio:**
- **Velocidad de desarrollo:** [−X% en cambios visuales / +X semanas por migración visual / +X bugs por rebrand]
- **Costo de QA:** [−X% en coverage / +X horas por ciclo de testing]
- **Deuda técnica:** [Estimación en person-months — cuánto tiempo para limpiar]
- **Riesgo:** [Si no se arregla: X pasará en Y meses]

**Esfuerzo para arreglar:** [X semanas con Y personas]

---

#### 🟡 [ANTI-PATRÓN_2 — AP-XX]
[Misma estructura]

---

#### 🟢 [ANTI-PATRÓN_3 — AP-XX] (Baja severidad, recomendado pero no urgente)
[Misma estructura]

---

## 6. QUÉ NO TOCAR AHORA (Evitar sobre-ingeniería)

**Lista explícita de cambios que suenan bien pero harían más mal que bien en tu contexto:**

### Cambio 1: [PROPUESTA_TENTADORA]
**Sonaría bien porque:** [Razón aparente]

**Pero NO debe hacerse ahora porque:**
- Tu equipo tiene [X limitaciones que hacen esto riesgoso]
- El ROI no es positivo hasta [CONDICIÓN — ej: "hasta tener >3 productos"]
- Hay [X cambios prioritarios] que deberían hacerse primero
- Costo estimado: [X semanas] de esfuerzo que mejor van a [PRIORIDAD_MAYOR]

**Cuándo reconsiderar:** [En qué punto (ej: después de 2 rebrand, cuando escales a 50 devs, etc.)]

### Cambio 2: [...]

---

## 7. PLAN DE CAMBIOS CON ESTIMACIÓN DE ESFUERZO

### Contexto del plan
- Equipo disponible: [X diseñadores, Y frontend engineers, Z product]
- Presupuesto: [Sí / No / Parcial]
- Timeline: [Inmediato / Post-[FASE CRÍTICA] / Q3 2026 / Otro]
- Restricciones: [Cambios en roadmap, no parar product, etc.]

### Fases del plan

#### **FASE 1: [NOMBRE] — [X semanas / Y meses]**
**Objetivo:** [Qué se logra al final — entregable concreto]

**Tareas:**
1. [Tarea 1] — [Estimated effort: 1-2 weeks, Owner: Designer/Dev]
2. [Tarea 2] — [Estimated effort: 2-3 weeks, Owner]
3. [...]

**Entregables:**
- [Entregable 1 — documento, código, componente]
- [Entregable 2]

**Riesgo:** [Qué puede salir mal — cómo mitigarlo]

**¿Puede hacerse en paralelo con product?** [Sí / No / Parcialmente]

---

#### **FASE 2: [NOMBRE] — [X semanas / Y meses]**
[Misma estructura]

---

#### **FASE 3: [NOMBRE] — [X semanas / Y meses]**
[Misma estructura]

---

### Cronograma visual

```
Ahora         [PHASE1_START]         [PHASE2_START]         [DONE]
  |═════════════════════════════════════════════════════════════════|
  |
  └─ [PARALLEL WORK — si aplica]
```

### Esfuerzo total
- **Person-months:** [X PM totales]
- **Dedicación recomendada:** [Full-time / X% FTE / 1 day/week + product]
- **Duración calendario:** [X meses si es en paralelo, Y meses si es serial]

**Precedencia importante:**
- [FASE_1] DEBE terminar antes de [FASE_2] porque [RAZÓN — ej: "porque FASE_2 depende del output de FASE_1"]

---

## 8. ESTIMACIÓN DE ROI ESPERADO

### Supuestos del cálculo

- Equipo actual: [X diseñadores, Y frontends, Z QA]
- Número de productos: [N]
- Número de cambios visuales/año: [M]
- Costo promedio por persona-hora: [€/$ — o usar costo regional si aplica]

### Ahorro esperado (metodología estándar)

**Reducción de tiempo en diseño:**
- Antes: [X horas por cambio visual / rebrand / nueva feature]
- Después: [Y horas]
- Ahorro: [X-Y] horas/cambio × [M cambios/año] = [TOTAL horas/año]
- **Ahorro anual:** [TOTAL × cost/hora] = €[X]

Citado en: [Empresa de referencia — ej: "Shopify reportó 20% en cambios visuales post-Polaris"]

**Reducción de tiempo en desarrollo + QA:**
- Antes: [X horas de desarrollo + testing por feature]
- Después: [Y horas — componentes reutilizables, menos regresiones]
- Ahorro: [X-Y] horas/feature × [Z features/año] = [TOTAL horas/año]
- **Ahorro anual:** [TOTAL × cost/hora] = €[X]

Citado en: [DS-Real-Cases.md — empresa similar, % de mejora]

**Valor de lanzar antes (time-to-market):**
- Reducción media: [X semanas por ciclo / X%]
- Valor por semana: [€X — ej: revenue por semana, competitividad, etc.]
- **Beneficio anual:** €[X] × [número de ciclos]

Citado en: [Caso real — ej: "Empresa B2B SaaS ahorró 22–35% en TTM"]

**Reducción en bugs y soporte:**
- Inconsistencias visuales detectadas en QA: [X bugs/month]
- Reducción esperada: [Y%]
- Costo promedio bug UI: €[Z]
- **Ahorro anual:** [X × (Y/100) × 12 × Z] = €[X]

### Costo de implementación

- Recursos internos: [X PM × €[cost/PM]] = €[X]
- Herramientas externas (si aplica): €[X]
- **Costo total:** €[X]

### ROI Neto

```
ROI = (Ahorro anual − Costo implementación) / Costo implementación × 100%

Ahorro total proyectado (anual): €[TOTAL_AHORRO]
Costo de implementación: €[COST]
─────────────────────────────────────────
PAYBACK PERIOD: [X.X meses]
ROI (Año 1): [X%]
ROI (Año 2+): [Y%] (sin costo de implementación)
```

**Break-even:** Se recupera la inversión en [X meses], asumiendo [SUPUESTO_CRÍTICO].

### Benchmarks citados

| Empresa | Métrica | Valor | Fuente |
|---------|---------|-------|--------|
| [Ref_1] | Mejora en eficiencia diseño/dev | +20–46% | DS-Real-Cases.md, Caso 1 |
| [Ref_2] | Reducción TTM | −22–35% | DS-Real-Cases.md, Caso 2 |
| [Ref_3] | Ahorro por reutilización | €190K/proyecto | DS-Real-Cases.md, Caso 1 |
| [Ref_4] | Payback period típico | 12–24 meses | DS-Real-Cases.md, Síntesis |

---

## 9. MÉTRICAS DE NEGOCIO A MEDIR POST-IMPLEMENTACIÓN

### Métricas de desarrollo

| Métrica | Línea base (antes) | Target (6 meses) | Cómo medir |
|---------|-------------------|------------------|-----------|
| Tiempo promedio para cambio visual | [X horas] | [Y horas] | Ticket a merged en Git |
| % de componentes reutilizados | [X%] | [Y%] | Auditoría de código cada trimestre |
| Bugs visuales por ciclo | [X] | [Y] | Tickets de QA etiquetados "visual" |
| Onboarding de frontend novo | [X días] | [Y días] | Tiempo hasta first PR merged |
| Consistencia visual (tests autom.) | [X%] | [Y%] | Visual regression tests |

### Métricas de negocio

| Métrica | Línea base | Target | Responsable |
|---------|-----------|--------|-------------|
| Time-to-market de features | [X semanas] | [Y semanas] | Product Manager |
| Número de incidentes UI en producción | [X/mes] | [Y/mes] | QA Lead |
| Customer support tickets por "design inconsistency" | [X/mes] | [Y/mes] | CS Manager |
| Satisfacción interna (NPS del DS entre equipos) | [X] | [Y] | Encuesta semestral |

### Cómo instrumentar

1. **Baseline (antes de cambios):**
   - Audit de tiempo en cambios actuales (muestreo de últimas 10 PRs)
   - Count de bugs visuales en últimos 3 meses de tickets cerrados
   - Self-evaluation de equipos: "¿Cuánto tiempo pierdes por inconsistencias?"

2. **Tracking durante la implementación:**
   - Dashboard en [TOOL] con métricas actuales
   - Checkin mensual en [MEETING/FORMAT]

3. **Evaluación post-6 meses:**
   - Mismos métodos que baseline
   - Comparación month-over-month
   - Documentar lecciones aprendidas

---

## 10. PRÓXIMOS PASOS RECOMENDADOS

### Inmediato (esta semana)

1. **Validar este diagnóstico** con [EQUIPO TÉCNICO]
   - ¿Los anti-patrones detectados coinciden con lo que sienten en el día a día?
   - ¿El modelo clasificado refleja lo que quieren lograr?

2. **Decidir scope de FASE 1**
   - ¿Van a atacar [PRIORIDAD_1] primero o hay otros bloqueantes?
   - ¿Quién será dueño del proyecto — DS team, arquitecto, Product?

3. **Reservar recursos**
   - Confirmar que hay [X personas] dedicadas
   - O ajustar el plan si el presupuesto es distinto

### Semana 1–2

1. **Kick-off de FASE 1** con [OWNER + STAKEHOLDERS]
   - Alineación en objetivos, timeline, entregables
   - Asignación clara de ownership

2. **Setup del tracking de métricas**
   - Instrumento baseline (por ej: Git query, Figma audit)
   - Dashboard inicial

### Semana 3+

Comienza FASE 1 del plan.

---

## 11. NOTAS Y LIMITACIONES

### Scope del audit

Este audit cubre:
- ✅ Tokens y estrategia de abstracción
- ✅ Arquitectura de tokens (centralización, fragmentación)
- ✅ Anti-patrones en definición y uso
- ✅ Score de salud ponderado

Este audit **NO cubre:**
- ❌ Componentes React/Vue/etc (arquitectura de componentes — doc 7)
- ❌ Herramientas de tooling (Webpack, Figma plugins, CLI)
- ❌ Accesibilidad (WCAG — separate audit recomendado)
- ❌ Performance de CSS
- ❌ Procesos de gobernanza detallados (excepto detección de síntomas)

### Datos utilizados

**Fuentes de datos:**
- Código fuente del repo: [RUTA_O_FECHA_DEL_SCAN]
- Discovery questions (Fase 0): [RESPUESTAS_RESUMIDAS]
- Scoring formula (Fase 5): Documento 10__Scoring_Formula.md

**Supuestos hechos:**
- [SUPUESTO_1 — ej: "Se asume que la rama main refleja el estado de producción"]
- [SUPUESTO_2]

**Datos que faltaron** (si aplica):
- [DATO_1 — y cómo afecta confiabilidad]

### Confiabilidad del diagnóstico

**Confianza media-alta** en:
- Modelo de tokens detectado (basado en análisis de código)
- Score de salud (fórmula estándar aplicada a métricas objetivas)
- Anti-patrones críticos (patrones detectables en código)

**Confianza media** en:
- Estimaciones de esfuerzo (dependen de factores organizacionales no capturados)
- ROI (basado en benchmarks, no datos históricos de la empresa)

**Factores que cambiarían el diagnóstico:**
- Cambio de contexto organizacional (nueva fase, nuevos productos)
- Refactor importante post-audit
- Cambio en tech stack o herramientas

---

## 12. FIRMA Y AUDITORÍA

**Auditor:** [AUDITOR_NAME]  
**Organización:** [ORG / Consultor independiente]  
**Email:** [EMAIL]  

**Fecha del audit:** [DATE]  
**Versión del proceso:** Design System Auditor v1.0 (Fase 6 — Report)  
**Próxima revisión recomendada:** [DATE + 6/12 MONTHS]

**Metodología:** Este reporte fue generado usando el Design System Auditor, un proceso estructurado de 6 fases:
1. Contexto (discovery questions)
2. Escaneo de código
3. Clasificación de tokens
4. Clasificación de arquitectura
5. Scoring ponderado de 3 ejes (tokens, componentes, arquitectura)
6. Reporte + plan de cambios

Documentación del proceso: `SKILL.md`, `10__Scoring_Formula.md`, `9__Discovery_Questions.md`, benchmarks en `DS-Real-Cases.md`.

---

## Apéndice A: Glosario de términos técnicos

| Término | Definición |
|---------|-----------|
| **Tokens** | Variables reutilizables que almacenan valores de diseño (colores, espaciado, tipografía) |
| **Primitive tokens** | Tokens que nombran valores sin contexto (ej: `blue-500`, `space-4`) |
| **Semantic tokens** | Tokens que nombran intención de uso (ej: `color-text-primary`, `spacing-content`) |
| **Component tokens** | Tokens específicos de un componente UI (ej: `button-bg-hover`) |
| **Centralizado** | Todos los tokens definidos en una ubicación única |
| **Co-located** | Tokens distribuidos junto con los componentes que los usan |
| **Multiplatform** | Arquitectura que soporta web, mobile, TV, etc. con fuente única de tokens |
| **Anti-patrón** | Práctica común que introduce problemas técnicos o de mantenimiento |

---

## Apéndice B: Referencias y fuentes

**Documentos del proyecto:**
- `1__Diccionario_de_modelos_de_Design_System.md` — definición formal de modelos
- `2__Reglas_y_anti-patrones_para_el_analizador.md` — cómo se detectan los problemas
- `10__Scoring_Formula.md` — fórmula de scoring detallada
- `DS-Real-Cases.md` — casos reales y ROI documentado

**Benchmarks citados en este reporte:**
- Shopify Polaris (caso studio, 2017+)
- Atlassian Design System (caso early-stage, 2012)
- PedidosYa (marketplace regional, 2024)
- IBM Carbon, Adobe Spectrum, Google Material (casos enterprise)

---

**END OF REPORT**
