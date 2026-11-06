# Dossier Ejecutivo & Oportunidad Comercial · Telat Group
## Real Value Rx (San Antonio, Texas)

**Documento Estratégico de Uso Interno · Confidencial**  
**Fecha:** 5 de noviembre de 2026  
**Área Emisora:** Dirección de Operaciones & Tecnología · Telat Group  
**Para:**
* **Luis Cortina**, Apoderado Legal de Telat Group
* **Mauricio Cruz**, Director de Operaciones y Dirección Comercial (en funciones)
* **Fabiola Álvarez**, Gerencia de Workforce Management (WFM)

**Prospecto:** Real Value Rx (Distribuidor mayorista de productos farmacéuticos genéricos)  
**Sede del Prospecto:** San Antonio, Texas, EE. UU.  
**Interlocutor Clave:** Trevor Battah (`tevorb@realvalueproducts.com` · Tel: (210) 868-3288)  
**Reunión Clave:** Sesión de alineación vía Zoom con el CEO y el VP de Ventas de Real Value Rx.  

---

### 1. Perfil del Prospecto y Naturaleza de la Operación B2B

Real Value Rx es un distribuidor mayorista estadounidense de medicamentos genéricos para farmacias comunitarias e independientes. Su requerimiento comercial consiste en un centro de contacto saliente (outbound) enfocado en prospección y reactivación de cuentas comerciales.

**Factores Operativos Fundamentales:**
1. **Llamadas B2B Puras:** La operación es 100% de negocio a negocio (farmacia independiente a distribuidor mayorista). **No hay contacto con pacientes finales**, lo cual elimina fricciones de normativas clínicas de pacientes (HIPAA) y simplifica los protocolos de calidad.
2. **Mensaje de Campaña Ultracorto:** Cada llamada comunica una sola notificación concreta de catálogo (por ejemplo: disponibilidad de lote de un medicamento genérico de alta demanda o una presentación específica con precio preferencial).
3. **Desenlace Binario Exclusivo:** Toda llamada termina únicamente en una de dos salidas:
   * **Salida A (Transferencia Caliente):** Conectar de inmediato en vivo a la farmacia con un ejecutivo de ventas interno de Real Value Rx.
   * **Salida B (Envío Digital de Alta):** Despachar en tiempo real durante la llamada un enlace vía SMS o correo electrónico para que la farmacia complete su apertura de cuenta mayorista.
4. **Listas e Instrucciones Internas:** Real Value Rx genera las listas de prospectos y los guiones internamente, con directrices sencillas por campaña.

---

### 2. Dimensión Matemática y Desafío Operativo (Workforce Management)

El correo del prospecto estipula un universo de **aproximadamente 20,000 farmacias independientes**, con una frecuencia de contacto de **2 a 3 llamadas por semana a cada farmacia**.

* **Volumen Semanal Proyectado:** 40,000 a 60,000 intentos de llamada a la semana (promedio canónico de **50,000 llamadas semanales**).
* **Volumen Diario:** 10,000 intentos de marcación al día.
* **Ventana Operativa:** Lunes a viernes, de 9:00 a 17:00 horas (San Antonio, Texas / Central Standard Time = 40 horas operativas por semana).

#### Premisas Base para Dimensionamiento de WFM (Fabiola Álvarez)
* **Datos Operativos para Modelado:** AHT (Average Handling Time) estimado de **90 a 150 segundos** por llamada efectiva (considerando tiempo de espera en conmutador de la farmacia, entrega del mensaje comercial de 30 a 45s, validación de teléfono para SMS o puente de transferencia en caliente y tipificación posterior), con marcación saliente concentrada en horario comercial de Texas (Central Time) y cadencia de 2 a 3 toques semanales por registro.
* **Jurisdicción de WFM:** La Gerencia de Workforce Management (**Fabiola Álvarez**) definirá formalmente el dimensionamiento de capacidad, cálculo oficial de FTEs, mermas (*shrinkage*) y curvas de staffing requeridas en caso de que el cliente opte por esquemas de personal humano.
* **Estrategia de Piloto Recomendada (30 a 45 Días):**
  * Trevor solicita explícitamente iniciar con un piloto: *"We would like to start with a pilot and scale from there"*.
  * El piloto no debe abarcar las 20,000 farmacias simultáneas. La recomendación operativa es acotarlo a una cohorte de **1,500 a 2,500 farmacias** (3,500 a 6,000 llamadas semanales) con una célula reducida, midiendo tasa de contacto real (*connect rate*), tasa de transferencia y conversión a enlaces enviados.

---

### 3. Viabilidad Técnica con Inteligencia Artificial de Voz (Voice AI)

La idea original de explorar Inteligencia Artificial en este proyecto no sólo es factible, sino que constituye el **caso de uso ideal de la industria**:
* **Conversación Acotada (30 a 60 segundos):** La IA no requiere vender de forma consultiva ni resolver objeciones farmacéuticas profundas. Solo notifica el producto, detecta si la farmacia tiene interés y ofrece transferir o mandar el link.
* **Detección Instantánea de Buzones (AMD - Answering Machine Detection):** La tecnología de voz descarta buzones de voz en menos de 1.5 segundos, logrando que sólo las llamadas con interacción humana genuina consuman tiempo.
* **Capacidad de Concurrencia Masiva:** La plataforma puede disparar cientos de llamadas simultáneas sin necesidad de reclutar, capacitar ni coordinar turnos de 50 personas.
* **Disparo Omnicanal Automatizado:** La IA puede ejecutar webhooks hacia Twilio/SendGrid para disparar el mensaje de texto o correo con el enlace durante la llamada en milisegundos.

---

### 4. Matriz Comparativa de los Tres Modelos Comerciales

Para la presentación con Trevor Battah y los directivos de Real Value Rx, se definen tres opciones comerciales:

| Característica / Criterio | Modelo 1: 100% Presencial (Humano) | Modelo 2: Híbrido (Voz IA + Célula Presencial) | Modelo 3: 100% Virtual (Voz IA Autónoma) |
| :--- | :--- | :--- | :--- |
| **Arquitectura de Marcación** | Marcador predictivo / asistido operado 100% por agentes humanos. | Agente de Voz IA ejecuta el barrido masivo de las 50,000 llamadas semanales. | Agente de Voz IA ejecuta el 100% de las 50,000 llamadas semanales. |
| **Interacción y Calificación** | Conversación completa atendida por agentes en sala. | La IA entrega el mensaje, califica el interés y filtra buzones. | La IA entrega el mensaje, resuelve preguntas frecuentes de catálogo y califica interés. |
| **Gestión de Transferencias / Enlaces** | El mismo agente envía el SMS/Email o transfiere a los vendedores de Trevor. | La IA transfiere en caliente a una célula núcleo de **3 agentes presenciales de Telat** para cierre y alta. | La IA envía el SMS/Email en automático y transfiere llamadas en caliente directamente a los vendedores de Real Value Rx. |
| **Ubicación Operativa** | **El Paso, Texas** (Onshore) o **Ciudad de México** (Nearshore Hub). | Capa de Voz en la nube + Célula de 3 agentes en El Paso, TX o CDMX. | Infraestructura en la nube con interconexión telefónica directa a conmutador del cliente. |
| **Tarifas Comerciales** | • **El Paso, TX:** 30.00 USD / hora / agente<br>• **Ciudad de México:** 17.00 USD / hora / agente | Tarifa formal cotizada de **0.65 USD por minuto de Voz IA** + Tarifa horaria de la célula de 3 agentes (30 USD El Paso / 17 USD CDMX). | Tarifa formal cotizada de **0.65 USD por minuto de Voz IA** conectado + Cuota mensual de plataforma. |
| **Requerimiento WFM (Fabiola)** | 3 a 5 agentes (Piloto inicial); dimensionamiento de escala por WFM. | **3 agentes comerciales dedicados** en piso (perfil cerrador / Inside Sales). | **Cero agentes humanos de Telat en nómina.** Cero carga de rotación de personal. |
| **Tiempo de Rampa (Ramp Time)** | 3 a 4 semanas (reclutamiento, selección bilingüe, capacitación y curvas). | 10 a 14 días hábiles (entrenamiento de prompts de IA, integración SIP y calibración de 3 agentes). | 5 a 7 días hábiles (configuración de guiones de IA, aprovisionamiento de números locales y pruebas SIP). |

---

### 5. Respuestas Puntuales a las Tres Peticiones de Trevor Battah

En su correo, Trevor solicita formalmente tres puntos específicos que deben responderse con claridad en la reunión:

#### 1. Esquema de Precios para el Piloto (Pricing & Setup)
* **Modelo Presencial (Piloto 3 agentes):**
  * Opción El Paso, Texas: 30.00 USD / hora facturable por agente.
  * Opción Ciudad de México: 17.00 USD / hora facturable por agente.
  * Cargo de Setup & Onboarding: 2,500 USD (configuración de campañas, telefonía, guiones y capacitación inicial).
* **Modelo Híbrido (Piloto IA + 3 agentes presenciales):**
  * Voz IA (Tarifa formal cotizada): **0.65 USD por minuto de interacción de voz completada**.
  * Célula Humana Presencial: Facturación regular por hora (30 USD El Paso / 17 USD CDMX).
  * Setup Tecnológico: 3,500 USD (programación del modelo de lenguaje, síntesis de voz, integración de webhooks SMS/Email y pruebas de transferencia SIP).
* **Modelo 100% IA Autónoma:**
  * Consumo de Voz IA (Tarifa formal cotizada): **0.65 USD por minuto de llamada conectada con farmacia**.
  * Fee de Mantenimiento de Plataforma: 1,500 USD / mes (monitoreo de modelos, calibración continua de guiones y soporte de SIP trunks).
  * Setup Tecnológico: 3,000 USD (puesta a punto, licenciamiento y pruebas extremo a extremo).

#### 2. Tiempo de Rampa (*Ramp Time* de Contrato Firmado a Llamadas en Vivo)
* **Modelo 100% IA:** **5 a 7 días hábiles**. La infraestructura y el aprovisionamiento de líneas locales de Texas permiten salir en vivo en menos de una semana.
* **Modelo Híbrido:** **10 a 14 días hábiles**, combinando la puesta a punto de la IA con la capacitación comercial de los 3 agentes presenciales de Telat.
* **Modelo 100% Presencial:** **2 a 3 semanas**, requiriendo proceso completo de selección, inducción de producto farmacéutico y curvas de aprendizaje de operadores humanos.

#### 3. Reporte Diario de Muestra y Referencias Comerciales
* **Reporte Diario Consolidado:** Se entrega cada día a las 18:00 horas CST con las siguientes métricas desglosadas por campaña y producto:
  * Total de marcaciones realizadas (*Dials*).
  * Tasa de contacto efectivo (*Connect Rate* / Farmacéutico en línea).
  * Desglose de no contacto (buzón de voz, línea ocupada, número no disponible).
  * Enlaces enviados en tiempo real (SMS y correos entregados exitosamente).
  * Transferencias calientes ejecutadas hacia los ejecutivos comerciales de Real Value Rx.
  * Transcripciones completas y grabaciones de audio auditables por muestra o al 100%.
* **Referencias de Clientes:** Telat Group cuenta con más de dos décadas de trayectoria respaldando operaciones corporativas binacionales en salud, finanzas y servicios B2B, con infraestructura física propia en El Paso, Texas y Ciudad de México, bajo certificaciones internacionales ISO 9001, ISO 27001 e ISO 22301.

---

### 6. Ruta de Acción Inmediata para la Reunión de Hoy (Zoom con Trevor, CEO y VP)

1. **Destacar la Presencia Onshore en Texas:** Aclarar que Telat cuenta con **instalaciones y operación en El Paso, Texas**, satisfaciendo plenamente la expectativa de agentes dentro del estado de Texas, combinada con capacidades Nearshore en CDMX para economías de escala.
2. **Presentar el Enfoque Híbrido como la Solución Superior:** Explicar cómo la IA absorbe el desgaste de 50,000 llamadas mientras una célula especializada cierra las transferencias con alta efectividad.
3. **Acordar Parámetros del Piloto:** Fijar duración de 30 días, universo de prueba de 2,000 farmacias y validación de las primeras integraciones tecnológicas (envío de SMS y transferencia SIP caliente).

