import pandas as pd, sys
d = pd.read_pickle('d.pkl'); tot = pd.read_pickle('tot.pkl')
d['tipo'] = d.c3.where(d.c3 == 'Repuestos', 'Máquina / herramienta').where(d.c3 != 'Repuestos', 'Repuesto / accesorio')
d['key'] = d['mod'].fillna('t:' + d.titulo.astype(str).str.lower().str.slice(0, 60)) + '|' + d.c3.astype(str)
rows = []
for (b, key), gg in d.groupby(['brand', 'key']):
    top = gg.sort_values('unidades', ascending=False).iloc[0]
    rows.append(dict(Marca=b, Tipo=top.tipo, Categoría=top.c3, Subcategoría='' if str(top.c4) == '(blanco)' else top.c4,
        Modelo='' if pd.isna(top.modelo) or str(top.modelo) == '(blanco)' else str(top.modelo), **{'Publicación más vendida': top.titulo},
        Unidades=int(gg.unidades.sum()), **{'Ventas $': float(gg.ventas.sum())}, Publicaciones=len(gg), Vendedores=gg.vendedor.nunique()))
r = pd.DataFrame(rows); r['Precio promedio $'] = (r['Ventas $'] / r.Unidades).round(0)
r = r.sort_values(['Marca', 'Unidades'], ascending=[True, False])
r.to_pickle('r2.pkl')
pd.set_option('display.width', 260); pd.set_option('display.max_colwidth', 62)
for b in tot.index:
    g = r[r.Marca == b]
    for t, n in [('Máquina / herramienta', 5), ('Repuesto / accesorio', 3)]:
        x = g[g.Tipo == t].head(n)
        if len(x): print(f'\n### {b} · {t}'); print(x[['Modelo','Publicación más vendida','Categoría','Unidades','Ventas $','Precio promedio $','Vendedores']].to_string(index=False))
