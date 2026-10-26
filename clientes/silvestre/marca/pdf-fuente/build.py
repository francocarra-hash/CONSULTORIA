import base64, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
def b64(p, mime):
    return f"data:{mime};base64," + base64.b64encode(open(os.path.join(HERE, p), "rb").read()).decode()

LOGO = b64("img/logo.png", "image/png")
P = {k: b64(f"img/{k}.png", "image/png") for k in ["ms162", "ms194t", "mse141", "bge71", "hse61", "fs"]}
BOSQUE = b64("img/bosque.jpg", "image/jpeg")
F_TIT = b64("fonts/Nunito.woff2", "font/woff2")
F_TXT = b64("fonts/NunitoSans.woff2", "font/woff2")

def ic(paths, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'
I = {
 "lupa": ic('<circle cx="11" cy="11" r="6.5"/><path d="M16 16l4.5 4.5"/>'),
 "usuario": ic('<circle cx="12" cy="8" r="4"/><path d="M4.5 20.5c1.2-3.8 4-5.5 7.5-5.5s6.3 1.7 7.5 5.5"/>'),
 "carrito": ic('<path d="M3 4h2.5l2.2 11h10.6l2-8H7"/><circle cx="9.5" cy="19.5" r="1.3"/><circle cx="17" cy="19.5" r="1.3"/>'),
 "camion": ic('<path d="M2.5 6.5h11v9h-11z"/><path d="M13.5 9.5h4l3 3.2v2.8h-7"/><circle cx="6.5" cy="17.5" r="1.8"/><circle cx="17" cy="17.5" r="1.8"/>'),
 "local": ic('<path d="M3.5 10l1.5-5.5h14L20.5 10"/><path d="M3.5 10c0 1.7 1.3 2.8 2.9 2.8S9.3 11.7 9.3 10c0 1.7 1.3 2.8 2.7 2.8s2.7-1.1 2.7-2.8c0 1.7 1.3 2.8 2.9 2.8s2.9-1.1 2.9-2.8"/><path d="M5 12.6V20h14v-7.4"/><path d="M10 20v-4.5h4V20"/>'),
 "cuotas": ic('<rect x="2.5" y="5.5" width="19" height="13" rx="2"/><path d="M2.5 9.5h19"/><path d="M6 15h4"/>'),
 "escudo": ic('<path d="M12 3l7.5 3v5.5c0 4.6-3.2 8.2-7.5 9.5-4.3-1.3-7.5-4.9-7.5-9.5V6z"/><path d="M8.8 12.2l2.2 2.2 4.2-4.4"/>'),
 "llave": ic('<path d="M14.5 6.5a4 4 0 0 0 5 5L13 18a2.1 2.1 0 0 1-3-3l6.5-6.5"/><path d="M14.5 6.5L17 4l3 3-2.5 2.5"/>'),
 "hoja": ic('<path d="M5 19c0-8 5-13 14-14-1 9-6 14-14 14z"/><path d="M5 19l7-7"/>'),
 "bateria": ic('<rect x="3" y="7.5" width="16" height="9" rx="2"/><path d="M21 10.5v3"/><path d="M11.5 9l-2 3h3l-2 3"/>'),
 "nafta": ic('<path d="M5 20V5.5A1.5 1.5 0 0 1 6.5 4h7A1.5 1.5 0 0 1 15 5.5V20"/><path d="M3.5 20h13"/><path d="M7.5 7.5h5v4h-5z"/><path d="M15 9.5h2a1.5 1.5 0 0 1 1.5 1.5v5a1.5 1.5 0 0 0 3 0V8l-2.5-2.5"/>'),
 "rayo": ic('<path d="M13 2.5L5 13.5h6l-1 8 8-11h-6z"/>'),
 "chat": ic('<path d="M4.5 19.5l1.2-3.6A7.5 7.5 0 1 1 8.6 18.6z"/><path d="M9.2 9.5c.3 2 2.3 4.1 4.6 4.6l1-1.1 1.8.8c-.2 1.2-1.2 1.9-2.3 1.7-3-.5-5.6-3.1-6-6-.2-1.1.5-2.1 1.7-2.3l.8 1.8z"/>'),
 "cesped": ic('<path d="M3 20h18"/><path d="M5 20c0-4 1-7 3-9"/><path d="M9 20c0-5 1.5-9 4-12"/><path d="M14 20c0-3.5 1-6.5 3-8.5"/><path d="M18 20c0-2.5.5-4.5 2-6"/>'),
 "sierra": ic('<path d="M3 15.5h11l3-3.5h3.5v6H14l-1.5 1.5H3z"/><path d="M5 15.5v-2M8 15.5v-2M11 15.5v-2"/><path d="M15 12V8.5h3"/>'),
 "viento": ic('<path d="M3 9h11a3 3 0 1 0-3-3"/><path d="M3 14h15a3 3 0 1 1-3 3"/><path d="M3 11.5h7"/>'),
 "gota": ic('<path d="M12 3.5c3.5 4.5 6 7.8 6 10.8a6 6 0 0 1-12 0c0-3 2.5-6.3 6-10.8z"/>'),
 "semilla": ic('<path d="M12 21v-8"/><path d="M12 13c0-4-3-7-7.5-7 0 4.5 3 7 7.5 7z"/><path d="M12 15c0-3.5 2.5-6 6.5-6 0 4-2.5 6-6.5 6z"/>'),
 "pala": ic('<path d="M14 10L20.5 3.5"/><path d="M18 3l3 3"/><path d="M14 10l-1.5-1.5-6 6a3.5 3.5 0 0 0 5 5l6-6z"/>'),
 "tuerca": ic('<path d="M12 2.8l8 4.6v9.2l-8 4.6-8-4.6V7.4z"/><circle cx="12" cy="12" r="3.2"/>'),
 "tag": ic('<path d="M3.5 12.5V4.5a1 1 0 0 1 1-1h8l8 8-9 9z"/><circle cx="8.5" cy="8.5" r="1.5"/>'),
 "si": ic('<path d="M5 12.5l4.5 4.5L19 7.5"/>', "ok"),
 "no": ic('<path d="M6 6l12 12M18 6L6 18"/>', "ko"),
}

def leaf_branch(x, y, n=6, pitch=24, scale=1.0, cls="hoja"):
    """Rama hecha con píldoras, eco de la rama del logo."""
    out = [f'<rect class="{cls}" x="{x-4}" y="{y-8}" width="8" height="{n*pitch+8}" rx="4"/>']
    for i in range(n):
        yy = y + i * pitch
        if i % 2 == 0:
            out.append(f'<rect class="{cls}" x="{x-34}" y="{yy}" width="32" height="16" rx="8" transform="rotate(-32 {x-2} {yy+8})"/>')
        else:
            out.append(f'<rect class="{cls}" x="{x+2}" y="{yy}" width="32" height="16" rx="8" transform="rotate(32 {x+2} {yy+8})"/>')
    return "\n".join(out)

def card(img, marca, nombre, precio, cuotas, etq="", antes="", sinstock=False):
    e = f'<div class="etqs">{etq}</div>' if etq else ""
    a = f'<s>{antes}</s>' if antes else ""
    return f'''<div class="card{' off' if sinstock else ''}">
  <div class="foto">{e}<img src="{img}" alt=""></div>
  <div class="info"><span class="marca">{marca}</span><span class="nom">{nombre}</span>
  <span class="pre">{precio}{a}</span><span class="cuo">{cuotas}</span></div></div>'''

E_OF = '<span class="etq of">15% OFF</span>'
E_EN = f'<span class="etq en">{I["camion"]}Envío gratis</span>'
E_BA = f'<span class="etq mo">{I["bateria"]}A batería</span>'
E_EL = f'<span class="etq mo">{I["rayo"]}Eléctrica</span>'

def page(num, label, body, cls=""):
    foot = "" if num is None else f'<footer class="pie-pag"><span>Silvestre · Manual de marca</span><span>{label}</span><span>{num:02d}</span></footer>'
    return f'<section class="page {cls}">{body}{foot}</section>'

pages = []

# 1. Portada
pages.append(page(None, "", f'''
<div class="portada">
  <svg class="portada-art" viewBox="0 0 560 794" aria-hidden="true">
    <rect class="f-naranja" x="40" y="-24" width="232" height="520" rx="24"/>
    <rect class="f-claro" x="296" y="200" width="264" height="420" rx="24"/>
    <rect class="f-accion" x="40" y="520" width="232" height="298" rx="24"/>
    <rect class="f-verde" x="296" y="644" width="120" height="40" rx="8"/>
    {leaf_branch(428, 240, n=13, pitch=27, cls="f-verde")}
    <g>{"".join(f'<rect class="f-corte" x="{x}" y="{y}" width="40" height="20" rx="10" transform="rotate(-32 {x+20} {y+10})"/>' for x,y in [(90,90),(150,150),(90,210),(150,270),(90,330)])}</g>
  </svg>
  <div class="portada-txt">
    <img class="portada-logo" src="{LOGO}" alt="Silvestre máquinas y jardines">
    <h1>Manual<br>de marca</h1>
    <p>Para la tienda online · 2026</p>
  </div>
</div>'''))

# 2. La marca en una imagen
ben = [("hoja","Especialistas"),("escudo","Garantía oficial"),("llave","Repuestos y servicio"),("camion","Envíos a todo el país")]
pages.append(page(2, "La marca", f'''
<div class="split">
  <div class="split-a" style="background:url({BOSQUE}) center/cover"><div class="bosque-velo"></div>
    <div class="bosque-txt"><span class="eyebrow claro">Quiénes somos</span>
    <h2 class="blanco">Máquinas para tu jardín y tu campo, con el asesoramiento de quien las conoce.</h2>
    <p class="blanco">Distribuidor oficial STIHL · Maipú, Mendoza</p></div></div>
  <div class="split-b">
    <span class="eyebrow">Por qué comprarnos</span>
    <div class="ben4">{"".join(f'<div class="ben"><span class="ben-n">{i+1}</span>{I[k]}<strong>{t}</strong></div>' for i,(k,t) in enumerate(ben))}</div>
    <div class="personalidad">
      {"".join(f'<span class="chip">{t}</span>' for t in ["Experto","Claro","Práctico","De confianza","Cercano"])}
    </div>
  </div>
</div>'''))

# 3. Logo
pages.append(page(3, "Logo", f'''
<div class="pad">
  <span class="eyebrow">Logo</span>
  <div class="logo-grid">
    <div class="logo-hero">
      <div class="respeto"><img src="{LOGO}" alt=""><span class="r-top">s</span><span class="r-left">s</span><span class="r-right">s</span><span class="r-bot">s</span></div>
      <div class="cotas">
        <div class="cota"><div class="regla" style="width:140px"></div><strong>140 px</strong><span>mínimo con bajada</span></div>
        <div class="cota"><div class="regla" style="width:200px"></div><strong>160 a 220 px</strong><span>encabezado en computadora</span></div>
        <div class="cota"><div class="regla" style="width:130px"></div><strong>120 a 140 px</strong><span>encabezado en celular</span></div>
      </div>
    </div>
    <div class="logo-fondos">
      <div class="lf" style="background:var(--fondo)"><img src="{LOGO}" alt="">{I["si"]}</div>
      <div class="lf" style="background:var(--verde-claro)"><img src="{LOGO}" alt="" class="mult">{I["si"]}</div>
      <div class="lf" style="background:var(--superficie)"><img src="{LOGO}" alt="" class="mult">{I["si"]}</div>
      <div class="lf" style="background:var(--naranja)"><img src="{LOGO}" alt="" class="mult">{I["no"]}</div>
    </div>
  </div>
  <div class="nos">
    <div class="nol"><div class="nobox"><img src="{LOGO}" alt="" style="transform:scaleX(1.5)"></div>{I["no"]}<span>Estirar</span></div>
    <div class="nol"><div class="nobox"><img src="{LOGO}" alt="" style="transform:rotate(-12deg)"></div>{I["no"]}<span>Rotar</span></div>
    <div class="nol"><div class="nobox"><img src="{LOGO}" alt="" style="filter:hue-rotate(160deg)"></div>{I["no"]}<span>Cambiar colores</span></div>
    <div class="nol"><div class="nobox"><img src="{LOGO}" alt="" style="filter:drop-shadow(4px 4px 3px rgba(0,0,0,.55))"></div>{I["no"]}<span>Sombras</span></div>
    <div class="nol"><div class="nobox"><span class="falso">Silvestre</span></div>{I["no"]}<span>Otra letra</span></div>
  </div>
</div>'''))

# 4. Color
sw_main = [("naranja","Naranja Silvestre","#F29100","242 · 145 · 0","Logo · barra · ofertas","oscuro"),
           ("verde","Verde Silvestre","#3AAA35","58 · 170 · 53","Rama · íconos · stock","oscuro"),
           ("verde-accion","Verde acción","#2E7D32","46 · 125 · 50","Botones · links","blanco")]
sw_sec = [("verde-accion-hover","Verde profundo","#1E5A23","blanco"),("verde-claro","Verde claro","#EAF9C6","oscuro"),
          ("naranja-claro","Naranja claro","#FFF4E0","oscuro"),("texto","Texto","#1A1A1A","blanco"),
          ("texto-secundario","Gris","#5F6368","blanco"),("superficie","Superficie","#F6F6F3","oscuro"),("borde","Borde","#E4E4DE","oscuro")]
pages.append(page(4, "Color", f'''
<div class="pad">
  <span class="eyebrow">Color</span>
  <div class="sw-main">{"".join(f'<div class="sw {c}" style="background:var(--{t})"><strong>{n}</strong><span class="hex">{h}</span><span>RGB {r}</span><em>{u}</em></div>' for t,n,h,r,u,c in sw_main)}</div>
  <div class="sw-sec">{"".join(f'<div class="sw2 {c}" style="background:var(--{t})"><strong>{n}</strong><span class="hex">{h}</span></div>' for t,n,h,c in sw_sec)}</div>
  <div class="prop"><div style="flex:70;background:var(--fondo)">70 %</div><div style="flex:15;background:var(--verde-accion);color:#fff">15 %</div><div style="flex:10;background:var(--naranja)">10</div><div style="flex:5;background:var(--texto);color:#fff">5</div></div>
  <div class="prop-ley"><span>Blanco y neutros</span><span>Verdes</span><span>Naranja</span><span>Texto</span></div>
</div>'''))

# 5. Contraste
pairs = [("#1A1A1A","#F29100","Aa","7,3 : 1",True),("#FFFFFF","#2E7D32","Aa","5,1 : 1",True),("#1E5A23","#EAF9C6","Aa","7,4 : 1",True),("#1A1A1A","#FFFFFF","Aa","17,4 : 1",True),
         ("#FFFFFF","#F29100","Aa","2,4 : 1",False),("#FFFFFF","#3AAA35","Aa","3,0 : 1",False),("#FFFFFF","#62C659","Aa","2,2 : 1",False),("#559D70","#EAF9C6","Aa","2,9 : 1",False)]
pages.append(page(5, "Contraste", f'''
<div class="pad">
  <span class="eyebrow">Contraste</span>
  <div class="contr">{"".join(f'<div class="ct" style="background:{bg};color:{fg}"><span class="aa">{t}</span><span class="ratio">{r}</span>{I["si"] if ok else I["no"]}</div>' for fg,bg,t,r,ok in pairs)}</div>
  <div class="contr-ley"><span>{I["si"]} Se lee bien</span><span>{I["no"]} No usar</span><span class="nota">Los cuatro de abajo están hoy en la web: barra, rama, botón Enviar y textos del pie.</span></div>
</div>'''))

# 6. Tipografía
pages.append(page(6, "Tipografía", f'''
<div class="tipo">
  <div class="tipo-a">
    <span class="eyebrow">Títulos</span>
    <div class="aa-gig tit">Aa</div>
    <strong class="fam">Nunito</strong><span class="pesos">Bold 700 · ExtraBold 800</span>
    <div class="abc tit">ABCDEFGHIJKLMNÑOPQRSTUVWXYZ<br>abcdefghijklmnñopqrstuvwxyz<br>áéíóú 0123456789 $ %</div>
  </div>
  <div class="tipo-b">
    <span class="eyebrow">Textos, precios y botones</span>
    <div class="aa-gig txt">Aa</div>
    <strong class="fam txt">Nunito Sans</strong><span class="pesos">Regular 400 · SemiBold 600 · Bold 700</span>
    <div class="escala">
      <div><span class="tit" style="font-size:40px;font-weight:800">Máquinas para tu jardín</span><em>Portada 40</em></div>
      <div><span class="tit" style="font-size:28px">Motosierras y poda</span><em>Sección 28</em></div>
      <div><span class="txt" style="font-size:32px;font-weight:700">$ 389.900</span><em>Precio ficha 32</em></div>
      <div><span class="txt" style="font-size:20px;font-weight:700">$ 389.900</span><em>Precio tarjeta 20</em></div>
      <div><span class="txt" style="font-size:16px">Ideal para jardines medianos y poda de cercos.</span><em>Texto 16</em></div>
      <div><span class="txt" style="font-size:14px;color:var(--texto-secundario)">6 cuotas sin interés de $ 64.983</span><em>Chico 14</em></div>
    </div>
  </div>
</div>'''))

# 7. Iconos y botones
icons = [("camion","Envío"),("local","Retiro"),("cuotas","Cuotas"),("escudo","Garantía"),("llave","Servicio"),("chat","WhatsApp"),("bateria","Batería"),("nafta","Nafta"),("rayo","Eléctrica"),("lupa","Buscar"),("usuario","Cuenta"),("carrito","Carrito")]
pages.append(page(7, "Íconos y botones", f'''
<div class="pad">
  <span class="eyebrow">Íconos · línea redondeada · un color</span>
  <div class="iconos">{"".join(f'<div class="icn">{I[k]}<span>{t}</span></div>' for k,t in icons)}</div>
  <span class="eyebrow" style="margin-top:34px">Botones y etiquetas</span>
  <div class="botones">
    <div class="bt-col"><span class="btn">Comprar</span><em>Principal</em></div>
    <div class="bt-col"><span class="btn sec">Ver ficha técnica</span><em>Secundario</em></div>
    <div class="bt-col"><span class="btn wa">{I["chat"]}Consultar por WhatsApp</span><em>WhatsApp</em></div>
    <div class="bt-col"><div class="etq-fila">{E_OF}{E_EN}{E_BA}</div><em>Etiquetas</em></div>
  </div>
  <em class="barra-et" style="margin-top:auto">Barra superior</em><div class="barra-demo" style="margin-top:0"><span>Envíos a todo el país</span><span>·</span><span>Retiro en Maipú</span><span>·</span><span>Hasta 6 cuotas sin interés</span></div>
</div>'''))

# 8. Tarjetas de producto
pages.append(page(8, "Tarjeta de producto", f'''
<div class="pad">
  <span class="eyebrow">Tarjeta de producto</span>
  <div class="cards4">
    {card(P["ms162"],"STIHL","Motosierra STIHL MS 162, espada 30 cm","$ 389.900","6 cuotas sin interés de $ 64.983",E_OF,"$ 458.700")}
    {card(P["fs"],"STIHL","Desmalezadora a nafta STIHL","$ 712.000","6 cuotas sin interés de $ 118.667",E_EN)}
    {card(P["hse61"],"STIHL","Cortacerco eléctrico STIHL HSE 61","$ 254.500","3 cuotas sin interés de $ 84.833",E_EL)}
    {card(P["bge71"],"STIHL","Soplador eléctrico STIHL BGE 71","$ 189.900","Sin stock por ahora","","",True)}
  </div>
  <div class="anota">
    <span><b>1</b> Foto cuadrada, fondo blanco</span><span><b>2</b> Máximo dos etiquetas</span><span><b>3</b> Marca · nombre · precio siempre visible</span><span><b>4</b> Cuotas debajo</span><span style="margin-left:auto;font-weight:400">Precios de ejemplo</span>
  </div>
  <div class="antes-despues">
    <div class="ad no"><span class="ad-t">{I["no"]} Hoy</span><span class="mono">MOTOSIERRA ELECTRICA MSE 141</span></div>
    <div class="flecha">→</div>
    <div class="ad si"><span class="ad-t">{I["si"]} Nuevo</span><span class="tit">Motosierra eléctrica STIHL MSE 141, 1400 W</span></div>
  </div>
</div>'''))

# 9. Ficha de producto
pages.append(page(9, "Ficha de producto", f'''
<div class="ficha">
  <div class="galeria">
    <div class="g-main"><img src="{P["mse141"]}" alt=""></div>
    <div class="g-thumbs">{"".join(f'<div class="g-t{" act" if i==0 else ""}"><img src="{P["mse141"]}" alt=""></div>' for i in range(4))}</div>
  </div>
  <div class="compra">
    <span class="marca">STIHL</span>
    <h2 class="c-tit">Motosierra eléctrica STIHL MSE 141, 1400 W</h2>
    <span class="c-pre">$ 289.900</span>
    <div class="c-dato">{I["cuotas"]}<span><b>6 cuotas sin interés</b> de $ 48.317</span></div>
    <div class="c-dato">{I["camion"]}<span><b>Envío a todo el país</b></span></div>
    <div class="c-dato">{I["local"]}<span><b>Retiro gratis</b> en Tropero Sosa 175, Maipú</span></div>
    <span class="btn ancho">Comprar</span>
    <span class="btn sec ancho">Agregar al carrito</span>
    <span class="btn wa ancho">{I["chat"]}Consultar por WhatsApp</span>
    <div class="sellos"><span>{I["escudo"]}Garantía oficial</span><span>{I["escudo"]}Compra protegida</span><span>{I["local"]}Retiro en Maipú</span></div>
  </div>
</div>'''))

# 10. Portada web (computadora + celular)
menu = ["Corte de césped","Desmalezado","Motosierras y poda","Soplado","Agua","Línea a batería","Repuestos","Marcas"]
mini_cards = "".join(f'<div class="mc"><div class="mc-f"><img src="{P[k]}" alt=""></div><span class="mc-n">{n}</span><span class="mc-p">{p}</span></div>'
                     for k,n,p in [("ms162","Motosierra STIHL MS 162","$ 389.900"),("fs","Desmalezadora a nafta STIHL","$ 712.000"),("hse61","Cortacerco STIHL HSE 61","$ 254.500"),("ms194t","Motosierra STIHL MS 194 T","$ 512.000")])
pages.append(page(10, "La web", f'''
<div class="mock-wrap">
  <div class="desk">
    <div class="d-bar"><i></i><i></i><i></i><span>silvestre.com.ar</span></div>
    <div class="d-anuncio">Envíos a todo el país · Retiro en Maipú · Hasta 6 cuotas sin interés</div>
    <div class="d-head"><span class="d-busca">{I["lupa"]}Buscá por máquina, marca o modelo</span><img src="{LOGO}" alt=""><span class="d-acc">{I["usuario"]}{I["carrito"]}</span></div>
    <div class="d-menu">{"".join(f"<span>{m}</span>" for m in menu)}</div>
    <div class="d-hero">
      <div class="d-hero-t"><span class="eyebrow">Distribuidor oficial STIHL</span><h3>Máquinas para tu jardín y tu campo</h3><span class="btn chico">Ver motosierras</span></div>
      <img src="{P["ms162"]}" alt="">
    </div>
    <div class="d-ben">{"".join(f'<span>{I[k]}{t}</span>' for k,t in ben)}</div>
    <div class="d-cards">{mini_cards}</div>
  </div>
  <div class="phone">
    <div class="ph-notch"></div>
    <div class="ph-anuncio">Envíos a todo el país</div>
    <div class="ph-head"><span class="ham"><i></i><i></i><i></i></span><img src="{LOGO}" alt=""><span>{I["carrito"]}</span></div>
    <div class="ph-busca">{I["lupa"]}Buscá por máquina, marca o modelo</div>
    <div class="ph-hero"><h3>Máquinas para tu jardín y tu campo</h3><span class="btn chico">Ver productos</span></div>
    <div class="ph-cards">{"".join(f'<div class="mc"><div class="mc-f"><img src="{P[k]}" alt=""></div><span class="mc-n">{n}</span><span class="mc-p">{p}</span></div>' for k,n,p in [("ms162","Motosierra MS 162","$ 389.900"),("fs","Desmalezadora STIHL","$ 712.000")])}</div>
    <span class="ph-wa">{I["chat"]}</span>
  </div>
</div>'''))

# 11. Fotos
pages.append(page(11, "Fotos", f'''
<div class="pad">
  <span class="eyebrow">Fotos de producto</span>
  <div class="fotos">
    <div class="fx si"><div class="fx-f guia"><img src="{P["ms162"]}" alt=""><i class="g85"></i></div><span>{I["si"]} Fondo blanco · cuadrada · 85 % · centrada</span></div>
    <div class="fx si"><div class="fx-f"><img src="{P["fs"]}" alt=""></div><span>{I["si"]} Mínimo 1200 × 1200 px</span></div>
    <div class="fx no"><div class="fx-f"><img src="{P["mse141"]}" alt="" style="width:150%;max-width:none;margin-left:-40%"></div><span>{I["no"]} Producto cortado</span></div>
    <div class="fx no"><div class="fx-f"><img src="{P["hse61"]}" alt=""><b class="marca-agua">¡OFERTA! silvestre.com.ar</b></div><span>{I["no"]} Textos o marcas encima</span></div>
  </div>
  <div class="ambiente">
    <div class="amb-f" style="background-image:url({BOSQUE})"></div>
    <div class="amb-t">
      <span class="eyebrow">Ambiente</span>
      <div class="amb-chips">{"".join(f'<span class="chip">{t}</span>' for t in ["Mendoza real","Viñedos y fincas","Montaña","Luz natural","Con equipo de protección"])}</div>
    </div>
  </div>
</div>'''))

# 12. Voz
voz = [("Bienvenido a nuestra Tienda online","Máquinas para tu jardín y tu campo"),
       ("¡¡Súper ofertas imperdibles!!","Motosierras STIHL con hasta 6 cuotas sin interés"),
       ("Producto de excelente calidad","Motor de 2 tiempos de 45,4 cc, ideal para leña y poda"),
       ("Consulte disponibilidad","¿Tenés dudas? Escribinos por WhatsApp y te asesoramos")]
pages.append(page(12, "Voz", f'''
<div class="pad">
  <span class="eyebrow">Cómo hablamos</span>
  <div class="voz">{"".join(f'<div class="vz-no">{I["no"]}<span>{a}</span></div><div class="vz-si">{I["si"]}<span>{b}</span></div>' for a,b in voz)}</div>
  <div class="voz-reglas">{"".join(f'<span class="chip">{t}</span>' for t in ["Tratamos de vos","Primero el uso, después el dato","Frases cortas","$ 1.250.000 · 45,4 cc · 40 cm","Siempre con tildes","Un ¡! por pantalla como mucho"])}</div>
</div>'''))

# 13. Tienda: categorías y marcas
cats = [("cesped","Corte de césped"),("hoja","Desmalezado"),("sierra","Motosierras y poda"),("viento","Soplado y limpieza"),("gota","Agua"),("bateria","Línea a batería"),("semilla","Césped y semillas"),("pala","Herramientas"),("tuerca","Repuestos"),("tag","Marcas")]
marcas = ["STIHL","Oleo-Mac","Fiasa","Yard Machines","Tramontina","Bahco","Picasso","Niwa","Konan","Dowen Pagio","BTA"]
pages.append(page(13, "Tienda", f'''
<div class="pad">
  <span class="eyebrow">Menú por uso</span>
  <div class="cats">{"".join(f'<div class="cat">{I[k]}<span>{t}</span></div>' for k,t in cats)}</div>
  <span class="eyebrow" style="margin-top:30px">Marcas · logos oficiales, mismo tamaño visual</span>
  <div class="marcas">{"".join(f'<div class="mk{" princ" if i==0 else ""}"><span>{m}</span></div>' for i,m in enumerate(marcas))}<div class="mk vacio"><span>Logo oficial de cada marca</span></div></div>
</div>'''))

# 14. Cierre
pages.append(page(None, "", f'''
<div class="cierre">
  <div class="cierre-txt">
    <img src="{LOGO}" alt="" class="cierre-logo">
    <div class="contacto">
      <span>{I["chat"]}(261) 242-6888</span>
      <span>{I["local"]}Tropero Sosa 175, Maipú, Mendoza</span>
      <span>{I["usuario"]}silvestre.com.ar</span>
    </div>
  </div>
  <svg class="cierre-art" viewBox="0 0 480 794" aria-hidden="true">
    <rect class="f-claro" x="40" y="-24" width="200" height="460" rx="24"/>
    <rect class="f-naranja" x="264" y="120" width="216" height="560" rx="24"/>
    <rect class="f-accion" x="40" y="460" width="200" height="358" rx="24"/>
    {leaf_branch(140, 70, n=12, pitch=27, cls="f-verde")}
  </svg>
</div>'''))

CSS = open(os.path.join(HERE, "style.css")).read().replace("__F_TIT__", F_TIT).replace("__F_TXT__", F_TXT)
html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Silvestre · Manual de marca</title>
<style>{CSS}</style></head><body>{"".join(pages)}</body></html>'''
open(os.path.join(HERE, "manual.html"), "w").write(html)
print("pages", len(pages))
