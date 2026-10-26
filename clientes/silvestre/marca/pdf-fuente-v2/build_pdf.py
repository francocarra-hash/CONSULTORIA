import base64, os
H = os.path.dirname(os.path.abspath(__file__))
def b64(p, m): return f"data:{m};base64," + base64.b64encode(open(os.path.join(H, p), "rb").read()).decode()
SVG = lambda n: b64(f"kit/logo-{n}.svg", "image/svg+xml")
LH, LA = SVG("horizontal"), SVG("apilado")
LHB, LAB = SVG("horizontal-blanco"), SVG("apilado-blanco")
LHN, LAN = SVG("horizontal-negro"), SVG("apilado-negro")
BOSQUE = b64("kit/bosque-kit.jpg", "image/jpeg")
HARABARA = b64("kit/harabara-alpha.png", "image/png")
P = {k: b64(f"img/{k}.png", "image/png") for k in ["ms162", "ms194t", "mse141", "bge71", "hse61", "fs"]}
SH = {k: b64(f"shots/{k}.jpg", "image/jpeg") for k in ["m-desk-top", "m-mob-0", "m-mob-1", "m-mob-2"]}
FT = b64("fonts/Montserrat.woff2", "font/woff2")

def ic(d, c="ic"): return f'<svg class="{c}" viewBox="0 0 24 24" aria-hidden="true">{d}</svg>'
I = {
 "camion": ic('<path d="M2.5 6.5h11v9h-11z"/><path d="M13.5 9.5h4l3 3.2v2.8h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'),
 "local": ic('<path d="M3.5 10l1.5-5.5h14L20.5 10"/><path d="M3.5 10c0 1.7 1.3 2.8 2.9 2.8S9.3 11.7 9.3 10c0 1.7 1.3 2.8 2.7 2.8s2.7-1.1 2.7-2.8c0 1.7 1.3 2.8 2.9 2.8s2.9-1.1 2.9-2.8"/><path d="M5 12.6V20h14v-7.4"/><path d="M10 20v-4.5h4V20"/>'),
 "cuotas": ic('<rect x="2.5" y="5.5" width="19" height="13" rx="2"/><path d="M2.5 9.5h19"/><path d="M6 15h4"/>'),
 "escudo": ic('<path d="M12 3l7.5 3v5.5c0 4.6-3.2 8.2-7.5 9.5-4.3-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.8 12.2l2.2 2.2 4.2-4.4"/>'),
 "llave": ic('<path d="M14.5 6.5a4 4 0 0 0 5 5L13 18a2.1 2.1 0 0 1-3-3l6.5-6.5"/><path d="M14.5 6.5L17 4l3 3-2.5 2.5"/>'),
 "chat": ic('<path d="M4.5 19.5l1.2-3.6A7.5 7.5 0 1 1 8.6 18.6z"/><path d="M9.2 9.5c.3 2 2.3 4.1 4.6 4.6l1-1.1 1.8.8c-.2 1.2-1.2 1.9-2.3 1.7-3-.5-5.6-3.1-6-6-.2-1.1.5-2.1 1.7-2.3l.8 1.8z"/>'),
 "bateria": ic('<rect x="3" y="7.5" width="16" height="9" rx="2"/><path d="M21 10.5v3"/><path d="M11.5 9l-2 3h3l-2 3"/>'),
 "nafta": ic('<path d="M5 20V5.5A1.5 1.5 0 0 1 6.5 4h7A1.5 1.5 0 0 1 15 5.5V20"/><path d="M3.5 20h13"/><path d="M7.5 7.5h5v4h-5z"/><path d="M15 9.5h2a1.5 1.5 0 0 1 1.5 1.5v5a1.5 1.5 0 0 0 3 0V8l-2.5-2.5"/>'),
 "rayo": ic('<path d="M13 2.5L5 13.5h6l-1 8 8-11h-6z"/>'),
 "lupa": ic('<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>'),
 "usuario": ic('<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c1.2-3.8 4-5.5 7.5-5.5s6.3 1.7 7.5 5.5"/>'),
 "carrito": ic('<path d="M3 4h2.5l2.2 11h10.6l2-8H7"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>'),
 "hoja": ic('<path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14z"/><path d="M5 19l7-7"/>'),
 "flecha": ic('<path d="M5 12h14M13 6l6 6-6 6"/>'),
 "camara": ic('<path d="M4 8h3l1.5-2.5h7L17 8h3v11H4z"/><circle cx="12" cy="13.2" r="3.4"/>'),
 "pin": ic('<path d="M12 21s-6.5-5.6-6.5-11a6.5 6.5 0 0 1 13 0c0 5.4-6.5 11-6.5 11z"/><circle cx="12" cy="10" r="2.3"/>'),
 "si": ic('<path d="M5 12.5l4.5 4.5L19 7.5"/>', "ok"),
 "no": ic('<path d="M6 6l12 12M18 6L6 18"/>', "ko"),
}

def pg(body, cls="", num=None, cap="", dark=False, half=False):
    f = "" if num is None else f'<footer class="folio{" folio--d" if dark else ""}{" folio--half" if half else ""}"><span>Silvestre — Manual de marca</span><span>{cap}</span><span class="n">{num:02d}</span></footer>'
    return f'<section class="page {cls}">{body}{f}</section>'

def head(ch, title, lead=""):
    l = f'<p class="lead">{lead}</p>' if lead else ""
    return f'<header class="hd"><span class="ch">{ch}</span><h2>{title}</h2>{l}</header>'

def slot(title, spec, cls=""):
    return f'<figure class="slot {cls}">{I["camara"]}<figcaption><b>{title}</b><span>{spec}</span></figcaption></figure>'

pages = []

# 01 Portada
pages.append(pg(f'''
<div class="cover" style="background-image:url({BOSQUE})"><div class="grain"></div>
  <img class="cover-logo" src="{LAB}" alt="Silvestre máquinas y jardines">
  <div class="cover-foot"><span>Manual de marca</span><span>Tienda online · Edición 2026</span></div>
</div>''', "full"))

# 02 Índice
idx = [("01","La marca","03"),("02","Logo","05"),("03","Color","08"),("04","Tipografía","10"),("05","Fotografía","11"),("06","Interfaz","12"),("07","La tienda online","13"),("08","Marcas","15")]
pages.append(pg(f'''
<div class="idx">
  <div class="idx-a" style="background-image:url({BOSQUE})"><div class="tint"></div><img src="{LHB}" alt=""></div>
  <div class="idx-b"><span class="ch">Contenido</span>
    <ol>{"".join(f'<li><span class="i-n">{n}</span><span class="i-t">{t}</span><span class="i-p">{p}</span></li>' for n,t,p in idx)}</ol>
  </div>
</div>''', "full", 2, "Contenido"))

# 03 Marca: apertura
pages.append(pg(f'''
<div class="open">
  <div class="open-txt">
    <span class="ch">01 · La marca</span>
    <h1>Máquinas para tu jardín y tu campo, con el asesoramiento de quien las conoce.</h1>
    <p class="lead">Silvestre es una casa especializada en máquinas y herramientas para jardín, parque y campo en Maipú, Mendoza. Distribuidor oficial STIHL y multimarca.</p>
  </div>
  <div class="open-img" style="background-image:url({BOSQUE})"><div class="grain"></div></div>
</div>''', "full", 3, "La marca", half=True))

# 04 Pilares y personalidad
pil = [("01","Especialistas","Te ayudamos a elegir la máquina justa para tu terreno y tu uso."),
       ("02","Garantía oficial","Distribuidor oficial STIHL y marcas líderes. Siempre original."),
       ("03","Repuestos y servicio","No te dejamos solo después de la compra."),
       ("04","Cerca tuyo","Envíos a todo el país y retiro en nuestro local de Maipú.")]
pers = [("Experto","no técnico"),("Claro","no complicado"),("Cercano","no informal"),("Honesto","no vendedor a cualquier costo")]
pages.append(pg(f'''
<div class="pad">
  {head("01 · La marca", "Cuatro razones para comprarnos")}
  <div class="pilares">{"".join(f'<div class="pil"><span class="pil-n">{n}</span><h3>{t}</h3><p>{d}</p></div>' for n,t,d in pil)}</div>
  <div class="pers"><span class="ch">Personalidad</span><div class="pers-row">{"".join(f'<div class="pr"><b>{a}</b><span>{b}</span></div>' for a,b in pers)}</div></div>
</div>''', "", 4, "La marca"))

# 05 Logo principal
pages.append(pg(f'''
<div class="pad">
  {head("02 · Logo", "Logo principal", "Dos versiones: horizontal para la web y documentos, apilada para espacios cuadrados.")}
  <div class="lg2">
    <div class="lg-card"><img class="lg-h" src="{LH}" alt=""><span class="tag-c">Horizontal</span></div>
    <div class="lg-card"><img class="lg-a" src="{LA}" alt=""><span class="tag-c">Apilada</span></div>
  </div>
  <div class="anat">
    <div><i style="background:var(--naranja)"></i><b>SIL · TRE</b><span>Naranja #F29100</span></div>
    <div><i style="background:var(--verde)"></i><b>VES · rama · bajada</b><span>Verde #39A935</span></div>
    <div><i style="background:var(--texto)"></i><b>Tipografía</b><span>Harabara Mais</span></div>
  </div>
</div>''', "", 5, "Logo"))

# 06 Área de respeto y tamaños
pages.append(pg(f'''
<div class="pad">
  {head("02 · Logo", "Área de respeto y tamaño mínimo")}
  <div class="resp-grid">
    <div class="resp">
      <div class="resp-box"><img src="{LH}" alt=""><i class="x x-t">x</i><i class="x x-b">x</i><i class="x x-l">x</i><i class="x x-r">x</i></div>
      <p class="cap">x = alto de la letra “s”. Nada entra en esa zona: textos, bordes ni otras marcas.</p>
    </div>
    <div class="mins">
      <div class="min"><img src="{LH}" style="width:140px" alt=""><b>140 px</b><span>Horizontal con bajada · pantalla</span></div>
      <div class="min"><img src="{LH}" style="width:100px;clip-path:inset(0 0 30% 0)" alt=""><b>100 px</b><span>Sin bajada · pantalla</span></div>
      <div class="min"><img src="{LA}" style="height:80px" alt=""><b>80 px de alto</b><span>Apilada · perfil y redes</span></div>
      <div class="min"><img src="{LH}" style="width:120px" alt=""><b>35 mm</b><span>Impreso</span></div>
    </div>
  </div>
</div>''', "", 6, "Logo"))

# 07 Versiones y usos incorrectos
pages.append(pg(f'''
<div class="pad">
  {head("02 · Logo", "Versiones y fondos")}
  <div class="vers">
    <div class="v" style="background:#fff;border:1px solid var(--borde)"><img src="{LH}" alt="">{I["si"]}<span>Color sobre blanco</span></div>
    <div class="v" style="background:var(--verde-claro)"><img src="{LH}" alt="">{I["si"]}<span>Color sobre verde claro</span></div>
    <div class="v" style="background-image:linear-gradient(rgba(20,61,24,.35),rgba(20,61,24,.35)),url({BOSQUE});background-size:cover"><img src="{LHB}" alt="">{I["si"]}<span class="w">Blanco sobre foto</span></div>
    <div class="v" style="background:var(--verde-noche)"><img src="{LHB}" alt="">{I["si"]}<span class="w">Blanco sobre verde</span></div>
    <div class="v" style="background:var(--arena)"><img src="{LH}" alt="">{I["si"]}<span>Color sobre arena</span></div>
    <div class="v" style="background:#fff;border:1px solid var(--borde)"><img src="{LHN}" alt="">{I["si"]}<span>Una tinta</span></div>
  </div>
  <div class="nos">
    <div class="no"><div><img src="{LH}" style="transform:scaleX(1.25)" alt=""></div>{I["no"]}<span>Deformar</span></div>
    <div class="no"><div><img src="{LH}" style="transform:rotate(-10deg)" alt=""></div>{I["no"]}<span>Rotar</span></div>
    <div class="no"><div><img src="{LH}" style="filter:hue-rotate(150deg)" alt=""></div>{I["no"]}<span>Recolorear</span></div>
    <div class="no"><div style="background:var(--naranja)"><img src="{LH}" alt=""></div>{I["no"]}<span>Color sobre naranja</span></div>
    <div class="no"><div><img src="{LH}" style="filter:drop-shadow(3px 4px 3px rgba(0,0,0,.5))" alt=""></div>{I["no"]}<span>Efectos</span></div>
    <div class="no"><div style="background:url({BOSQUE}) center/cover"><img src="{LH}" alt=""></div>{I["no"]}<span>Color sobre foto</span></div>
  </div>
</div>''', "", 7, "Logo"))

# 08 Color principal
sec = [("Salvia","#559E72","85 · 158 · 114",True),("Menta","#93E98B","147 · 233 · 139",True),("Verde claro","#EAF9C7","234 · 249 · 199",True),
       ("Terracota","#C16F1E","193 · 111 · 30",True),("Durazno","#FFAF8D","255 · 175 · 141",True),("Rosa arena","#FFCDBB","255 · 205 · 187",True)]
pages.append(pg(f'''
<div class="col-page">
  <div class="cp cp-v"><span class="ch w">03 · Color</span><div class="cp-info"><h3>Verde Silvestre</h3><p>HEX #39A935<br>RGB 57 · 169 · 53</p><span>Principal</span></div></div>
  <div class="cp cp-n"><div class="cp-info"><h3>Naranja Silvestre</h3><p>HEX #F29100<br>RGB 242 · 145 · 0</p><span>Principal</span></div></div>
  <div class="cp-sec">{"".join(f'<div class="cs" style="background:{h}"><div class="{"d" if dk else "w"}"><b>{n}</b><span>{h}</span><span>{r}</span></div></div>' for n,h,r,dk in sec)}</div>
</div>''', "full"))

# 09 Color en la web
web = [("Verde acción","#2E7D32","Botones y links","w"),("Verde bosque","#1E5A23","Textos sobre claro · foco","w"),("Verde noche","#143D18","Fondos oscuros","w"),
       ("Texto","#1A1A1A","Títulos, textos y precios","w"),("Gris","#5F6368","Textos secundarios","w"),("Arena","#F7F6F2","Fondos de sección","d")]
pairs = [("#1A1A1A","#F29100","7,3",True),("#FFFFFF","#2E7D32","5,1",True),("#1E5A23","#EAF9C7","7,4",True),("#FFFFFF","#143D18","12,3",True),
         ("#FFFFFF","#F29100","2,4",False),("#FFFFFF","#39A935","3,0",False),("#559E72","#EAF9C7","2,9",False),("#FFFFFF","#93E98B","1,5",False)]
pages.append(pg(f'''
<div class="pad">
  {head("03 · Color", "Color en la web", "Los colores de marca identifican. Para botones y textos se usan tonos derivados que se leen bien.")}
  <div class="webc">{"".join(f'<div class="wc"><div class="wc-s" style="background:{h}"></div><b>{n}</b><span>{h}</span><em>{u}</em></div>' for n,h,u,_ in web)}</div>
  <div class="ct-row">{"".join(f'<div class="ct" style="background:{bg};color:{fg}"><span class="aa">Aa</span><span class="r">{r} : 1</span>{I["si"] if ok else I["no"]}</div>' for fg,bg,r,ok in pairs)}</div>
  <div class="prop"><div style="flex:65;background:#fff">Blanco y arena 65 %</div><div style="flex:20;background:var(--verde-noche);color:#fff">Verdes 20 %</div><div style="flex:10;background:var(--naranja)">Naranja 10 %</div><div style="flex:5;background:var(--texto);color:#fff">5</div></div>
</div>''', "", 9, "Color"))

# 10 Tipografía
pages.append(pg(f'''
<div class="typo">
  <div class="ty-a">
    <span class="ch">04 · Tipografía</span>
    <div class="ty-lbl">Tipografía de marca</div>
    <div class="harabara" style="-webkit-mask-image:url({HARABARA});mask-image:url({HARABARA})"></div>
    <p class="ty-note">Harabara Mais · logo, títulos de campaña y piezas gráficas.<br>El kit usa la versión Demo: para uso comercial hace falta la licencia completa.</p>
  </div>
  <div class="ty-b">
    <div class="ty-lbl">Tipografía secundaria</div>
    <div class="helv">Helvetica LT Std</div>
    <p class="ty-note d">Textos, precios y datos. En la web: Helvetica Neue, con Arial como respaldo.</p>
    <div class="ty-lbl" style="margin-top:28px">Títulos en la web</div>
    <div class="mont">Montserrat</div>
    <p class="ty-note d">La misma del kit para rótulos. Gratuita en Google Fonts, reemplaza a Harabara en pantalla.</p>
    <div class="scale">
      <div><span class="s1">Máquinas para tu jardín</span><em>H1 · 56</em></div>
      <div><span class="s2">Motosierras y poda</span><em>H2 · 36</em></div>
      <div><span class="s3">$ 389.900</span><em>Precio · 22</em></div>
      <div><span class="s4">6 cuotas sin interés de $ 64.983</span><em>Texto · 14</em></div>
    </div>
  </div>
</div>''', "full", 10, "Tipografía"))

# 11 Fotografía
pages.append(pg(f'''
<div class="pad">
  {head("05 · Fotografía", "Fotografía", "Tres tipos de imagen. Las de acción muestran las máquinas trabajando en paisajes reales de Mendoza.")}
  <div class="ph-grid">
    <div class="ph-amb" style="background-image:url({BOSQUE})"><div class="grain"></div><span class="ph-lbl w">Ambiente · verde, fuera de foco, con grano</span></div>
    {slot("En acción · desmalezado en finca", "Horizontal 3:2 · luz de tarde · operario con protección", "s-big")}
    {slot("En acción · poda en viñedo", "Vertical 4:5 · detalle de manos y máquina")}
    {slot("En acción · corte de césped", "Horizontal 3:2 · jardín de casa")}
    <div class="ph-prod"><img src="{P["ms162"]}" alt=""><span class="ph-lbl">Producto · fondo blanco, cuadrada, 1200 px</span></div>
  </div>
  <div class="ph-rules"><span>{I["si"]} Personas con equipo de protección</span><span>{I["si"]} Luz natural</span><span>{I["si"]} Paisajes de Mendoza</span><span>{I["no"]} Fotos de stock genéricas</span><span>{I["no"]} Textos sobre la foto de producto</span></div>
</div>''', "", 11, "Fotografía"))

# 12 Interfaz
icons = [("camion","Envío"),("local","Retiro"),("cuotas","Cuotas"),("escudo","Garantía"),("llave","Servicio"),("chat","WhatsApp"),("bateria","Batería"),("nafta","Nafta"),("rayo","Eléctrica"),("lupa","Buscar"),("usuario","Cuenta"),("carrito","Carrito")]
pages.append(pg(f'''
<div class="pad">
  {head("06 · Interfaz", "Componentes de la tienda")}
  <div class="ui">
    <div class="ui-col">
      <span class="ui-l">Botones</span>
      <div class="btns"><span class="btn">Comprar</span><span class="btn btn-g">Ver ficha técnica</span><span class="btn btn-w">{I["chat"]}Hablá con un asesor</span></div>
      <span class="ui-l">Etiquetas</span>
      <div class="tags"><span class="tg t-of">15% OFF</span><span class="tg t-en">{I["camion"]}Envío gratis</span><span class="tg t-mo">{I["bateria"]}A batería</span></div>
      <span class="ui-l">Íconos · línea 1,8 px, esquinas redondeadas</span>
      <div class="icons">{"".join(f'<div>{I[k]}<span>{t}</span></div>' for k,t in icons)}</div>
    </div>
    <div class="card">
      <div class="card-img"><span class="tg t-of">15% OFF</span><img src="{P["ms162"]}" alt=""></div>
      <span class="c-m">STIHL</span><span class="c-n">Motosierra STIHL MS 162, espada 30 cm</span>
      <div class="c-p"><b>$ 389.900</b><s>$ 458.700</s></div><span class="c-c">6 cuotas sin interés de $ 64.983</span>
      <span class="btn btn-full">Agregar al carrito</span>
      <span class="c-note">Precios de ejemplo</span>
    </div>
  </div>
</div>''', "", 12, "Interfaz"))

# 13 Web escritorio
pages.append(pg(f'''
<div class="web">
  <div class="web-txt">
    <span class="ch">07 · La tienda online</span>
    <h2>Portada en computadora</h2>
    <ol class="anot">
      <li><b>Barra superior</b> envíos, retiro y cuotas</li>
      <li><b>Buscador protagonista</b> por máquina, marca o modelo</li>
      <li><b>Menú por uso</b> lo que el cliente necesita hacer</li>
      <li><b>Promesa + asesor</b> dos acciones claras</li>
      <li><b>Promos de temporada</b> con precio visible</li>
      <li><b>Franja de confianza</b> los cuatro pilares</li>
    </ol>
  </div>
  <div class="browser"><div class="b-bar"><i></i><i></i><i></i><span>silvestre.com.ar</span></div><img src="{SH["m-desk-top"]}" alt=""></div>
</div>''', "full", 13, "La tienda online"))

# 14 Web celular
pages.append(pg(f'''
<div class="mob">
  <div class="mob-txt">
    <span class="ch">07 · La tienda online</span>
    <h2>En el celular</h2>
    <p class="lead">La mayoría de las visitas llegan por el celular. El buscador queda siempre a mano, las categorías entran con el pulgar y WhatsApp está a un toque.</p>
  </div>
  <div class="phones">{"".join(f'<div class="phone"><img src="{SH[k]}" alt=""></div>' for k in ["m-mob-0","m-mob-1","m-mob-2"])}</div>
</div>''', "full", 14, "La tienda online", dark=True))

# 15 Marcas
marcas = [("STIHL","Máquinas y repuestos"),("Oleo-Mac","Cortadoras y tanzas"),("Fiasa","Cortadoras"),("Yard Machines","Tractores"),("Tramontina","Jardín"),("Bahco","Poda"),
          ("Picasso","Semillas"),("Niwa","Jardinería"),("Konan","Jardín"),("Dowen Pagio","Robots"),("BTA","Desmalezadoras"),("MTD","Tractores")]
pages.append(pg(f'''
<div class="pad">
  {head("08 · Marcas", "Las marcas que vendemos", "Logos oficiales de cada marca, del mismo tamaño visual, sobre blanco. Pedir el kit a cada proveedor.")}
  <div class="mk-grid">{"".join(f'<div class="mk{" mk-1" if i==0 else ""}"><b>{m}</b><span>{d}</span><em>Logo oficial</em></div>' for i,(m,d) in enumerate(marcas))}</div>
</div>''', "", 15, "Marcas"))

# 16 Contratapa
pages.append(pg(f'''
<div class="back" style="background-image:linear-gradient(rgba(20,61,24,.55),rgba(20,61,24,.75)),url({BOSQUE})"><div class="grain"></div>
  <img src="{LHB}" alt="">
  <div class="back-c"><span>{I["chat"]}(261) 242-6888</span><span>{I["pin"]}Tropero Sosa 175, Maipú, Mendoza</span><span>silvestre.com.ar</span></div>
</div>''', "full"))

css = open(os.path.join(H, "pdf.css")).read().replace("__FT__", FT)
open(os.path.join(H, "manual.html"), "w").write(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Silvestre · Manual de marca</title><style>{css}</style></head><body>{"".join(pages)}</body></html>')
print("pages", len(pages))
