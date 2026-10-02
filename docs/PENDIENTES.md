# 📋 PENDIENTES & HOJA DE RUTA: PRESENTACIONES EJECUTIVAS

> 💡 **Validación Rápida con 1 Clic en Obsidian:** Haz clic directamente sobre la casilla `[ ]` para marcarla como `[x]` una vez probada en producción.

---

## 🔴 1. VERIFICACIONES PENDIENTES EN CALIENTE (seguras, no urgentes)

- [x] Probar la navegación móvil en el celular accediendo a `https://morocog.github.io/presentaciones-ejecutivas/`. *(✅ Validado en Móvil)*
- [x] Validar el botón de "Copiar Enlace Directo" en móvil para compartir presentaciones específicas. *(✅ Validado)*
- [x] Eliminar el repositorio remoto `paginas-prueba` — **COMPLETADO 2026-09-27**: retirado de público, carpeta local eliminada y repositorio remoto borrado. Verificado con 404 autenticado.
- [x] Eliminar los repositorios remotos `ai-itsm-integration` y `nlp-ticket-classifier` — **COMPLETADO 2026-09-27**: ambos retirados de público, carpetas locales eliminadas y repositorios remotos borrados. Verificado con 404 autenticado.
- [x] Confirmar que el micro-sitio público `tip-direccion` siga visible en `https://morocog.github.io/tip-direccion/` para los directivos de TIP México. *(✅ Validado)*

---

## 🟡 2. MEJORAS FUTURAS & ROADMAP

- [ ] Incorporar el deck comercial interactivo de la campaña Movistar Portabilidad en `01-Propuestas-Comerciales/Movistar-Portabilidad/`.
- [x] Exportador de presentaciones a PDF de alta resolución con vista ejecutiva 16:9 panorámica — **COMPLETADO 2026-10-01**: Implementado estándar `@media print` en `Presentacion-Comercial-Telat` con división balanceada de 6 casos en 2 láminas horizontales de 3 columnas (3 y 3), sustitución de iframes por fichas mockup HD de software y compilador headless Chromium automatizado (`scripts/export_pdf.ps1`). Generado `Presentacion_Comercial_Telat_Group.pdf` (11 páginas vectoriales HD).
- [ ] Script unificado en PowerShell para archivar micro-sitios públicos con 1 solo comando tras la firma de contratos.

---

## 🟢 3. DECISIONES ARQUITECTÓNICAS CONFIRMADAS

- **Acceso Móvil Flexible a Bóveda:** `presentaciones-ejecutivas` se mantiene activa con GitHub Pages para permitir a Ricardo consultar y presentar desde cualquier dispositivo móvil sin requerir la PC de trabajo.
- **MorocoVoice Público:** `MorocoVoice` se mantiene 100% público en GitHub como herramienta abierta / open-tool para colaboración con agentes de IA y equipo.
- **Eliminación Total de Dummies:** `ai-itsm-integration`, `nlp-ticket-classifier` y `paginas-prueba` se eliminan por completo de local y GitHub. **Estado 2026-09-27: COMPLETADO** — borrados de local y de GitHub (404 autenticado verificado) tras retirarlos de público. Ver `telat-master-wiki/log.md` [2026-09-27].
- **Micro-Sitios Satélite Efímeros:** Para clientes externos en negociación, se utiliza la publicación aislada (ej. `tip-direccion`).
