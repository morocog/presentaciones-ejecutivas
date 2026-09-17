# 🏛️ Telat Group · Bóveda Central de Presentaciones Ejecutivas

Este repositorio contiene la **bóveda canónica y privada** de todas las propuestas comerciales, pliegos técnicos, protocolos de gobernanza WFM y presentaciones institucionales de Telat Group.

---

## 🔒 Política de Seguridad & Publicación On-Demand

1. **Privacidad de la Bóveda:** Este repositorio debe permanecer **100% PRIVADO**. No se utiliza GitHub Pages público en este repositorio para evitar la indexación involuntaria de propuestas cruzadas o benchmarks confidenciales.
2. **Micro-Sitios Públicos Efímeros:** Cuando un cliente específico (ej. TIP México, Movistar, etc.) requiere acceso web público para evaluación directiva, se utiliza el script `scripts/publish_presentation.ps1` para generar un repositorio satélite dedicado (ej. `tip-direccion`) con **única y exclusivamente** el material aprobado para ese cliente.
3. **Retiro de la Nube:** Una vez formalizado el contrato o cerrada la oportunidad, el micro-sitio satélite se pasa a privado o se archiva.

---

## 📂 Estructura Canónica de la Bóveda

```text
presentaciones-ejecutivas/
├── index.html                                        # Portal / Hub Maestro Central
├── .nojekyll                                         # Prevención de procesamiento Jekyll
│
├── 01-Propuestas-Comerciales/                        # Clientes y Cuentas Estratégicas
│   ├── TIP-Mexico/                                   # Propuesta, GOC Dashboard, Brief N2A
│   ├── Instituto-Tecnologico/                        # Propuesta, Consola GOC, Simulador Olas WFM
│   ├── ViaPath/                                      # Propuesta BPO Global
│   ├── Driven-Brands-AGN/                            # Solución Automotriz Omnicanal
│   └── NexGen-Agency/                                # Suite de Inteligencia Operativa & IA
│
├── 02-Direccion-y-Estrategia/                        # Institucional & Ecosistemas
│   ├── Presentacion-Digitalizacion/                  # Transformación Digital y Ecosistemas
│   └── Presentacion-Comercial-Telat/                 # Pitch Comercial Macro Telat Group
│
├── 03-Operaciones-y-WFM/                             # Gobernanza & Operaciones
│   └── STB-Late-Approved-2026/                       # Protocolo y Alineación Entradas Tardías
│
├── 04-Estudios-y-Benchmarks/                         # Análisis de Industria Confidencial
│   └── Estudio-Mercado-Competitivo-2026/             # Benchmark de Tarifas y Competidores BPO
│
├── docs/                                             # Fichas técnicas y memoria persistente
│   └── PENDIENTES.md                                 # Hoja de ruta y pendientes
│
└── scripts/                                          # Herramientas de automatización
    └── publish_presentation.ps1                      # Desplegador de micro-sitios públicos
```

---

## 🚀 Cómo Visualizar Localmente

Abre el archivo `index.html` en cualquier navegador web o utiliza la extensión **Live Server** de VS Code / Antigravity IDE para navegar fluidamente por todas las presentaciones sin necesidad de conexión a internet ni despliegues en la nube.
