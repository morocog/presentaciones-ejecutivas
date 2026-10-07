# 📘 Ficha Técnica: Refactorización SPA, Branding Telat & Blindaje Anti-Bucle (Simulador de Olas)

**Fecha:** 2026-10-07  
**Autor:** Antigravity (Pair Programming con Ricardo García)  
**Módulo:** `01-Propuestas-Comerciales/Instituto-Tecnologico/simulador-olas.html`  
**Estado:** ✅ Implementado, Probado en Chromium & Commiteado en Git  

---

## 1. Contexto y Síntomas

Al interactuar con el campo numérico de capacidad física del **Aula Alfa**, la aplicación web se congelaba por completo, bloqueando la pestaña de Google Chrome con un uso del 100% de CPU. Asimismo, la versión previa presentaba una altura vertical excesiva (>3,100px) que obligaba al usuario a realizar scroll prolongado para consultar tablas y gráficas, carecía de la identidad visual corporativa de Telat Group y mantenía los paneles de site fijos en la vista principal restando espacio operativo.

---

## 2. Causa Raíz

1. **Bucle Infinito en Asignación de Cola (`proyeccion`):**
   En el despachador de aulas de la propiedad reactiva `proyeccion`, el ciclo `while` evaluaba:
   ```javascript
   const capMaxEfectiva = Math.min(aulaAsignar.capacidad, limitePedagogico.value);
   const agentesAIniciar = Math.min(grupo.totalAgentes, capMaxEfectiva);
   if (agentesAIniciar > 0) { ... }
   ```
   Cuando el usuario borraba el valor del input para teclear una nueva cifra, `aulaAsignar.capacidad` pasaba momentáneamente a `""`, `null` o `0`. Esto causaba que `capMaxEfectiva` fuera `0` y `agentesAIniciar` fuera `0`. En consecuencia:
   - `agentesAIniciar > 0` evaluaba en falso.
   - `grupo.totalAgentes` no se decrementaba.
   - `qIdx` no avanzaba.
   - El aula seguía en la lista de disponibles.
   El bucle `while` se repetía de forma infinita en el hilo principal de JavaScript, congelando la ventana del navegador.

2. **Deuda Técnica de Maquetación y Navegación:**
   - Estructura monolítica sin tabs que acumulaba KPIs, paneles de site, controles WFM, dos tablas extensas y gráficas en una sola columna vertical.
   - Falta de cumplimiento de las directrices corporativas de Telat Group (ausencia de isotipo corporativo oficial, tipografía predeterminada y ausencia de paleta de marca `#3284C6` / `#EB5B27`).

---

## 3. Solución Implementada

1. **Blindaje Defensivo Anti-Bucle (4 Capas):**
   - *Capa 1 (Filtro Activo):* Descarte automático en `aulasLibres` de cualquier aula con `Number(a.capacidad) <= 0`, vacía o `NaN`.
   - *Capa 2 (Salida Inmediata):* Si la capacidad efectiva calculada es `capMaxEfectiva <= 0`, ejecución de `break` inmediato para no atrapar el hilo.
   - *Capa 3 (Avance Forzado):* Si `agentesAIniciar <= 0`, incremento de `qIdx++` y `continue`.
   - *Capa 4 (Circuit Breaker):* Límite estricto de seguridad `safetyGuard < 400` que impide bucles infinitos bajo cualquier estado transitorio del DOM.

2. **Arquitectura SPA de 4 Vistas Persistentes:**
   - **Tablero & Curvas (`dashboard`):** Vista principal compacta con mini-cards ejecutivas de KPIs, panel izquierdo de parámetros operativos WFM, gráfica de Curva de Capacidad SOTA (doble eje con barras de cuellos de botella) y gráfica complementaria de Composición Semanal de Plantilla por Estado (Ops, Nesting, Training, Bajas).
   - **Calendario de Olas (`olas`):** Tabla interactiva de las 22 olas comerciales con edición en línea y cascada masiva.
   - **Recursos de Site (`site`):** Panel desacoplado para instructores y aulas físicas con turnos, liberando el espacio del tablero principal.
   - **Sábana Semanal (`sabana`):** Auditoría forense de 30 semanas con encabezados *sticky* y toggle detallado/compacto.
   - Persistencia de pestaña activa en `localStorage` (`vistaActiva`).

3. **Branding Corporativo Telat Group:**
   - Navbar superior estilizado en grafito `#222221` con Logotipo Canónico (`https://telat.mx/assets/img/logo.png`), badge institucional de la propuesta y botones de acción rápida.
   - Acentos de color Telat: Celeste `#3284C6`, Naranja `#EB5B27` y Amarillo `#FECA66`.
   - Tipografía oficial Google Fonts (*DM Sans* para encabezados y *Montserrat* para texto y números).

---

## 4. Anti-Patrones / Prohibiciones

- 🚫 **PROHIBIDO** iterar con `while` sobre entradas numéricas de usuario sin salvaguarda de ciclo máximo (*circuit breaker*) o sin comprobar que `agentesAIniciar > 0`.
- 🚫 **PROHIBIDO** desbordar verticalmente herramientas directivas con componentes estáticos cuando pueden modularizarse en una SPA interactiva.
- 🚫 **PROHIBIDO** omitir la identidad corporativa y logotipo canónico de Telat Group en aplicaciones ejecutivas para clientes institucionales.

---

## 5. Verificación & Evidencia

- **Prueba en Chromium:**
  1. Se navegó a la aplicación y se verificó el montaje reactivo de Vue 3.
  2. Se conmutó a la pestaña **Recursos de Site**.
  3. Se borró por completo la capacidad de Aula Alfa (dejándola en blanco/0) y posteriormente se escribió `50`: **0 congelamientos, respuesta instantánea en 0ms**.
  4. Se conmutó a **Tablero & Curvas**: ambas gráficas Chart.js renderizaron en tiempo real.
  5. 0 errores en la consola de JavaScript.
- **Evidencia Visual:** Captura guardada en `brain/ddce0f69-04b4-480a-bf84-fbb6f2dc9fac/telat_spa_verified_1791412891963.png`.
