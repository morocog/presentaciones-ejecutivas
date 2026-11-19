# Informe Forense e Histórico: Operación Wine Country Gift Baskets (WCGB) & NexGen Agency

**Fecha de Auditoría:** 18 de Noviembre de 2026  
**Fuente de Verdad:** Telat Workspace Gateway v2.4 (Google Workspace corporativo: Drive & Gmail)  
**Alcance:** Rastreo forense de las temporadas históricas 2020 a 2023, acuerdos contractuales, análisis cuantitativo de FTEs, dimensionamiento de personal, organigrama de interlocutores y repositorio de recursos.

---

## 1. Resumen ejecutivo y cronología de campañas

La cuenta de Wine Country Gift Baskets (WCGB) fue operada por Telat Group a través de NexGen Agency en tres ciclos estacionales consecutivos (*Q4 Holiday Season*):

1. **Temporada 2020 (Piloto inicial & TTT):** Kickoff y transferencia de conocimiento mediante Train-the-Trainer (TTT) liderado por JC Velez (19 de octubre de 2020). Dotación inicial de 15 posiciones técnicas y de liderazgo.
2. **Temporada 2021 (Operación plena):** Reclutamiento en noviembre de 2021 (Corinne Ladenhauf y Gilberto Trejo). Go-live el 1 de diciembre de 2021. Pico de volumen en la semana 49 (6 al 12 de diciembre) con 3,379.96 horas facturadas en México y 84.50 FTEs semanales. Cierre de campaña el 22–23 de diciembre de 2021 con 98 agentes en roster.
3. **Temporada 2022 (Máxima dotación en nómina):** Kickoff el 4 de octubre de 2022. Entrenamiento presencial en CDMX conducido por Oscar Rosales con asistencia de JC Velez. Incorporación de Batches 3.1 a 3.4 y ampliación de +21 agentes (Batch 4.2). Go-live general el 4 de diciembre de 2022. Fin formal del proyecto notificado el 19 de diciembre de 2022 a las 15:52 CST con 116 colaboradores en nómina auditada.
4. **Conciliación 2023:** Cierre de nóminas históricas y conciliación de saldos y finiquitos de temporada.

---

## 2. Estructura de actores clave e interlocutores

### A. Broker / Socio Contratante (NexGen Agency)
- **Jose Carlos (JC) Velez Jr.** (*Operations & Training Manager*): Propietario de matrices maestras de staffing y currícula. Estuvo presencialmente en las sedes de CDMX en noviembre de 2022 (`jc@nexgenagency.com`).
- **Gladimir Cruz ("Glad")** (*Operations Manager*): Autor de las guías de setup técnico, Microsoft Edge, MFA en MyApps y reglas de visualización de IVR (`glad.cruz@nexgenagency.com`).
- **Christina Crespo** (*Senior Vice President of Operations*): Interlocutora comercial principal para aprobaciones de Headcount adicional y facturación (`christina@nexgenagency.com`).
- **Ephraim Samson** (*Real Time Analyst & Reporting Lead*): Analista desde Filipinas; remitía reportes de inContact para cálculo de horas facturables netas (`ephraim.samson@nexgenexpert.com`).

### B. Cliente Final (Wine Country Gift Baskets - WCGB)
- **Angela Johnson** (*Operations & Training Manager*): Material de entrenamiento y validación de usuarios en WebOE.
- **Jeff Faucet** (*Director*): Aprobación de incentivos y lineamientos generales del programa.
- **Michael Swanson / Andy** (*I.T. Leads*): Configuración de credenciales de red y telefonía.

### C. Estructura de Operaciones Telat Group
- **Ricardo García** (*Subdirector de Operaciones*): Gobernanza operativa integral, supervisión de KPIs y auditoría de horas.
- **Mauricio Cruz** (*Director de Operaciones*): Relación comercial con Christina Crespo y dimensionamiento contractual.
- **Oscar Rosales** (*Operations Manager & Lead Trainer*): Conducción de entrenamientos en CDMX, asignación de turnos y cierre formal de campaña.
- **Fabiola Alvarez** (*Workforce Management Specialist*): Conciliación de horas contra reportes de inContact y prenóminas.
- **Gilberto Trejo** (*Jefe de Atracción de Talento*): Reclutamiento de tandas de 80 a 100 candidatos bilingües.
- **Ricardo Morales** (*Gerente de TI*): Asignación y desmovilización de computadoras y 47 diademas USB en Sede Insurgentes.

---

## 3. Análisis matemático de Headcount y FTEs

### A. Consolidado histórico de Headcount
- **2020:** 15 colaboradores (Supervisores, formadores y analistas de WFM).
- **2021:** 98 colaboradores nominales en roster de facturación; 75 a 81 posiciones simultáneas en piso.
- **2022:** 116 colaboradores registrados en nómina auditada (`WINE NEXGEN.xlsx`); 7,209.15 horas netas trabajadas; desembolso de nómina de $714,923.12 MXN con sueldo base diario de $466.66 MXN.
- **Total acumulado:** Más de 220 profesionales bilingües movilizados en el ciclo de vida de la cuenta.

### B. Desglose semanal de FTEs en 2021 (Base 40 horas semanales)
A partir de los 4,798 registros de log de inContact en `WCGB Billable Hours 2021.xlsx`:

| Semana ISO | Rango de fechas | Fase operativa | HC activo | Horas México | FTE semanal México (40h) | Horas globales | FTE global (40h) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Semana 46** | 15 al 20 de Nov | TTT y calibración | 1 | 40.00 | **1.00** | 80.00 | 2.00 |
| **Semana 47** | 26 al 28 de Nov | Capacitación masiva | 48 | 1,050.30 | **26.26** | 2,100.60 | 52.51 |
| **Semana 48** | 29 Nov al 5 Dic | Go-live general | 78 | 3,150.87 | **78.77** | 6,301.75 | 157.54 |
| **Semana 49** | 6 al 12 de Dic | **Pico de temporada** | **81** | **3,379.96** | **84.50** | **6,759.91** | **169.00** |
| **Semana 50** | 13 al 19 de Dic | Meseta alta | 71 | 2,608.73 | **65.22** | 5,217.46 | 130.44 |
| **Semana 51** | 20 al 22 de Dic | Desmovilización | 41 | 804.07 | **20.10** | 1,608.13 | 40.20 |

> **Día pico histórico:** Viernes 10 de diciembre de 2021 con 81 agentes activos, 625.29 horas facturadas y **78.16 FTEs diarios** (sobre base de 8 horas).

### C. Curva de concurrencia horaria de FTEs en piso (Intradía)
Cálculo de agentes simultáneos en piso por intervalo horario (5:00 AM a 9:00 PM PT / 7:00 AM a 11:00 PM CDMX) derivado de la matriz de horarios de JC Velez:

| Intervalo Pacific Time (PT) | Hora local CDMX (CST) | FTEs Lunes | FTEs Miércoles | FTEs Viernes | FTEs Domingo | Perfil de demanda |
| :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **05:00 - 06:00 PT** | 07:00 - 08:00 CST | 7 | 4 | 5 | 8 | Apertura temprana |
| **06:00 - 07:00 PT** | 08:00 - 09:00 CST | 18 | 12 | 17 | 19 | Rampa matutina inicial |
| **07:00 - 08:00 PT** | 09:00 - 10:00 CST | 39 | 31 | 32 | 46 | Conexión de turnos intermedios |
| **08:00 - 11:00 PT** | 10:00 - 13:00 CST | 63 | 53 | 56 | 73 | Meseta matutina alta sostenida |
| **11:00 - 13:00 PT** | 13:00 - 15:00 CST | 64 | 53 | 57 | 74 | Entrada de turnos de mediodía |
| **13:00 - 14:00 PT** | **15:00 - 16:00 CST** | **74** | **60** | **63** | **77** | **Pico máximo en piso (corte logístico 1:00 PM PST)** |
| **14:00 - 15:00 PT** | 16:00 - 17:00 CST | 67 | 56 | 58 | 72 | Salida gradual de turnos matutinos |
| **15:00 - 16:00 PT** | 17:00 - 18:00 CST | 35 | 29 | 31 | 34 | Transición vespertina |
| **16:00 - 17:00 PT** | 18:00 - 19:00 CST | 21 | 15 | 13 | 14 | Descenso de llamadas |
| **17:00 - 21:00 PT** | 19:00 - 23:00 CST | 10 a 11 | 7 | 6 a 7 | 6 a 7 | Cobertura tardía (Batch 4.2) |
| **21:00 PT** | 23:00 CST | 0 | 0 | 0 | 0 | Cierre de operación |

---

## 4. Repositorio de recursos con enlaces directos en Google Workspace

### A. Workforce Management y Roster
- [Overall Program Expectations & Info (Google Sheet)](https://docs.google.com/open?id=1dtqth3PO2ua4AjfrNymnBCxw0W_XkhBbYLSYZi_d5Pg)
- [Copia de WCGB (MX) 11/2021 (Google Sheet)](https://docs.google.com/open?id=1hOh2j5PzW844rs9J80E8N_7JA_BTqu_s907O0wRDHzE)
- [Attendance Notification (Google Sheet)](https://docs.google.com/open?id=11ixGMlCyxn9uqUK-spibrVo92Wcn_C-EoK2_ZDAi3pc)
- Nómina Operativa 2022 (`WINE NEXGEN.xlsx`): En el hilo de Gmail `18aae487098593c0`.

### B. Capacitación e Inducción
- [Frequently Asked Questions - FAQ (Google Doc)](https://docs.google.com/open?id=1amWupVYSVce3PqfkipPD58Ve--yMLyEv)
- [WCGB Leadership Coaching Process and Guide (Google Doc)](https://docs.google.com/open?id=1BIEPNXHP8ULCxPukSDVx1feiocgZvH5b9EGXBELsiw0)
- [WCGB Computer Set Up 2021 (Google Doc)](https://docs.google.com/open?id=1aCKSlAv-jli6vzOTGlALsxcCsRR_3WC3)
- [WCGB 2021 Computer Requirements (Google Doc)](https://docs.google.com/open?id=1_oW2g7ZsoaaYAOVX8J-nWqm2RT3_g3HnB81DxTmj0Wk)

### C. Gobernanza y Finanzas (Gmail)
- Hilo `184beb2db6a3fa3c`: Fórmula oficial de facturación neta (*Agent Time Card* menos *Lunch Break* en inContact con Ephraim Samson).
- Hilo `1846255d4c5ccd3a`: Aprobación y asignación de batches adicionales (+21 HC en Batch 4.2).
- Hilo `1852c5fb975eab2e`: Notificación formal de cierre de proyecto (19 de diciembre de 2022 a las 15:52 CST).
- Hilo `1853beff034209fc`: Devolución de 47 diademas USB y desmovilización de equipos en Sede Insurgentes.

---

## 5. Reglas operativas y parámetros técnicos

1. **Sistema WebOE (OMS):** Uso obligatorio de ALL CAPS en campos de captura, navegación exclusiva mediante la tecla TAB (prohibido presionar ENTER) y búsquedas limitadas a *Customer Search*.
2. **Configuración inContact:** Supresión obligatoria de paneles de pantalla (`Display -> Panels: OFF`) para permitir que la ventana del IVR de pagos bancarios se despliegue sin colisiones.
3. **Restricciones de Alcohol:** Prohibición estricta de envío de vino a Alabama (AL), Mississippi (MS), South Dakota (SD) y Utah (UT). Firma presencial obligatoria de adulto (+21 años).
4. **Empoderamiento:** Autonomía del agente de hasta $500 USD por orden para resolución inmediata de incidencias sin escala a supervisión. Corte logístico de paquetería (UPS / FedEx) a la 1:00 PM PST.
