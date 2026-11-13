import os
import shutil
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE

def create_presentation():
    base_dir = r"c:\Users\SDVP\Documents\GitHub\presentaciones-ejecutivas\01-Propuestas-Comerciales\UVC-Unlimited-Vacation-Club"
    assets_dir = os.path.join(base_dir, "assets")
    cert_dir = os.path.join(assets_dir, "certificaciones")
    clients_dir = os.path.join(assets_dir, "clients")
    output_pptx = os.path.join(base_dir, "Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat.pptx")
    downloads_pptx = os.path.join(os.environ["USERPROFILE"], "Downloads", "Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat.pptx")

    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Colors
    c_navy_dark = RGBColor(11, 19, 43)
    c_navy = RGBColor(20, 41, 92)
    c_slate_dark = RGBColor(15, 23, 42)
    c_white = RGBColor(255, 255, 255)
    c_orange = RGBColor(235, 91, 39)
    c_blue = RGBColor(32, 121, 200)
    c_yellow = RGBColor(254, 202, 102)
    c_sky = RGBColor(56, 189, 248)
    c_text_dark = RGBColor(15, 23, 42)
    c_text_muted = RGBColor(71, 85, 105)
    c_card_border = RGBColor(203, 213, 225)
    c_card_bg = RGBColor(248, 250, 252)
    c_emerald = RGBColor(16, 185, 129)

    font_main = "Montserrat"
    font_body = "Arial"

    logo_telat = os.path.join(assets_dir, "logo_telat_canonical.png")
    logo_uvc_light = os.path.join(assets_dir, "uvc_logo.png")
    logo_uvc_dark = os.path.join(assets_dir, "uvc_logo_dark.png")

    def add_header(slide, title_text, category_text, dark=False):
        cat_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.35), Inches(8.5), Inches(0.3))
        p_cat = cat_box.text_frame.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.name = font_main
        p_cat.font.size = Pt(10)
        p_cat.font.bold = True
        p_cat.font.color.rgb = c_orange if not dark else c_yellow

        t_box = slide.shapes.add_textbox(Inches(0.7), Inches(0.6), Inches(9.0), Inches(0.65))
        p_t = t_box.text_frame.paragraphs[0]
        p_t.text = title_text
        p_t.font.name = font_main
        p_t.font.size = Pt(26)
        p_t.font.bold = True
        p_t.font.color.rgb = c_text_dark if not dark else c_white

        if os.path.exists(logo_telat):
            slide.shapes.add_picture(logo_telat, Inches(9.8), Inches(0.35), height=Inches(0.75))
        uvc_img = logo_uvc_dark if dark else logo_uvc_light
        if os.path.exists(uvc_img):
            slide.shapes.add_picture(uvc_img, Inches(10.75), Inches(0.42), height=Inches(0.62))

        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.7), Inches(1.25), Inches(11.933), Inches(0.02))
        line.fill.solid()
        line.fill.fore_color.rgb = c_card_border if not dark else RGBColor(51, 65, 85)
        line.line.color.rgb = c_card_border if not dark else RGBColor(51, 65, 85)

    def add_footer(slide, current, total=11, dark=False):
        f_box = slide.shapes.add_textbox(Inches(0.7), Inches(7.05), Inches(10), Inches(0.3))
        p = f_box.text_frame.paragraphs[0]
        p.text = "Telat Group · Solución Operativa y Propuesta Comercial · Unlimited Vacation Club (UVC)"
        p.font.name = font_body
        p.font.size = Pt(9.5)
        p.font.bold = True
        p.font.color.rgb = c_text_muted if not dark else RGBColor(148, 163, 184)

        pg_box = slide.shapes.add_textbox(Inches(11.5), Inches(7.05), Inches(1.1), Inches(0.3))
        p_pg = pg_box.text_frame.paragraphs[0]
        p_pg.alignment = PP_ALIGN.RIGHT
        p_pg.text = f"{current:02d} / {total:02d}"
        p_pg.font.name = font_main
        p_pg.font.size = Pt(10)
        p_pg.font.bold = True
        p_pg.font.color.rgb = c_text_muted if not dark else RGBColor(148, 163, 184)

    # ==========================================
    # SLIDE 1: PORTADA EJECUTIVA CO-BRANDED
    # ==========================================
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = c_navy_dark
    bg1.line.color.rgb = c_navy_dark

    if os.path.exists(logo_telat):
        s1.shapes.add_picture(logo_telat, Inches(0.9), Inches(0.6), height=Inches(1.1))
    tb_brand = s1.shapes.add_textbox(Inches(2.1), Inches(0.75), Inches(4.0), Inches(0.8))
    p_br1 = tb_brand.text_frame.paragraphs[0]
    p_br1.text = "TELAT GROUP"
    p_br1.font.name = font_main
    p_br1.font.size = Pt(22)
    p_br1.font.bold = True
    p_br1.font.color.rgb = c_white
    p_br2 = tb_brand.text_frame.add_paragraph()
    p_br2.text = "CONTACT CENTER & BPO SOLUTIONS"
    p_br2.font.name = font_main
    p_br2.font.size = Pt(9.5)
    p_br2.font.bold = True
    p_br2.font.color.rgb = c_orange

    if os.path.exists(logo_uvc_dark):
        s1.shapes.add_picture(logo_uvc_dark, Inches(9.2), Inches(0.7), height=Inches(0.9))

    badge = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(2.1), Inches(4.6), Inches(0.45))
    badge.fill.solid()
    badge.fill.fore_color.rgb = RGBColor(30, 41, 59)
    badge.line.color.rgb = c_orange
    p_b = badge.text_frame.paragraphs[0]
    p_b.text = "●  SOLUCIÓN TELAT · PROPUESTA ECONÓMICA"
    p_b.font.name = font_main
    p_b.font.size = Pt(11)
    p_b.font.bold = True
    p_b.font.color.rgb = c_yellow

    tb_h = s1.shapes.add_textbox(Inches(0.9), Inches(2.7), Inches(11.5), Inches(2.5))
    tf_h = tb_h.text_frame
    tf_h.word_wrap = True
    p1 = tf_h.paragraphs[0]
    p1.text = "Operación Bilingüe con Inteligencia Artificial y Personal 100% Dedicado"
    p1.font.name = font_main
    p1.font.size = Pt(38)
    p1.font.bold = True
    p1.font.color.rgb = c_white

    p2 = tf_h.add_paragraph()
    p2.text = "\nModelo diseñado a la medida de Unlimited Vacation Club (UVC): atención exclusiva al socio, analítica operativa al 100% y blindaje transaccional PCI DSS."
    p2.font.name = font_body
    p2.font.size = Pt(17)
    p2.font.color.rgb = RGBColor(226, 232, 240)

    meta_info = [
        ("CLIENTE OBJETIVO", "Unlimited Vacation Club"),
        ("ESQUEMA OPERATIVO", "Recursos 100% Dedicados"),
        ("COBERTURA", "Bilingüe México – USA"),
        ("VIGENCIA", "Noviembre 2026")
    ]
    for i, (k, v) in enumerate(meta_info):
        left = Inches(0.9 + i * 2.92)
        card = s1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(5.5), Inches(2.75), Inches(1.2))
        card.fill.solid()
        card.fill.fore_color.rgb = RGBColor(20, 32, 60)
        card.line.color.rgb = RGBColor(51, 65, 85)
        tf = card.text_frame
        tf.word_wrap = True
        pk = tf.paragraphs[0]
        pk.text = k
        pk.font.name = font_main
        pk.font.size = Pt(9.5)
        pk.font.bold = True
        pk.font.color.rgb = c_sky
        pv = tf.add_paragraph()
        pv.text = v
        pv.font.name = font_main
        pv.font.size = Pt(13)
        pv.font.bold = True
        pv.font.color.rgb = c_white

    add_footer(s1, 1, dark=True)

    # ==========================================
    # SLIDE 2: ACERCA DE NOSOTROS (650 EMPLEADOS + IA)
    # ==========================================
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "Acerca de Nosotros", "Identidad Corporativa")

    box_l = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(1.5), Inches(5.8), Inches(2.1))
    box_l.fill.solid()
    box_l.fill.fore_color.rgb = c_white
    box_l.line.color.rgb = c_card_border
    tf_l = box_l.text_frame
    tf_l.word_wrap = True
    pl1 = tf_l.paragraphs[0]
    pl1.text = "20+ AÑOS DE EXPERIENCIA"
    pl1.font.name = font_main
    pl1.font.size = Pt(11)
    pl1.font.bold = True
    pl1.font.color.rgb = c_orange
    pl2 = tf_l.add_paragraph()
    pl2.text = "\nSomos una empresa 100% Mexicana de Contact Center y Gestión de Procesos BPO en empresas nacionales y extranjeras."
    pl2.font.name = font_main
    pl2.font.size = Pt(16)
    pl2.font.bold = True
    pl2.font.color.rgb = c_text_dark

    callout = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(3.8), Inches(5.8), Inches(2.9))
    callout.fill.solid()
    callout.fill.fore_color.rgb = c_slate_dark
    callout.line.color.rgb = c_orange
    callout.line.width = Pt(2)
    tf_c = callout.text_frame
    tf_c.word_wrap = True
    pc1 = tf_c.paragraphs[0]
    pc1.text = "650 EMPLEADOS"
    pc1.font.name = font_main
    pc1.font.size = Pt(36)
    pc1.font.bold = True
    pc1.font.color.rgb = c_yellow

    pc2 = tf_c.add_paragraph()
    pc2.text = "Con Integración Completa de Inteligencia Artificial"
    pc2.font.name = font_main
    pc2.font.size = Pt(15)
    pc2.font.bold = True
    pc2.font.color.rgb = c_white

    pc3 = tf_c.add_paragraph()
    pc3.text = "\nOperación moderna potenciada por IA para auditoría automática al 100%, Speech & Text Analytics en vivo y máxima productividad."
    pc3.font.name = font_body
    pc3.font.size = Pt(12)
    pc3.font.color.rgb = RGBColor(226, 232, 240)

    pillars = [
        ("Importante Presencia en USA", "Cobertura binacional bilingüe con sede operativa en El Paso, Texas."),
        ("Soluciones Integrales BPO", "Gestión de procesos de extremo a extremo adaptada a cada socio."),
        ("Mesa de Control y Trabajo", "Monitoreo en tiempo real de indicadores, WFM y adherencia operativa."),
        ("Fondo de Inversión", "Solidez financiera que respalda el desarrollo tecnológico futuro.")
    ]
    for i, (pt_text, pd_text) in enumerate(pillars):
        col = i % 2
        row = i // 2
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7 + col * 3.0), Inches(1.5 + row * 1.45), Inches(2.85), Inches(1.35))
        card.fill.solid()
        card.fill.fore_color.rgb = c_white
        card.line.color.rgb = c_card_border
        tf = card.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = "✓ " + pt_text
        pt.font.name = font_main
        pt.font.size = Pt(12)
        pt.font.bold = True
        pt.font.color.rgb = c_blue
        pd = tf.add_paragraph()
        pd.text = pd_text
        pd.font.name = font_body
        pd.font.size = Pt(10)
        pd.font.color.rgb = c_text_muted

    evol_img = os.path.join(assets_dir, "talent_evolution_chart.png")
    if os.path.exists(evol_img):
        s2.shapes.add_picture(evol_img, Inches(6.7), Inches(4.4), width=Inches(5.85))

    add_footer(s2, 2)

    # ==========================================
    # SLIDE 3: NUESTRA EXPERIENCIA (CUENTAS VERIFICADAS TELAT)
    # ==========================================
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Nuestra Experiencia Comprobada", "Sectores Consolidados & Casos de Éxito")

    verified_sectors = [
        ("Automotriz y Flotillas", "ORO IMT 2026", [
            "• Marcas líderes de comercio automotriz en EE. UU. (Oro IMT 2026 & Plata 2023)",
            "• Redes nacionales de servicios vehiculares y cristales (Bronce IMT 2025)",
            "• Arrendadoras líderes de flotillas corporativas y telemetría"
        ]),
        ("Telecomunicaciones", "BRONCE IMT 2024", [
            "• Corporativos líderes de conectividad y dispositivos en EE. UU.",
            "• Proveedores globales de soluciones de videovigilancia con IA",
            "• Diagnóstico remoto de red y soporte técnico bilingüe 24/7"
        ]),
        ("Comercio Digital y Retail", "MERCADO EE. UU.", [
            "• Marcas líderes de comercio electrónico personalizado en EE. UU.",
            "• Campañas estacionales de alto volumen y venta adicional",
            "• Programas de lealtad, retención y atención a socios"
        ]),
        ("Salud y Farmacéutico", "SECTOR SALUD EE. UU.", [
            "• Organizaciones líderes de beneficios farmacéuticos en EE. UU.",
            "• Redes de farmacias, validación de coberturas y asistencia 24/7",
            "• Gestión de citas y orientación médica telefónica bilingüe"
        ]),
        ("Servicios y Logística", "BPO INTEGRAL", [
            "• Corporativos líderes en logística aduanal y transporte intermodal",
            "• Programas de orientación ciudadana e institucional masiva",
            "• Mesas de ayuda y seguimiento documental de extremo a extremo"
        ]),
        ("Sector Financiero", "PCI DSS v4.0", [
            "• Instituciones líderes de banca, seguros y tecnología financiera",
            "• Cobranza preventiva y validación de identidad",
            "• Procesamiento de pagos seguro certificado bajo PCI DSS v4.0"
        ])
    ]

    for idx, (sec_name, sec_badge, bullets) in enumerate(verified_sectors):
        col = idx % 3
        row = idx // 3
        left = Inches(0.7 + col * 4.05)
        top = Inches(1.5 + row * 2.65)

        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.8), Inches(2.45))
        card.fill.solid()
        card.fill.fore_color.rgb = c_white
        card.line.color.rgb = c_card_border

        t_box = s3.shapes.add_textbox(left + Inches(0.15), top + Inches(0.12), Inches(3.5), Inches(2.2))
        tf_s = t_box.text_frame
        tf_s.word_wrap = True
        p_t = tf_s.paragraphs[0]
        p_t.text = f"{sec_name}  [{sec_badge}]"
        p_t.font.name = font_main
        p_t.font.size = Pt(13)
        p_t.font.bold = True
        p_t.font.color.rgb = c_navy

        for b_line in bullets:
            pb = tf_s.add_paragraph()
            pb.text = "\n" + b_line
            pb.font.name = font_body
            pb.font.size = Pt(10.5)
            pb.font.color.rgb = c_text_dark

    add_footer(s3, 3)

    # ==========================================
    # SLIDE 4: UBICACIONES (MAPA VISUAL CON ESTRELLAS + 4 SEDES)
    # ==========================================
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "Ubicaciones & Presencia Binacional", "Infraestructura Física")

    mapa_path = os.path.join(assets_dir, "mapa_hubs_starred.png")
    if os.path.exists(mapa_path):
        s4.shapes.add_picture(mapa_path, Inches(0.7), Inches(1.5), width=Inches(5.8))

    hubs = [
        ("CDMX · Sede Insurgentes", "Av. Insurgentes Sur 263, Col. Roma", "Centro Corporativo y Operativo"),
        ("CDMX · Sede Monterrey", "Calle Monterrey 149, Col. Roma", "Centro Operativo Principal"),
        ("Ciudad Juárez, Chih.", "Chihuahua · Centro Bilingüe", "Operación Bilingüe Fronteriza"),
        ("El Paso, Texas, EE. UU.", "Sede Binacional EE. UU.", "Centro Operativo en EE. UU.")
    ]
    for idx, (h_title, h_sub, h_st) in enumerate(hubs):
        col = idx % 2
        row = idx // 2
        left = Inches(6.8 + col * 2.95)
        top = Inches(1.5 + row * 2.0)

        card = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.8), Inches(1.85))
        card.fill.solid()
        card.fill.fore_color.rgb = c_white
        card.line.color.rgb = c_card_border
        tf = card.text_frame
        tf.word_wrap = True

        pt = tf.paragraphs[0]
        pt.text = h_title
        pt.font.name = font_main
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = c_text_dark

        ps = tf.add_paragraph()
        ps.text = h_sub
        ps.font.name = font_body
        ps.font.size = Pt(10)
        ps.font.color.rgb = c_text_muted

        pst = tf.add_paragraph()
        pst.text = "\n" + h_st
        pst.font.name = font_main
        pst.font.size = Pt(11.5)
        pst.font.bold = True
        pst.font.color.rgb = c_orange

    strip4 = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(5.6), Inches(5.75), Inches(1.1))
    strip4.fill.solid()
    strip4.fill.fore_color.rgb = c_slate_dark
    strip4.line.color.rgb = c_slate_dark
    ps4 = strip4.text_frame.paragraphs[0]
    ps4.alignment = PP_ALIGN.CENTER
    ps4.text = "4 CENTROS OPERATIVOS  |  650 COLABORADORES + IA  |  24/7 REDUNDANCIA BINACIONAL"
    ps4.font.name = font_main
    ps4.font.size = Pt(11)
    ps4.font.bold = True
    ps4.font.color.rgb = c_yellow

    add_footer(s4, 4)

    # ==========================================
    # SLIDE 5: SOLUCIONES INTEGRALES (ESPEJO DE LUIS)
    # ==========================================
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Soluciones Integrales", "Tecnología y Diferenciadores")

    sub5 = s5.shapes.add_textbox(Inches(0.7), Inches(1.35), Inches(11.8), Inches(0.45))
    ps5 = sub5.text_frame.paragraphs[0]
    ps5.text = "Nuestra tecnología puede ser aplicada en cualquier sector empresarial con el fin de hacer más competitiva y eficiente la actividad de la empresa."
    ps5.font.name = font_body
    ps5.font.size = Pt(12.5)
    ps5.font.color.rgb = c_text_muted

    items_s5 = [
        "01. Software integrado con nuestros aliados",
        "02. Equipo de desarrollo, operaciones y soporte local",
        "03. BCP (Business Continuity Plan)",
        "04. Continuidad de negocio con respaldo internacional",
        "05. Gran estabilidad del servicio (99.99% Uptime)",
        "06. Avalado por más de 20 años de experiencia en plataformas SaaS",
        "07. Fondo de inversión",
        "08. Innovación continua (On demand)",
        "09. Atención Omnicanal (Voz, WhatsApp, Chat, Correo, Redes)",
        "10. CRM & Integración Nativa via API / Webhooks",
        "11. Las soluciones de IA · Speech & Text Analytics y Auditoría QA 100%",
        "12. Chatbots, Copiloto en Tiempo Real & Automatización"
    ]

    list_box = s5.shapes.add_textbox(Inches(0.7), Inches(1.85), Inches(7.3), Inches(4.4))
    tf_list = list_box.text_frame
    tf_list.word_wrap = True
    for idx, line in enumerate(items_s5):
        p = tf_list.paragraphs[0] if idx == 0 else tf_list.add_paragraph()
        p.text = line
        p.font.name = font_main
        p.font.size = Pt(12.5)
        p.font.bold = True
        p.font.color.rgb = c_orange if idx == 10 else c_text_dark
        p.space_after = Pt(3.5)

    ai_img = os.path.join(assets_dir, "slide5_ai_visual.png")
    if os.path.exists(ai_img):
        s5.shapes.add_picture(ai_img, Inches(8.1), Inches(1.85), width=Inches(4.5))

    partner_strip = os.path.join(assets_dir, "partner_logos_strip.png")
    if os.path.exists(partner_strip):
        s5.shapes.add_picture(partner_strip, Inches(0.7), Inches(6.25), width=Inches(11.933))

    add_footer(s5, 5)

    # ==========================================
    # SLIDE 6: NUESTRA INFRAESTRUCTURA (DIAGRAMA DE RED HD)
    # ==========================================
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Nuestra Infraestructura", "Arquitectura de Interconexión")

    net_img = os.path.join(assets_dir, "network_diagram_hd.png")
    if os.path.exists(net_img):
        s6.shapes.add_picture(net_img, Inches(0.7), Inches(1.45), width=Inches(7.8))

    spec_card = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(8.7), Inches(1.45), Inches(3.9), Inches(5.3))
    spec_card.fill.solid()
    spec_card.fill.fore_color.rgb = c_slate_dark
    spec_card.line.color.rgb = c_orange
    spec_card.line.width = Pt(2)
    tf_sp = spec_card.text_frame
    tf_sp.word_wrap = True

    p_st = tf_sp.paragraphs[0]
    p_st.text = "CONECTIVIDAD CON SOCIOS ESTRATÉGICOS"
    p_st.font.name = font_main
    p_st.font.size = Pt(14)
    p_st.font.bold = True
    p_st.font.color.rgb = c_yellow

    specs = [
        "• Enlaces dedicados redundantes entre CDMX (Insurgentes & Monterrey), Cd. Juárez y El Paso, TX.",
        "• Interconexión directa con Data Centers en Houston / Dallas y KIO Querétaro.",
        "• Disponibilidad de Red: 99.99% Uptime.",
        "• Firewalls y Switches en Alta Disponibilidad (HA).",
        "• Segmentación por VLANs privadas dedicadas a la campaña UVC."
    ]
    for sp in specs:
        p = tf_sp.add_paragraph()
        p.text = "\n" + sp
        p.font.name = font_body
        p.font.size = Pt(11.5)
        p.font.color.rgb = c_white

    add_footer(s6, 6)

    # ==========================================
    # SLIDE 7: SEGURIDAD EN INFORMACIÓN - PCI DSS
    # ==========================================
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Seguridad en Información – PCI DSS", "Blindaje Transaccional")

    banner7 = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(1.45), Inches(11.933), Inches(1.15))
    banner7.fill.solid()
    banner7.fill.fore_color.rgb = c_navy
    banner7.line.color.rgb = c_blue
    tf_b7 = banner7.text_frame
    tf_b7.word_wrap = True
    pb7 = tf_b7.paragraphs[0]
    pb7.text = "SISTEMAS AVANZADOS DE SEGURIDAD & PROTECCIÓN DE PAGOS UVC"
    pb7.font.name = font_main
    pb7.font.size = Pt(15)
    pb7.font.bold = True
    pb7.font.color.rgb = c_yellow
    pb7_2 = tf_b7.add_paragraph()
    pb7_2.text = "Transferencia y procesamiento seguro de pagos bajo cumplimiento PCI DSS, garantizando cero exposición de datos sensibles de socios."
    pb7_2.font.name = font_body
    pb7_2.font.size = Pt(12)
    pb7_2.font.color.rgb = c_white

    sec_items = [
        ("Identificación", "Control de acceso biométrico en sitio y trazabilidad individual de cada asesor."),
        ("Autenticación", "Validación multifactor (MFA) y políticas estrictas en Active Directory."),
        ("Encripción End-to-End", "Cifrado punto a punto en voz, pantallas y bases de datos transaccionales."),
        ("BCP (Business Continuity)", "Plan de continuidad del negocio certificado bajo norma ISO 22301."),
        ("DRP (Disaster Recovery)", "Plan de recuperación ante desastres con redundancia en nuestras 4 sedes."),
        ("PCI DSS Compliance", "Transferencia segura de pagos sin almacenamiento de CVV ni captura en audio.")
    ]
    for idx, (st, sd) in enumerate(sec_items):
        col = idx % 3
        row = idx // 3
        left = Inches(0.7 + col * 4.05)
        top = Inches(2.85 + row * 1.95)

        card = s7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.8), Inches(1.8))
        card.fill.solid()
        card.fill.fore_color.rgb = c_white
        card.line.color.rgb = c_card_border
        tf = card.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = "🔒 " + st
        pt.font.name = font_main
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = c_navy
        pd = tf.add_paragraph()
        pd.text = "\n" + sd
        pd.font.name = font_body
        pd.font.size = Pt(11)
        pd.font.color.rgb = c_text_muted

    add_footer(s7, 7)

    # ==========================================
    # SLIDE 8: NUESTRAS CERTIFICACIONES (CON MODELO GLOBAL CIC GRANDE)
    # ==========================================
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Nuestras Certificaciones & Modelo Global CIC", "Respaldo Auditado")

    certs = [
        ("cert_modelo_cic.png", "Modelo Global CIC", "Excelencia en Centros de Contacto"),
        ("cert_pci_dss.png", "PCI DSS Compliance", "Seguridad de Datos de Tarjetas"),
        ("cert_iso_27001.png", "ISO 27001", "Seguridad de la Información"),
        ("cert_iso_22301.png", "ISO 22301", "Continuidad del Negocio (BCP)"),
        ("cert_iso_9001.png", "ISO 9001", "Gestión de la Calidad"),
        ("cert_iso_20000.png", "ISO 20000-1", "Calidad en Servicios de TI"),
        ("cert_iso_37001.png", "ISO 37001", "Sistema Antisoborno"),
        ("cert_iso_18295.png", "ISO 18295-1", "Operación de Contact Centers"),
        ("cert_esr_2026.png", "ESR & Premios IMT", "Responsabilidad Social y Excelencia")
    ]

    for idx, (img_file, cname, csub) in enumerate(certs):
        col = idx % 3
        row = idx // 3
        left = Inches(0.7 + col * 4.05)
        top = Inches(1.45 + row * 1.8)

        card = s8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(3.8), Inches(1.65))
        card.fill.solid()
        card.fill.fore_color.rgb = c_navy if idx == 0 else c_white
        card.line.color.rgb = c_orange if idx == 0 else c_card_border
        card.line.width = Pt(2) if idx == 0 else Pt(1)

        img_path = os.path.join(cert_dir, img_file)
        if os.path.exists(img_path):
            s8.shapes.add_picture(img_path, left + Inches(0.18), top + Inches(0.22), height=Inches(1.15))

        tb = s8.shapes.add_textbox(left + Inches(1.45), top + Inches(0.25), Inches(2.25), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        pt = tf.paragraphs[0]
        pt.text = cname
        pt.font.name = font_main
        pt.font.size = Pt(14)
        pt.font.bold = True
        pt.font.color.rgb = c_yellow if idx == 0 else c_text_dark

        ps = tf.add_paragraph()
        ps.text = csub
        ps.font.name = font_body
        ps.font.size = Pt(10.5)
        ps.font.color.rgb = c_white if idx == 0 else c_text_muted

    add_footer(s8, 8)

    # ==========================================
    # SLIDE 9: POR QUÉ CONTRATAR TELAT
    # ==========================================
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "¿Por Qué Contratar los Servicios de Telat?", "Valor Diferencial")

    reasons = [
        ("20+ Años", "Experiencia BPO", "Especialistas en campañas complejas orientadas a maximizar resultados."),
        ("24 / 7", "Presencia Binacional", "Operación continua en CDMX, Ciudad Juárez y El Paso, Texas."),
        ("9 Sellos", "Certificaciones & CIC", "Modelo Global CIC, PCI DSS, ISO 27001, 22301, 9001, 20000 y 37001."),
        ("100% IA", "Speech & Text Analytics", "Inteligencia artificial para mejorar decisiones comerciales y de servicio."),
        ("360°", "Omnicanalidad", "Atención integrada por Voz, Chat, WhatsApp, redes sociales y correo."),
        ("BCP/DRP", "Continuidad Garantizada", "Respaldo operativo total ante cualquier circunstancia ajena."),
        ("Flex", "Desborde de Llamadas", "Capacidad inmediata ante situaciones atípicas de alto tráfico."),
        ("ROI", "Precios Competitivos", "Nos adaptamos al tamaño de su operación con costos altamente rentables.")
    ]
    for idx, (rk, rt, rd) in enumerate(reasons):
        col = idx % 4
        row = idx // 4
        left = Inches(0.7 + col * 3.02)
        top = Inches(1.45 + row * 2.05)

        card = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, Inches(2.85), Inches(1.9))
        card.fill.solid()
        card.fill.fore_color.rgb = c_white
        card.line.color.rgb = c_card_border
        tf = card.text_frame
        tf.word_wrap = True

        pk = tf.paragraphs[0]
        pk.text = rk
        pk.font.name = font_main
        pk.font.size = Pt(20)
        pk.font.bold = True
        pk.font.color.rgb = c_orange

        pt = tf.add_paragraph()
        pt.text = rt
        pt.font.name = font_main
        pt.font.size = Pt(13)
        pt.font.bold = True
        pt.font.color.rgb = c_navy

        pd = tf.add_paragraph()
        pd.text = rd
        pd.font.name = font_body
        pd.font.size = Pt(10)
        pd.font.color.rgb = c_text_muted

    strip9 = s9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(5.65), Inches(11.933), Inches(1.15))
    strip9.fill.solid()
    strip9.fill.fore_color.rgb = c_slate_dark
    strip9.line.color.rgb = c_slate_dark

    imt_logo_path = os.path.join(cert_dir, "logo_imt.png")
    if os.path.exists(imt_logo_path):
        s9.shapes.add_picture(imt_logo_path, Inches(0.95), Inches(5.82), height=Inches(0.8))

    tb_s9 = s9.shapes.add_textbox(Inches(2.9), Inches(5.78), Inches(9.5), Inches(0.9))
    tf_s9 = tb_s9.text_frame
    ps9 = tf_s9.paragraphs[0]
    ps9.text = "RECONOCIDOS EN MÉXICO Y LATAM POR 4TO AÑO CONSECUTIVO (IMT)"
    ps9.font.name = font_main
    ps9.font.size = Pt(14)
    ps9.font.bold = True
    ps9.font.color.rgb = c_yellow
    ps9_2 = tf_s9.add_paragraph()
    ps9_2.text = "Galardonados en Customer Experience por la operación de las mejores campañas offshore."
    ps9_2.font.name = font_body
    ps9_2.font.size = Pt(11.5)
    ps9_2.font.color.rgb = c_white

    add_footer(s9, 9)

    # ==========================================
    # SLIDE 10: PROPUESTA DE INVERSIÓN · UVC
    # ==========================================
    s10 = prs.slides.add_slide(blank_layout)
    add_header(s10, "Propuesta de Inversión · UVC", "Condiciones Económicas Formales")

    rates = [
        ("Costo por Hora Staffed Time", "$17.30 USD", "Por hora · Incluye telefonía outbound", c_blue),
        ("Costo por Hora Capacitación", "$15.00 USD", "Por hora · Formación especializada UVC", c_orange),
        ("Presupuesto Mensual", "$350,575 USD", "Facturación mensual según Sistema ACD", c_navy),
        ("Presupuesto Anual", "$4,206,889 USD", "Proyección anual de operación dedicada", c_slate_dark)
    ]
    for idx, (rt_title, rt_val, rt_sub, border_c) in enumerate(rates):
        left = Inches(0.7 + idx * 3.02)
        card = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, Inches(1.45), Inches(2.85), Inches(1.85))
        card.fill.solid()
        card.fill.fore_color.rgb = c_white if idx < 2 else c_navy
        card.line.color.rgb = border_c
        card.line.width = Pt(2)
        tf = card.text_frame
        tf.word_wrap = True

        pt = tf.paragraphs[0]
        pt.text = rt_title
        pt.font.name = font_main
        pt.font.size = Pt(11)
        pt.font.bold = True
        pt.font.color.rgb = c_text_muted if idx < 2 else c_sky

        pv = tf.add_paragraph()
        pv.text = "\n" + rt_val
        pv.font.name = font_main
        pv.font.size = Pt(22)
        pv.font.bold = True
        pv.font.color.rgb = c_text_dark if idx < 2 else c_yellow

        ps = tf.add_paragraph()
        ps.text = rt_sub
        ps.font.name = font_body
        ps.font.size = Pt(9.5)
        ps.font.color.rgb = c_text_muted if idx < 2 else c_white

    card_ops = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(3.5), Inches(5.8), Inches(2.2))
    card_ops.fill.solid()
    card_ops.fill.fore_color.rgb = c_white
    card_ops.line.color.rgb = c_card_border
    tf_ops = card_ops.text_frame
    tf_ops.word_wrap = True
    p_opst = tf_ops.paragraphs[0]
    p_opst.text = "IMPLEMENTACIÓN: RECURSOS 100% DEDICADOS"
    p_opst.font.name = font_main
    p_opst.font.size = Pt(13)
    p_opst.font.bold = True
    p_opst.font.color.rgb = c_blue

    for item in [
        "✓ Agentes 100% Dedicados a la campaña UVC",
        "✓ Supervisores: Dedicados",
        "✓ Workforce Management (WFM): Dedicado",
        "✓ Auditoría QA con Inteligencia Artificial: Dedicada",
        "✓ Trainer de campaña: Dedicado"
    ]:
        p = tf_ops.add_paragraph()
        p.text = item
        p.font.name = font_body
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = c_text_dark

    card_sc = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.7), Inches(3.5), Inches(5.933), Inches(2.2))
    card_sc.fill.solid()
    card_sc.fill.fore_color.rgb = c_white
    card_sc.line.color.rgb = c_card_border
    tf_sc = card_sc.text_frame
    tf_sc.word_wrap = True
    p_sct = tf_sc.paragraphs[0]
    p_sct.text = "ALCANCE INCLUIDO & CONSIDERACIONES"
    p_sct.font.name = font_main
    p_sct.font.size = Pt(13)
    p_sct.font.bold = True
    p_sct.font.color.rgb = c_blue

    for item in [
        "• Precio por hora Staffed: ACD In/Out, ACW, Hold, Available, Lunch Time y Auxiliares (Fuente: Sistema ACD).",
        "• Estación de trabajo con PC, teléfono, diadema, mobiliario e infraestructura Telat.",
        "• Reportes de productividad y dashboard de campaña en vivo.",
        "• Solución escalable de acuerdo con el volumen de llamadas."
    ]:
        p = tf_sc.add_paragraph()
        p.text = item
        p.font.name = font_body
        p.font.size = Pt(10.5)
        p.font.color.rgb = c_text_dark

    strip10 = s10.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.7), Inches(5.9), Inches(11.933), Inches(0.95))
    strip10.fill.solid()
    strip10.fill.fore_color.rgb = c_slate_dark
    strip10.line.color.rgb = c_blue
    tf_s10 = strip10.text_frame
    tf_s10.word_wrap = True
    ps10 = tf_s10.paragraphs[0]
    ps10.text = "⚖️  CONDICIONES FISCALES: Precios expresados en USD. Aplica IVA en facturación dentro de la República Mexicana; exento de impuestos locales (Net / Zero-Tax) para facturación corporativa directa en Estados Unidos."
    ps10.font.name = font_body
    ps10.font.size = Pt(11.5)
    ps10.font.bold = True
    ps10.font.color.rgb = c_white

    add_footer(s10, 10)

    # ==========================================
    # SLIDE 11: CIERRE EJECUTIVO (LOGOS GIGANTES + LUIS CORTINA)
    # ==========================================
    s11 = prs.slides.add_slide(blank_layout)
    bg11 = s11.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
    bg11.fill.solid()
    bg11.fill.fore_color.rgb = c_navy_dark
    bg11.line.color.rgb = c_navy_dark

    # Giant Center Co-Branding Card
    hero_box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(1.0), Inches(10.333), Inches(2.8))
    hero_box.fill.solid()
    hero_box.fill.fore_color.rgb = RGBColor(20, 32, 60)
    hero_box.line.color.rgb = c_orange
    hero_box.line.width = Pt(2)

    if os.path.exists(logo_telat):
        s11.shapes.add_picture(logo_telat, Inches(2.5), Inches(1.5), height=Inches(1.8))

    tb_x = s11.shapes.add_textbox(Inches(5.5), Inches(1.9), Inches(1.5), Inches(1.0))
    px = tb_x.text_frame.paragraphs[0]
    px.alignment = PP_ALIGN.CENTER
    px.text = "×"
    px.font.name = font_main
    px.font.size = Pt(44)
    px.font.bold = True
    px.font.color.rgb = c_yellow

    if os.path.exists(logo_uvc_dark):
        s11.shapes.add_picture(logo_uvc_dark, Inches(7.2), Inches(1.75), height=Inches(1.3))

    # Message
    msg_box = s11.shapes.add_textbox(Inches(1.0), Inches(4.05), Inches(11.333), Inches(1.1))
    tf_m = msg_box.text_frame
    tf_m.word_wrap = True
    pm1 = tf_m.paragraphs[0]
    pm1.alignment = PP_ALIGN.CENTER
    pm1.text = "Listos para Impulsar la Experiencia de los Socios de Unlimited Vacation Club"
    pm1.font.name = font_main
    pm1.font.size = Pt(24)
    pm1.font.bold = True
    pm1.font.color.rgb = c_white

    pm2 = tf_m.add_paragraph()
    pm2.alignment = PP_ALIGN.CENTER
    pm2.text = "Personal 100% dedicado, tecnología con Inteligencia Artificial e infraestructura binacional a su servicio."
    pm2.font.name = font_body
    pm2.font.size = Pt(14)
    pm2.font.color.rgb = RGBColor(203, 213, 225)

    # Exclusive Contact Box: Luis Cortina
    sign_box = s11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.5), Inches(5.35), Inches(10.333), Inches(1.4))
    sign_box.fill.solid()
    sign_box.fill.fore_color.rgb = RGBColor(15, 23, 42)
    sign_box.line.color.rgb = RGBColor(51, 65, 85)
    tf_sb = sign_box.text_frame
    tf_sb.word_wrap = True

    psb1 = tf_sb.paragraphs[0]
    psb1.alignment = PP_ALIGN.CENTER
    psb1.text = "REPRESENTACIÓN INSTITUCIONAL · TELAT GROUP"
    psb1.font.name = font_main
    psb1.font.size = Pt(10)
    psb1.font.bold = True
    psb1.font.color.rgb = c_yellow

    psb2 = tf_sb.add_paragraph()
    psb2.alignment = PP_ALIGN.CENTER
    psb2.text = "Luis Cortina — Apoderado Legal"
    psb2.font.name = font_main
    psb2.font.size = Pt(18)
    psb2.font.bold = True
    psb2.font.color.rgb = c_white

    psb3 = tf_sb.add_paragraph()
    psb3.alignment = PP_ALIGN.CENTER
    psb3.text = "contacto@telat-group.com   |   www.telat-group.com   |   CDMX · Ciudad Juárez · El Paso, TX"
    psb3.font.name = font_body
    psb3.font.size = Pt(11)
    psb3.font.color.rgb = c_sky

    add_footer(s11, 11, dark=True)

    prs.save(output_pptx)
    print(f"PPTX generado exitosamente: {output_pptx}")
    try:
        shutil.copy2(output_pptx, downloads_pptx)
        print(f"PPTX copiado a Descargas: {downloads_pptx}")
    except PermissionError:
        alt_pptx = os.path.join(os.environ["USERPROFILE"], "Downloads", "Propuesta_Comercial_UVC_Unlimited_Vacation_Club_Telat_v2.pptx")
        shutil.copy2(output_pptx, alt_pptx)
        print(f"Archivo original abierto en PowerPoint; copiado a Descargas como: {alt_pptx}")

if __name__ == "__main__":
    create_presentation()
