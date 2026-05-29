# 5. Modelo Objetivo y Decisión

> La clasificación (Fase 3) responde: "¿dónde estás?"
> Esta fase responde: "¿dónde deberías estar, dado tu contexto específico?"
>
> Son preguntas distintas. El mismo score de 62/100 puede ser correcto para Pre-seed e inaceptable para Serie B. Pero más importante: el modelo al que debería apuntar un sistema Pre-seed es completamente distinto al de Serie B, incluso si tienen el mismo score hoy.

---

## 5.1 Dimensiones que determinan el modelo objetivo

Estas dimensiones vienen de las respuestas de Fase 0. Si no se obtuvieron todas, indicar qué se asumió.

| Dimensión | Opciones | Por qué importa |
|-----------|---------|-----------------|
| **Fase de empresa** | Pre-seed / Seed / Serie A / Serie B / Enterprise | Determina tolerancia a complejidad y deuda |
| **Número de marcas** | 1 / múltiples / white-label | Multiplica la necesidad de tokens primitivos y hybrid |
| **Número de productos** | 1 / 2–3 / 4+ | Multiplica presión en arquitectura y gobernanza |
| **Plataformas** | Solo web / web + mobile nativo / multiplatform | Determina si se necesita build pipeline cross-platform |
| **Equipo de diseño** | 1 / 2–5 / 5–10 / 10+ | Determina si se necesita gobernanza de tokens |
| **Rebrand en roadmap** | No / posible / confirmado | Activa necesidad de primitive tokens como capa explícita |
| **Dark mode en roadmap** | No / posible / confirmado | Activa necesidad de separación semantic/primitive |

---

## 5.2 Matriz: contexto → modelo objetivo de tokens

| Condiciones | Modelo objetivo | Por qué este y no el siguiente |
|------------|-----------------|-------------------------------|
| Pre-seed + 1 marca + sin rebrand ni dark mode en roadmap | **Semantic-first maduro** | Los tokens semánticos bien nombrados ya dan la flexibilidad necesaria. La capa de primitivos añade overhead sin beneficio cuando hay 1 marca y sin necesidad de reescalar la paleta. |
| Pre-seed + 1 marca + rebrand o dark mode confirmado | **Hybrid: primitive → semantic** | El rebrand o dark mode justifican aislar los valores crudos. Permite cambiar la escala de colores sin tocar los tokens de intención. |
| Seed + 1–2 marcas + <3 productos | **Semantic-first maduro** con component tokens opcionales en componentes complejos | El equipo crece; los component tokens reducen coordinación en componentes de alta frecuencia. Pero no vale la pena el 3er nivel completo si las marcas no divergen. |
| Seed/Serie A + múltiples marcas o white-label | **Hybrid completo: primitive → semantic → component** | White-label requiere que diferentes clientes tengan paletas sin tocar los semánticos. Esta es la razón original del 3er nivel. |
| Serie A+ + múltiples productos y equipos | **Hybrid completo** | Múltiples product teams necesitan componentes tokens para tematizar sin romper el contrato del DS. |
| Cualquier fase + iOS o Android nativo | **+ Multiplatform infra (Style Dictionary o Token Studio)** | CSS custom properties no compilan a Swift ni a XML. Se necesita una fuente agnóstica que genere outputs por plataforma. |

### Regla general

- **1 marca, 1 equipo, sin mobile nativo** → el techo correcto es Semantic-first maduro. No subir antes de tiempo.
- **Múltiples marcas o white-label** → Hybrid es obligatorio, no opcional.
- **Mobile nativo** → Multiplatform infra es obligatorio, independiente de todo lo demás.

---

## 5.3 Matriz: contexto → modelo objetivo de arquitectura

| Condiciones | Modelo objetivo | Por qué este y no otro |
|------------|-----------------|------------------------|
| 1–2 superficies + 1 equipo | **Centralized limpio** | Sin coordinación entre equipos, la centralización es más simple de auditar, mantener y onboardear. |
| 2–4 superficies + 1 equipo con autonomía por superficie | **Centralized core + component tokens co-located** | El core (primitives + semantic) centralizado. Solo los tokens de componente, próximos a sus componentes. |
| 3+ product teams con ownership de superficies distintas | **Hybrid: core centralized + domain co-located** | Cada equipo puede extender sin romper el contrato del core. El ownership queda explícito. |
| Web + mobile nativo | **Multiplatform** | Necesita build pipeline que genere CSS, Swift/SwiftUI, XML/Compose desde la misma fuente. |

---

## 5.4 "Lo que NO necesitás" — razonamiento por contexto

Esta sección es igual de importante que las anteriores. **El error más común es sobre-diseñar antes de que el contexto lo justifique.** Cada nivel de complejidad que se agrega sin necesidad es deuda de mantenimiento, no inversión.

### Pre-seed / 1 marca / 1 equipo / sin rebrand

**Primitive tokens (blue-500, gray-900) como capa explícita**
- Por qué no: Con 1 marca, nadie más necesita reusar esos primitivos en otra escala o combinación. La capa duplica los archivos a mantener sin añadir flexibilidad real. Los tokens semánticos pueden referenciar valores literales directamente sin perder coherencia.
- Cuándo reconsiderar: dark mode confirmado en roadmap, white-label, o Figma ↔ código sync automatizado que requiera token-level naming.

**Component tokens (--button-bg, --card-radius) como primera capa de tokens**
- Por qué no: Los component tokens existen para que equipos distintos puedan tematizar componentes sin romper el DS core. Con 1 equipo y CSS Modules, el aislamiento ya está dado por los archivos de componente. Añadir una capa de tokens solo mueve el "qué cambia" sin añadir más control.
- Cuándo reconsiderar: Primer contractor externo en UI que necesite theming de componentes, o >3 frontends con ownership separado.

**Style Dictionary o pipeline de tokens generado**
- Por qué no: Este tooling resuelve el problema de compilar tokens para múltiples plataformas (iOS, Android, web) desde una fuente única. Para web + Tauri/Electron, CSS custom properties en un solo archivo son más simples de debuggear, versionar y mantener.
- Cuándo reconsiderar: Mobile nativo (iOS/Android) en roadmap con fecha concreta.

**Storybook o documentación formal de componentes**
- Por qué no: Con 1 owner del DS, el costo de mantener Storybook sincronizado supera el beneficio. Útil cuando hay onboarding frecuente de devs o contractors.
- Cuándo reconsiderar: Tercer dev frontend, primer contractor externo en UI, o cuando el onboarding de un dev nuevo tarda >2 semanas por falta de documentación.

**Co-located tokens (tokens junto a cada componente)**
- Por qué no: Co-location resuelve un problema de coordinación entre equipos. Sin ese problema, es overhead sin beneficio: más archivos que mantener, más rutas de importación, más superficie para que los tokens se dupliquen entre componentes.
- Cuándo reconsiderar: Múltiples product teams con ownership de componentes distintos, o >50 componentes donde la gestión centralizada se vuelve un bottleneck.

---

### Seed / 2–5 diseñadores / 1 marca / 2–3 productos

**3 niveles completos de tokens si las marcas son iguales entre productos**
- Por qué no: Si los productos comparten la misma identidad visual, el nivel de component tokens solo añade fricción sin dar flexibilidad nueva.
- Cuándo reconsiderar: Cuando los productos tengan que verse distintos (sub-branding, white-label).

**Multiplatform infra si el mobile es web-based (PWA, WebView)**
- Por qué no: PWAs y WebViews consumen CSS directamente. Solo se necesita multiplatform cuando hay compilación a formatos nativos (Swift, XML, Compose).
- Cuándo reconsiderar: Mobile nativo con Swift/Kotlin explícitamente en roadmap.

---

## 5.5 Triggers para evolucionar al siguiente nivel

Un sistema NO debe evolucionar por ambición técnica. Solo debe hacerlo cuando un trigger concreto aparece.

### De Semantic-first maduro → Hybrid (primitive → semantic)

| Trigger | Qué activa |
|---------|-----------|
| Dark mode en roadmap (próximos 6 meses) | Crear capa de primitive tokens que sirvan de base para los semánticos. Los semánticos actuales se convierten en referencias a primitivos, no en valores literales. |
| Rebrand confirmado con nueva paleta | Los primitivos permiten cambiar la escala de colores (blue-100 a blue-900) sin tocar los tokens semánticos ni los componentes. |
| Figma ↔ código sync automatizado necesario | Token Studio y plugins similares trabajan mejor con las 3 capas explícitas. |
| White-label para clientes externos | Obligatorio. Los clientes necesitan poder inyectar su paleta sin romper los componentes. |

### De Hybrid → Hybrid + component tokens

| Trigger | Qué activa |
|---------|-----------|
| Segundo producto con identidad visual distinta | Component tokens permiten tematizar por producto sin duplicar componentes. |
| Primer contractor externo en UI | Les da una superficie de customización controlada sin acceso al core. |
| >3 frontends con ownership separado | Reduce la coordinación: cada equipo puede ajustar component tokens de los componentes que son suyos. |

### De Centralized → Centralized core + co-located component tokens

| Trigger | Qué activa |
|---------|-----------|
| Velocidad frenada por bottleneck en tokens centrales | Mover component tokens cerca de los componentes reduce dependencias del core. |
| Múltiples product teams con ownership de UI propio | Dar autonomía de component tokens por equipo, con review, sin tocar el core. |

### De Single platform → Multiplatform

| Trigger | Qué activa |
|---------|-----------|
| Mobile nativo (iOS, Android) confirmado | Style Dictionary o Token Studio para compilar tokens a Swift/XML/Compose desde CSS. |
| TV, reloj, o superficie no-web | Mismo pipeline pero con transformaciones adicionales. |

---

## 5.6 Qué se gana al llegar al modelo objetivo

Documentar esto en el reporte conecta el esfuerzo técnico con beneficios concretos que el usuario entiende.

**Semantic-first maduro + Centralized limpio:**
- Cambiar un color de marca = 1 línea en el archivo de tokens, se propaga a todas las superficies automáticamente.
- Dark mode posible con 1 media query que sobreescribe los tokens semánticos, sin tocar componentes.
- Nueva superficie o microsite = importa el CSS del DS y hereda el sistema sin copiar nada.
- Cualquier dev puede entender el sistema en <5 minutos: 1 archivo, tokens con nombre de intención.
- Auditoría y diff de tokens triviales: 1 lugar donde mirar.

**Hybrid (una vez que los triggers lo justifiquen):**
- Rebrand en minutos en lugar de días: cambiar la escala de primitivos actualiza todos los semánticos.
- Clientes externos o productos con identidad propia sin necesidad de forkear el DS.
- Theming de componentes sin acceso al core del sistema.

---

## 5.7 Cómo usar esta fase en la auditoría

Ejecutar después de Fase 3 (clasificación) y antes de Fase 4 (anti-patrones).

1. Leer las respuestas de Fase 0: fase, marcas, productos, plataformas, equipo, rebrand/dark mode en roadmap.
2. Aplicar las matrices 5.2 y 5.3 para determinar el modelo objetivo de tokens y arquitectura.
3. Construir el argumento en lenguaje del usuario: "dado que tenés X, Y y Z, el modelo correcto para vos es A, porque [razones]". No usar jerga técnica sin explicación.
4. Listar explícitamente lo que NO necesitan ahora, con la razón concreta en su contexto.
5. Listar los triggers para evolucionar: cuándo tiene sentido ir al siguiente nivel.
6. Verificar coherencia con el plan de cambios (Fase 6): ¿las tareas del plan llevan hacia el objetivo o están sobre-diseñando?

---

## 5.8 Output esperado de esta fase

Una sección del reporte que responde de forma directa y sin ambigüedades:

```
Modelo objetivo de tokens:      [nombre]
Modelo objetivo de arquitectura: [nombre]

Por qué este objetivo:
  - [Razón 1 — anclada en contexto real del usuario]
  - [Razón 2]
  - [Razón 3]

Lo que NO necesitás todavía:
  - [Item 1] — cuándo reconsiderar: [condición concreta]
  - [Item 2] — cuándo reconsiderar: [condición concreta]

Qué ganás al llegar:
  - [Beneficio 1 en lenguaje de negocio]
  - [Beneficio 2]

Cuándo ir más allá:
  - [Trigger 1] → [qué activa]
  - [Trigger 2] → [qué activa]
```

Este output alimenta la sección **03 — Modelo Objetivo** del reporte HTML.
