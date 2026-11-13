# Ficha de Solución: WhatsApp Cloud API vs App Coexistencia & Arquitectura Comercial CEM

**Fecha:** 2026-11-12  
**Autor:** Ricardo García (`rgarcia@telat-group.com`) & Antigravity  
**Repositorio:** `presentaciones-ejecutivas`  
**Área:** Propuestas Comerciales / Integración Tecnológica WhatsApp Business API  
**Contexto:** Preparación del entorno de laboratorio sandbox para la automatización de admisiones del Colegio de Estudios Multidisciplinarios (CEM S.C.).

---

## 1. Problema Abordado

Al preparar un número de teléfono celular nuevo para conectarlo a la WhatsApp Cloud API mediante una plataforma CRM (Kommo) para pruebas de laboratorio:
1. **Conflicto de Registro de Meta:** Si el número se inicializa primero en la app estándar de WhatsApp (móvil/Android/iOS), Meta bloquea la conexión en la nube arrojando error de registro duplicado.
2. **Duda sobre Credenciales y Privacidad de Clientes:** Preocupación operativa de si las credenciales personales de Facebook o del cliente (CEM) deben compartirse o intervenirse para conectar la API de Meta.
3. **Optimización Financiera y Reglas Meta 2025/2026:** Necesidad de verificar costos reales (Kommo bloque 6 meses vs reglas de cobro por mensaje y ventanas gratuitas de Click-to-WhatsApp en Meta Ads) para garantizar márgenes netos >85% en Telat sin depender de intermediarios como Net2Alliance.

---

## 2. Hallazgos Técnicos y Reglas de Arquitectura

### A. Regla Estricta de Coexistencia de Números en Meta
- Un mismo número E.164 **no puede coexistir** en la app móvil de WhatsApp (normal o Business) y en la WhatsApp Cloud API / BSP al mismo tiempo.
- **Protocolo de Liberación:** Se debe entrar a `Ajustes > Cuenta > Eliminar cuenta` dentro de la app móvil. Desinstalar la aplicación sin eliminar la cuenta mantiene el número bloqueado en los servidores de Meta.
- Al eliminar la cuenta en la app, el número queda en estado "virgen" en la base de datos de Meta, listo para recibir el SMS de verificación de la Cloud API en la ventana emergente de Kommo (*Embedded Signup*).

### B. Separación de Portafolios Comerciales en Meta Business Manager
- La ventana de *Log in with Facebook* es un handshake de autenticación de persona física, no de vinculación social.
- **En Pruebas Internas (Telat):** El administrador (Ricardo García) usa su cuenta de Facebook para generar un portafolio comercial de prueba (`Telat Sandbox`), manteniendo 100% aislado su perfil personal.
- **En Producción con Clientes (CEM):** Jamás se solicitan contraseñas al cliente. Se opera mediante:
  - *Opción A (Recomendada):* Acceso de Socio en Meta Business Manager (`business.facebook.com > Configuración del Negocio > Socios > Agregar Telat como Socio`).
  - *Opción B:* Sesión de 10 minutos por Google Meet compartiendo pantalla donde el cliente autoriza su propio número en su sesión activa de Meta.

### C. Estructura de Costos Verificada (Kommo + Meta 2025/2026)
- **Kommo Plan Avanzado (México):** $558 MXN por usuario/mes, pero facturado obligatoriamente en **bloques de 6 meses por adelantado** ($3,348 MXN por usuario). Para 5 usuarias: **$16,740 MXN de desembolso inicial**.
- **Meta WhatsApp Cloud API (2025/2026):**
  - Modelo por mensaje entregado. 1,000 conversaciones de servicio gratuitas al mes por número.
  - **Ventana Gratuita Click-to-WhatsApp:** 72 horas 100% libres de costo para cualquier mensaje si el usuario entra por anuncio de Facebook/Instagram.
- **Economics de Telat (Piloto CEM):**
  - Cobro Setup: $110,000 MXN.
  - Costo Software Semestral: -$16,740 MXN.
  - **Margen Neto Día 1: +$92,260 MXN limpios (83.8% de margen)**.
  - Cobro Póliza Mensual: $28,000 MXN / mes vs costo Meta ~$800 MXN/mes -> **+$27,200 MXN / mes netos**.

---

## 3. Plan de Acción y Agendamiento

- **Fecha de Ejecución:** Martes 17 de noviembre de 2026 (primer día hábil tras puente de asueto).
- **Entorno Listo:** Chip adquirido con señal SMS activa y cuenta de WhatsApp eliminada.
- **Ventana de Prueba:** Se activa el Free Trial de 14 días en Kommo con `rgarcia@telat-group.com` a partir del martes para no desperdiciar días en el fin de semana.
- **Archivos de Control:**
  - `01-Propuestas-Comerciales/CEM-Colegio-Estudios-Multidisciplinarios/BITACORA_ESTADO_CEM.md`
  - `docs/PENDIENTES.md`

