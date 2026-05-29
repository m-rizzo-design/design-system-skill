# 9. Discovery Questions

Banco de preguntas de contexto para reemplazar la Fase 0 genérica del auditor. Estructura: 4 dimensiones, preguntas obligatorias + opcionales por fase.

Use estos criterios de selección: **Equipo** está siempre presente. **Producto** es obligatorio. **Técnica** se ajusta por fase. **Negocio** es obligatorio si hay presupuesto DS o migraciones planeadas.

---

## Preguntas obligatorias (siempre se hacen)

Estas 4 preguntas establece el baseline y permiten elegir el perfil de referencia correcto.

### EQUIPO — Contexto organizacional mínimo

1. **¿Cuántos diseñadores y cuántos frontend/full-stack engineers trabajan en esto?**
   - Rango típico de equipo por fase: Pre-seed (1–2 diseño, <10 devs) → Seed (2–5 diseño, 10–30 devs) → Serie A (5–10 diseño, 30–100 devs) → Serie B+ (10+ diseño, 100+ devs)
   - Si hay <3 diseñadores o <15 devs: formalizaciones mínimas; prioridad es momentum.

2. **¿En qué fase está la empresa?** (Pre-seed / Seed / Serie A / Serie B / Growth / Enterprise)
   - Esto define tolerancia al riesgo, velocidad esperada, y modelo de referencia.

### PRODUCTO — Superficie a cubrir

3. **¿Cuántos productos o aplicaciones distintas usan (o necesitan usar) este sistema?**
   - 1 producto = sin presión de consistencia global. Múltiples = punto de dolor.
   - Si >3 productos: preguntar si tienen un producto principal y qué tan divergente es cada uno (diseño 80% compartido vs 40% compartido).

4. **¿Plataformas?** (solo web / web + mobile / web + mobile + otras)
   - Determina si la arquitectura debe soportar multiplatform infra.
   - Si incluye mobile, preguntar: ¿cuántas plataformas? ¿nativo (iOS/Android) o cross-platform (React Native, Flutter)?

---

## Preguntas por dimensión (seleccionar según fase)

### EQUIPO

#### Obligatorias en todas las fases

5. **¿Quién es dueño del design system?** (nombre, rol, quién lo reporta)
   - Sin owner explícito = no hay gobernanza. Señal de alerta.

6. **¿Hay un proceso formal para diseño→código?** (Figma? Specs? Handoff manual?)
   - Si no existe: hay deuda de documentación y riesgo de divergencia.

#### Si Seed o superior (equipos creciendo)

7. **¿Cómo se hace code review para cambios visuales/tokens?**
   - ¿Quién aprueba cambios? ¿Hay reglas documentadas?
   - Sin proceso = riesgo de fracturas de arquitectura.

8. **¿Hay separación clara entre diseño system team y product teams?**
   - Si no: quién establece estándares y quién los usa.

#### Si Serie A+ (multi-equipo)

9. **¿Hay gobernanza de tokens?** (¿quién puede crear tokens nuevos? ¿hay registro central?)
   - Sin gobernanza → "shadow tokens" y fragmentación garantizada.

10. **¿Cómo se toman decisiones sobre cambios a los tokens principales?**
    - ¿Es un bottleneck? ¿Cuántas semanas tarda agregar un token?
    - Si > 2 semanas: indicador de que la gobernanza es reactiva.

#### Si Enterprise o platform multi-equipo

11. **¿Hay diferentes equipos usando diferentes design systems?**
    - Si SÍ → cuáles y por qué. Oportunidad de unificación.

---

### PRODUCTO

#### Obligatorias en todas las fases

12. **¿Cuál es el estado actual del design system?** (no existe / muy básico / en transición / maduro)
    - Auto-evaluación del estado. Comparar con hallazgos del análisis de código.

13. **¿Está en roadmap un rebrand o cambio visual importante?**
    - SÍ → el DS debe estar listo para eso. Timing crítico.
    - NO → puede esperar formalizaciones no-críticas.

14. **¿Hay una única marca visual o múltiples?** (ej: productos sub-branded, white-label, marketplace)
    - Si múltiples: necesita semantic tokens y contexto de brand por producto.

#### Si Serie A+ o >2 productos

15. **¿Qué porcentaje de UI ya está unificada en el DS actual?**
    - <30% = sin tracción. >70% = buena adopción.
    - Útil para estimar esfuerzo de "llevar todo al DS".

16. **¿Hay APIs internas o un monorepo?**
    - Sí = arquitectura centralizada posible.
    - No (micro-frontends) = más complejo, necesita coordinación.

#### Si hay historial de rebrands o theming

17. **¿Cuántas veces se ha hecho rebrand total?** ¿En cuánto tiempo?
    - Indicador de si el DS aceleró o no el proceso.
    - "Antes sin DS tomaba 4 meses, ahora con semánticos toma 2 semanas" = prueba del ROI.

---

### TÉCNICA

#### Obligatorias en todas las fases

18. **¿Qué estrategia usan ahora?** (valores literales / primitivos / semánticos / otro)
    - Si no lo saben = hay inconsistencia. Probable que sea "no existe".
    - Comparar con lo que detecta el analizador.

19. **¿Stack principal?** (React / Vue / Angular / Svelte / Web Components / otros)
    - Determina herramientas y syntax.

20. **¿CSS o CSS-in-JS?** (vanilla CSS / SCSS / CSS Modules / Tailwind / styled-components / Panda / otro)
    - Influye en cómo se almacenan y distribuyen los tokens.

#### Si Seed+

21. **¿Tienen deuda técnica documentada en el DS?**
    - Sí = cuál es (qué tokens, qué componentes, qué arquitectura).
    - No = probable que sientan pain pero no lo hayan mapeado.

22. **¿Hay herramientas de análisis automático en CI/CD?**
    - Tests de accesibilidad, linting, análisis de duplicación.
    - Sin ellas = regresos visuales no detectados.

#### Si Serie A+

23. **¿Cómo se versionan los componentes y tokens?**
    - ¿Semantic versioning? ¿Release notes?
    - Sin versioning = cambios no-documentados rompen product teams.

24. **¿Hay documentación de componentes (Storybook, etc.)?**
    - Sí = nivel de madurez. Actualizado = disciplina.
    - No = onboarding lento.

25. **¿Existe un build pipeline para multi-plataforma?** (web, mobile, TV, etc.)
    - Si hay múltiples plataformas: ¿cómo sincroniza tokens?
    - ¿Es manual o automatizado?

#### Si hay custom variables o CSS-in-JS

26. **¿Los tokens se generan de una única fuente o son mantenidos en múltiples sitios?**
    - Una fuente = buena; múltiples = duplicación garantizada.

#### Si migración planeada (ej: Tailwind → tokens semánticos)

27. **¿Hay un plan de migración existente?**
    - Si no = necesita especificar pasos y esfuerzo.

---

### NEGOCIO

#### Obligatorias si hay presupuesto DS o iniciativa planeada

28. **¿Hay presupuesto reservado para mejorar el DS?**
    - No = ajustar recomendaciones a "0 inversión nueva" (refactor incremental).
    - Sí → cuánto (personas-mes, dinero).
    - Indica si las mejoras son "cuando sobre tiempo" o "proyecto dedicado".

29. **¿Cuál es el roadmap de productos en los próximos 6 meses?**
    - Lanzamientos nuevos, plataformas nuevas, integraciones.
    - Tiempos críticos donde el DS debe estar listo.

#### Si hay problemas visibles de inconsistencia

30. **¿Cuánto tiempo pierde el equipo por inconsistencias visuales?**
    - "Cada rebrand, un componente se ve diferente en cada página."
    - "Los colores no coinciden entre web y mobile."
    - Cuantificar (es 5 bugs por semana, es 2 semanas de cada rebrand, es 30% del QA).

#### Si hay múltiples equipos o plataformas

31. **¿Cuáles son los mayores friction points ahora?**
    - Onboarding diseñadores: ¿cuánto tarda?
    - Onboarding developers: ¿cuánto tarda?
    - Cambios globales: ¿cuánto toman?
    - Identificar el "win más obviamente rápido".

---

## Guía de selección por fase

### Pre-seed (MVP, <10 personas)
**Preguntas mínimas para hacer:**
- Obligatorias: 1–4, 5, 12, 18–20
- Omitir todo lo que pida "gobernanza" o "multi-equipo"
- Foco: ¿qué stack usan? ¿hay al menos un primitivo o están todo valores literales?

**Modelo de referencia:** GitHub 2011–2015 (inicio sin DS formal, CSS sin abstracción)

---

### Seed (Product-market fit, 10–50 personas)
**Preguntas mínimas para hacer:**
- Obligatorias: 1–4, 5, 12–14, 18–22
- Agregar: 7 (code review), 21 (deuda técnica)
- Omitir: gobernanza, versionado, multiplatform avanzado

**Modelo de referencia:** Atlassian 2012 (5 personas, consistencia local, primitivos incipientes)

---

### Serie A (Growth, 50–200 personas, 2–5 productos)
**Preguntas mínimas para hacer:**
- Obligatorias: 1–4, 5, 12–24, 28–30
- Focus: ¿hay fragmentación de tokens entre productos? ¿ownership claro?
- Si hay mobile: preguntar sincronización multiplatform

**Modelo de referencia:** Shopify pre-2017 (inconsistencia detectada, primer rebrand impulsó formalización)

---

### Serie B / Growth (200–1000 personas, 3+ productos, ecosistema)
**Preguntas mínimas para hacer:**
- Todas excepto las Enterprise-only (9, 11)
- Agregar: migración planeada, ROI esperado, comparación con competencia

**Modelo de referencia:** Shopify 2017+ (Polaris, multiplatform, open source)

---

### Enterprise (1000+ personas, plataforma + partners, global)
**Preguntas mínimas para hacer:**
- Todas
- Agregar: gobernanza multi-región, soporte a partners externos, diferencias culturales en diseño

**Modelo de referencia:** IBM Carbon, Microsoft Fluent (escala global, múltiples equipos autónomos, necesidad de estándares)

---

## Señales de alerta que cambian el enfoque

### Rojo — Bloquea la auditoría

1. **"No existe design system"** + equipo >20 personas + >2 productos
   - Recomendación: no auditar tokens. Primero mapear qué existe (CSS, inline styles, clases utilitarias) y proponer arquitectura base.

2. **"No hay código fuente accesible"** (IP lock, cliente no puede compartir)
   - No se puede hacer análisis detallado. Ofrecer versión "self-service" de checklist.

3. **"Los diseños y código nunca estuvieron sincronizados"**
   - Audit histórico: ¿qué pasó? ¿siempre fue así o se desacoplaron?
   - Impacta recomendaciones: puede que necesite Figma→código workflow como Fase 0 antes de formalizaciones.

### Amarillo — Cambia el enfoque

4. **"Intentamos migrar a [modelo] hace X meses y fue un desastre"**
   - Indagar: ¿por qué falló? ¿fue arquitectura o adopción?
   - Enfocar en lo que aprendieron y cómo evitar repetir.

5. **"Tenemos personas de múltiples países con gustos de diseño muy distintos"**
   - No es problema de tokens, es problema de gobernanza y estándares visuales.
   - Agregar pregunta: ¿hay design direction documento? ¿o cada región decide?

6. **"Migración a [plataforma] planeada en próximos 3 meses"**
   - Timing crítico. El DS debe estar frozen o muy estable en esa ventana.
   - Ajustar plan de cambios: "post-migración" en lugar de "ahora".

7. **"Acabamos de contratar nuevo Head of Design/CTO"**
   - Nueva visión de prioridades. Preguntar: ¿qué cambios plantea?
   - Puede que la "deuda técnica que reporta el audit" no sea lo que quieren atacar primero.

8. **"No hay comunicación Design↔Eng"** (silos)
   - El problema no es técnico, es organizacional.
   - Recomendación: establecer canal y ritmo antes de formalizar tokens.

9. **Producto financiero, salud, o regulado**
   - DS no es discrecional; es requerimiento legal.
   - Cambios urgentes son accesibilidad (WCAG, HIPAA, PSD2).
   - Enfocar audit en cobertura de estándares, no velocidad.

10. **"Queremos hacer un white-label"**
    - Arquitectura cambia completamente. Tokens semánticos son obligatorios.
    - Agregar pregunta: ¿cuántos white-labels? ¿cuánta variación visual permiten?

---

## Cómo usar este documento desde la Skill

**En Fase 0 del auditor:**

1. Hacer preguntas obligatorias (1–4 siempre; 5, 12, 18–20 siempre).
2. Identificar fase de empresa (Pre-seed / Seed / Serie A / B / Enterprise).
3. Hacer preguntas de esa fase.
4. Revisar "Señales de alerta": si alguna aplica, ajustar enfoque.
5. Proceder a Fase 1 (escaneo) con contexto completo.

**Salida esperada de Fase 0:**
- Contexto demográfico (equipo, fase, productos, plataformas)
- Modelo de referencia elegido (de SKILL.md sección Benchmarks)
- Señales de alerta identificadas
- Plan de esfuerzo estimado (ver **Orden de ejecución recomendado** en README.md)

Nunca saltarse la Fase 0. La calidad del diagnóstico depende de usar el modelo de referencia correcto.
