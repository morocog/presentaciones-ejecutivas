# Bitácora de Estado y Memoria Viva · Oportunidad Comercial CEM
**Institución:** Colegio de Estudios Multidisciplinarios (CEM S.C.)  
**Fecha de corte:** 12 de noviembre de 2026  
**Líder del Proyecto:** Ricardo García (`rgarcia@telat-group.com`), Subdirector de Operaciones & Tecnología, Telat Group.  
**Equipo Telat Involucrado:** Mauricio Cruz (Director de Operaciones), Alejandro Valente Ortega (Gerente de Procesos y Calidad / SGC ISO).  

---

## 1. Contactos Clave y Dinámica del Cliente
- **Lic. Eduardo Alarcón:** **Dueño y Co-fundador del Colegio CEM** (junto con su esposa, ambos abogados). Es el tomador de decisión final económica y operativa.
- **Lic. Jacqueline Maldonado:** Coordinadora Administrativa (`coordinacionadmin@colegio-cem.mx` · Tel: `56 1953 8258`). Responsable de la gestión interna y seguimiento del proyecto.
- **Dolor crítico:** Llevan 8 meses consecutivos estancados en **112 alumnos inscritos al mes** con ~4,000 leads de Meta Ads. Su agencia anterior les prometió 300 alumnos y fracasó.
- **Equipo de ventas:** Tienen 4 vendedoras in-house que no son profesionales de cierre, están viciadas con enviar plantillas en celulares personales y se resistieron a usar un CRM previo.
- **Calendario Comercial:** Su público son abogados, peritos y policías. Tienen vacaciones judiciales de mediados de diciembre a principios de enero. La ventana comercial crítica es lo que resta de noviembre y primera mitad de diciembre para asegurar el ingreso de enero 2027.

---

## 2. Entregables Vigentes en Disco (Repositorio `presentaciones-ejecutivas`)
1. **Propuesta Comercial Oficial Cliente (3 Páginas exactas):**
   - PDF: `c:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\01-Propuestas-Comerciales\CEM-Colegio-Estudios-Multidisciplinarios\Propuesta_Comercial_CEM_Colegio_Estudios_Multidisciplinarios.pdf`
   - HTML fuente: `propuesta-comercial-cem.html`
   - Markdown: `PROPUESTA_COMERCIAL_CLIENTE_CEM.md`
   - Script de compilación: `c:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\scripts\export_cem_proposal_pdf.ps1`
2. **Simulador Interactivo de Flujo WhatsApp:**
   - HTML: `c:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\01-Propuestas-Comerciales\CEM-Colegio-Estudios-Multidisciplinarios\simulador-whatsapp-cem.html`
3. **Documentos Internos Previos:**
   - Dossier Ejecutivo para Luis Cortina: `Dossier_Ejecutivo_CEM_Colegio_Estudios_Multidisciplinarios.pdf`
   - RFQ Técnico Net2Alliance: `RFQ_Tecnico_Net2Alliance_CEM_Telat.pdf` (Código `RFQ-TELAT-N2A-2026-08`)

---

## 3. Estructura Comercial Entregada al Cliente
- **Escenario A: Proyecto Integral (Catálogo completo de 22 Diplomados):**
  - Setup Inicial: **$195,000 MXN** ($70k Consultoría SGC ISO + $125k Implementación WABA/CRM).
  - Póliza Mensual: **$38,000 MXN / mes** (Soporte + Auditoría de Calidad).
- **Escenario B: Piloto Fast-Track Temporada Alta (3 a 4 Certificaciones estrella):**
  - Setup Inicial: **$110,000 MXN** ($45k Consultoría SGC ISO + $65k Implementación WABA/CRM).
  - Póliza Mensual: **$28,000 MXN / mes** (Tarifa preferencial durante 60 días).
  - **Cláusula de Garantía:** 100% del setup del piloto ($110,000 MXN) tomado a cuenta del Proyecto Integral si deciden expandir a los 18 restantes.
  - Tiempo de entrega: **10 a 14 días hábiles**.
- **Business Case:** 112 alumnos base protegidos. Subir a 150-180 alumnos (+38 a +68 inscripciones) genera entre +$104,500 y +$187,000 MXN netos mensuales, pagando el proyecto en menos de 45 días.

---

## 4. Arquitectura y Análisis Financiero Interno (Vía Kommo Partner vs N2A)
- **Kommo Plan Avanzado (México):**
  - $558 MXN por usuario/mes.
  - **Condición de compra:** Bloque forzoso de 6 meses por adelantado ($3,348 MXN por usuario).
  - Para 5 usuarias: **$16,740 MXN de pago único inicial** (cubre los primeros 6 meses).
- **Reglas Meta WhatsApp Business (2025/2026):**
  - Modelo por mensaje individual entregado.
  - 1,000 mensajes de servicio gratis al mes por número. Mensajes excedentes: $0.0085 USD ($0.1565 MXN).
  - **Regla Click-to-WhatsApp:** Ventana de 72 horas 100% GRATIS para leads que entran por anuncios de Facebook/Instagram.
  - Consumo estimado Meta: ~$500 a $1,000 MXN / mes.
- **Flujo de Caja Real para Telat (Piloto):**
  - Setup cobrado a CEM: **$110,000 MXN**.
  - Pago inicial software 6 meses: **-$16,740 MXN**.
  - **Utilidad neta Día 1 en Telat:** **+$92,260 MXN limpios**.
  - Mensualidad cobrada a CEM: **$28,000 MXN / mes**.
  - Gasto operativo mensual (meses 1 a 6): ~$800 MXN (Meta).
  - **Flujo mensual neto para Telat:** **+$27,200 MXN / mes**.

---

## 5. Próximos Pasos Técnicos y Operativos
1. Enviar la propuesta formal en PDF (`Propuesta_Comercial_CEM_Colegio_Estudios_Multidisciplinarios.pdf`) junto con el NDA acordado por Alejandro Valente a Jacqueline Maldonado y Eduardo Alarcón.
2. **Laboratorio Sandbox Kommo & WhatsApp Cloud API (Agendado: Martes 17-Nov-2026):**
   - Número nuevo adquirido y con cuenta de WhatsApp eliminada (chip listo con señal para SMS).
   - Abrir cuenta de prueba de 14 días en Kommo con `rgarcia@telat-group.com` (aprovechando ventana hábil completa tras puente del lunes festivo).
   - Vincular a WhatsApp Cloud API mediante Meta Business Manager (contenedor `Telat Sandbox` con Facebook de Ricardo) o WhatsApp Web QR temporal.
   - Configurar Salesbot de 3 botones (Triage SEP-CONOCER / Diplomados / Asesor) y validar handover a consola de asesores.
   - Prueba de tráfico entrante desde WhatsApp personal.
3. Definir subdominio de marca blanca (`admisiones.telat.mx` / `cem.telat.mx`).

