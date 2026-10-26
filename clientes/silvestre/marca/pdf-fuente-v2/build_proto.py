import base64, os
H = os.path.dirname(os.path.abspath(__file__))
def b64(p, m): return f"data:{m};base64," + base64.b64encode(open(os.path.join(H, p), "rb").read()).decode()
def rama(x, y, n, pitch, cls=""):
    out = [f'<rect x="{x-4}" y="{y-8}" width="8" height="{n*pitch+8}" rx="4" fill="currentColor"/>']
    for i in range(n):
        yy = y + i*pitch
        if i % 2 == 0: out.append(f'<rect x="{x-34}" y="{yy}" width="32" height="16" rx="8" fill="currentColor" transform="rotate(-32 {x-2} {yy+8})"/>')
        else: out.append(f'<rect x="{x+2}" y="{yy}" width="32" height="16" rx="8" fill="currentColor" transform="rotate(32 {x+2} {yy+8})"/>')
    return "".join(out)
marcas = ["STIHL","Oleo-Mac","Fiasa","Yard Machines","Tramontina","Bahco","Picasso","Niwa","Konan","Dowen Pagio","BTA","MTD"]
M = "".join(f'<a class="marca" href="#">{m}</a>' for m in marcas)
s = open(os.path.join(H, "prototipo.src.html")).read()
rep = {"{{FONT}}": b64("fonts/Montserrat.woff2","font/woff2"), "{{LOGO}}": b64("kit/logo-horizontal.svg","image/svg+xml"), "{{LOGOB}}": b64("kit/logo-horizontal-blanco.svg","image/svg+xml"), "{{BOSQUEKIT}}": b64("kit/bosque-kit.jpg","image/jpeg"), "{{BOSQUE}}": b64("img/bosque.jpg","image/jpeg"),
       "{{RAMA}}": f'<g style="color:#39A935">{rama(100, 20, 15, 26)}</g>', "{{MARCAS}}": M}
for k in ["ms162","ms194t","mse141","bge71","hse61","fs"]: rep["{{"+k.upper()+"}}"] = b64(f"img/{k}.png","image/png")
for k,v in rep.items(): s = s.replace(k, v)
assert "{{" not in s
open(os.path.join(H, "prototipo.html"), "w").write(s); print(len(s)//1024, "KB")
