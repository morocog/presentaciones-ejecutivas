# 📘 Ficha Técnica: Simulador SOTA de Capacidad & Planeación WFM (Licitación Instituto)

**Fecha:** 2026-10-07  
**Autor:** Antigravity (Pair Programming con Ricardo García)  
**Módulo:** `01-Propuestas-Comerciales/Instituto-Tecnologico/simulador-olas.html`  
**Estado:** ✅ Implementado & Validado en Navegador  

---

## 1. Contexto y Síntomas

Durante la preparación técnica de la propuesta comercial para la licitación del Instituto Tecnológico, se requería una herramienta interactiva para dimensionar la rampa de contratación de 519 agentes hacia 2026-2027. La versión anterior del simulador presentaba las siguientes inconsistencias:
- Los parámetros de rampa de aprendizaje y eficiencia de nesting existían en la interfaz de usuario, pero el cálculo matemático subyacente los ignoraba por completo (asumía un 100% de rendimiento operativo inmediato tras la capacitación teórica).
- La lógica de ocupación de aulas bloqueaba espacios físicos teóricos para la fase de Nesting (OJT), distorsionando los cuellos de botella reales de la plataforma.
- La persistencia en `localStorage` estaba declarada pero sin funciones de guardado ni carga.
- La exportación a PDF se realizaba mediante captura de pantalla recortada (`html2canvas`), generando documentos ilegibles con tablas cortadas.
- La función de `autoBackfill` arrojaba de golpe 469 agentes en la Semana 1, saturando la cola de espera de forma ficticia antes de dar paso al calendario de 22 olas preprogramadas.

---

## 2. Causa Raíz

1. **Omisión de Factor Rampa en `proyeccion`:** El cálculo de `hcOpsProductivo` utilizaba una fórmula estática `Math.round(finalHC_Ops * (1 - shrinkPct))` sin iterar sobre la antigüedad de semanas de cada aula en operaciones (`semanasOpsActivas`).
2. **Confusión Operativa entre Aula Teórica y Piso Telefónico:** Nesting se procesaba como ocupante de aula física, cuando en operaciones de contact center el Nesting ocurre en plataforma con diademas telefónicas reales.
3. **Falta de Desacoplamiento en Backfill:** `autoBackfill` no discriminaba entre el déficit total inicial del contrato y la capacidad de absorción del site por cohorte, inyectando todo el faltante en una sola solicitud masiva.

---

## 3. Solución Implementada

1. **Motor de Rampa de Aprendizaje y Nesting SOTA:**
   - Se añadió el seguimiento individualizado de `semanasOpsActivas` por cada grupo activo en Ops.
   - Cálculo progresivo: `factorRampa = rendInicial + ((1 - rendInicial) * (aula.semanasOpsActivas / duracionRampa.value))`.
   - Se sumó la aportación productiva de Nesting (`rendimientoNesting = 60%`) sin consumir aulas teóricas.
2. **Gráfica Interactiva con Doble Eje (Y y Y2):**
   - Eje Y izquierdo: Líneas de Roster Contratado, Capacidad Productiva Real y Meta Comercial.
   - Eje Y2 derecho: Gráfico de barras ámbar con el semáforo de agentes varados en espera (`Agentes en Cola`).
   - Marcador scatter con forma de estrella (`✅ Meta Alcanzada`) en la semana exacta de cumplimiento del 100%.
   - Renderizado optimizado con debounce de 250ms.
3. **Calibración Estratégica de Auto-Backfill:**
   - Configurado en `autoBackfill = false` por defecto para respetar el cronograma planificado de 22 olas comerciales.
   - En caso de activación manual, el backfill solicita bloques manejables limitados a `agentesDefault` (50 agentes por cohorte), respetando los límites físicos de site e instructores.
4. **Persistencia Total en `localStorage`:**
   - Funciones `guardarEstado()` y `cargarEstado()` serializando los 17 parámetros de site, aulas y olas.
5. **Exportación Ejecutiva a PDF Vectorial (3 Páginas jsPDF):**
   - Generación de informe ejecutivo limpio con portada, gráficos de alta resolución, inventario de infraestructura y tabla de proyección semanal sin recortes.

---

## 4. Anti-Patrones & Prohibiciones

- 🚫 **PROHIBIDO** ignorar la curva de rampa en cálculos de fuerza productiva: ningún agente de nuevo ingreso produce al 100% en su primer día de operaciones.
- 🚫 **PROHIBIDO** bloquear aulas de capacitación para la fase de Nesting (OJT): el nesting se ejecuta en piso operativo.
- 🚫 **PROHIBIDO** inyectar bloques de contratación mayores a la capacidad de absorción física de site en rutinas de auto-backfill.

---

## 5. Verificación & Evidencia

- **Validación en Navegador:** Verificado mediante subagente de navegación en Chromium.
- **Métricas Comprobadas:**
  - 0 errores en consola JavaScript.
  - Renderizado en caliente de Vue 3 (`[v-cloak]` superado).
  - 5 tarjetas de KPI activas: Meta 519 contratos, Fuerza Productiva 363 agentes, Cumplimiento de Roster en Semana 30, Pico de 4 aulas simultáneas, Eficiencia 49.7%.
  - Gráfico de doble eje operativo con semáforo de cola de espera.
- **Evidencia Visual:** Captura registrada en `brain/ddce0f69-04b4-480a-bf84-fbb6f2dc9fac/simulador_olas_verified_1791412383780.png`.
