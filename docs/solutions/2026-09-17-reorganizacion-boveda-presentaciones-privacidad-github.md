# 🏛️ Ficha Técnica: Reorganización de Bóveda Central de Presentaciones y Blindaje de Repositorios en GitHub

**Fecha:** 2026-09-17  
**Autor:** Ricardo García / Antigravity IDE  
**Repositorio:** `presentaciones-ejecutivas`  
**Clasificación:** Arquitectura, Seguridad & Gobernanza  

---

## 1. Contexto y Síntomas

Con el crecimiento de proyectos y propuestas comerciales en Telat Group, existía dispersión de presentaciones interactivas en HTML a lo largo de varios directorios (`paginas-prueba`, `presentaciones-ejecutivas`, `tip-direccion`), con múltiples archivos duplicados (`index.html` y `presentacion.html` redundantes en cada subdirectorio). Adicionalmente, el repositorio maestro `presentaciones-ejecutivas` y repositorios de código fuente (`ai-itsm-integration`, `nlp-ticket-classifier`, `MorocoVoice`) se encontraban con visibilidad **Pública** en GitHub, exponiendo información confidencial de clientes, estudios de mercado y propiedad intelectual en internet.

---

## 2. Causa Raíz

1. **Falta de Bóveda Estructurada:** Las presentaciones se creaban como pruebas ad-hoc en repositorios temporales (`paginas-prueba`) o sin categorización estandarizada dentro de `presentaciones-ejecutivas`.
2. **Exposición Cruzada en GitHub Pages:** Al habilitar GitHub Pages sobre un repositorio con múltiples presentaciones de diferentes clientes, la URL raíz permitía a cualquier usuario explorar todas las propuestas y estrategias internas.
3. **Falta de Ciclo de Vida Efímero para Clientes:** No existía un protocolo claro para crear y destruir accesos públicos una vez finalizada la negociación comercial.

---

## 3. Solución Implementada

### A. Bóveda Central Privada (`presentaciones-ejecutivas`)
Se consolidaron todas las presentaciones en 4 categorías canónicas dentro de un repositorio privado:
- `01-Propuestas-Comerciales/`: `TIP-Mexico`, `Instituto-Tecnologico`, `ViaPath`, `Driven-Brands-AGN`, `NexGen-Agency`.
- `02-Direccion-y-Estrategia/`: `Presentacion-Digitalizacion`, `Presentacion-Comercial-Telat`.
- `03-Operaciones-y-WFM/`: `STB-Late-Approved-2026`.
- `04-Estudios-y-Benchmarks/`: `Estudio-Mercado-Competitivo-2026`.

### B. Hub Maestro Ejecutivo (`index.html`)
Se construyó un portal central interactivo con:
- Buscador en tiempo real por palabras clave, cliente y tecnología.
- Filtro por categoría visual mediante badges.
- Identidad corporativa estricta Telat (DM Sans, Montserrat, paleta de colores oficial y logotipo canónico).
- Acceso directo a dashboards GOC, simuladores de capacidad y pliegos técnicos.

### C. Estrategia de Micro-Sitios Públicos Efímeros
- La bóveda central permanece privada y libre de GitHub Pages.
- Para clientes activos en negociación (como TIP México), se utiliza el repositorio satélite público `tip-direccion` de forma exclusiva.
- Se implementó el script `scripts/publish_presentation.ps1` para publicar a 1 clic cualquier presentación a un nuevo micro-sitio público cuando sea necesario.

### D. Depuración de Repositorios Dummies & Seguridad
- Se rescataron los assets de `paginas-prueba` y se eliminó la carpeta local.
- Se eliminó la carpeta huérfana vacía `estudio-tec`.
- Se generaron las directrices de privacidad para repositorios remotos en GitHub.

---

## 4. Anti-Patrones y Prohibiciones

1. **PROHIBIDO:** Publicar GitHub Pages sobre el repositorio central `presentaciones-ejecutivas` (riesgo de fuga de información de clientes y estrategias internas).
2. **PROHIBIDO:** Mezclar material de diferentes clientes en un mismo repositorio público de GitHub Pages.
3. **PROHIBIDO:** Duplicar archivos de presentación con nombres redundantes (`presentacion.html` vs `index.html`).

---

## 5. Verificación & Evidencia

- [x] Rescate y migración de 100% de presentaciones desde `paginas-prueba` y `presentaciones-ejecutivas`.
- [x] Limpieza de carpetas huérfanas y directorios obsoletos (`estudio-tec`, `paginas-prueba`, `Direccion-General`, `Clientes-Estrategicos`).
- [x] Portal maestro `index.html` validado con búsqueda reactiva y filtros de categoría.
- [x] Script `publish_presentation.ps1` creado y documentado.
- [x] Memoria persistente y `docs/PENDIENTES.md` creados y actualizados.
