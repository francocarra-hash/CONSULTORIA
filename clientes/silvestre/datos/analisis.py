import sys, re, pandas as pd
df = pd.read_excel(sys.argv[1], sheet_name=0)
df.columns = ['titulo','c1','c2','c3','c4','c5','marca','vendedor','ventas','unidades','modelo']
k = df.marca.astype(str).str.strip().str.lower()
MAP = {
 'STIHL': ['stihl','stihl original','stihll'],
 'Tramontina': ['tramontina','tramontina/cdc','tramontina multi'],
 'Niwa': ['niwa','niwa original'],
 'Dowen Pagio': ['dowen pagio','dowen paggio'],
 'BTA': ['bta tools','bta','bta garden','bta maquinas'],
 'Konan': ['konan'],
 'Fiasa': ['fiasa','fiasa® premium','windsor® by fiasa®','fiasa® windsor®'],
 'Bahco': ['bahco'],
 'Oleo-Mac': ['oleo-mac','oleo mac'],
 'MTD / Yard Machines': ['mtd','yard','mtd yard machines','yard machines','mtd original','mtd cub cadet'],
 'Picasso': ['picasso'],
}
inv = {v: b for b, vs in MAP.items() for v in vs}
df['brand'] = k.map(inv)
print('vendedor silvestre:', df[df.vendedor.astype(str).str.contains('silvestre', case=False)][['vendedor','marca','unidades']].head(10).to_string())
d = df[df.brand.notna()].copy()
d['mod'] = d.modelo.astype(str).str.strip().str.lower().str.replace(r'[\s\-_/\.]+', '', regex=True)
d.loc[d['mod'].isin(['nan','(blanco)','','none','na','n/a']), 'mod'] = None
d['key'] = d['mod'].fillna('t:' + d.titulo.astype(str).str.lower().str.slice(0, 60))
rows = []
for b, g in d.groupby('brand'):
    for key, gg in g.groupby('key'):
        top = gg.sort_values('unidades', ascending=False).iloc[0]
        rows.append(dict(marca=b, modelo=top.modelo if pd.notna(top.modelo) and str(top.modelo) != '(blanco)' else '', producto=top.titulo,
            categoria=top.c3, subcategoria=top.c4 if str(top.c4) != '(blanco)' else '', unidades=int(gg.unidades.sum()), ventas=float(gg.ventas.sum()),
            publicaciones=len(gg), vendedores=gg.vendedor.nunique()))
r = pd.DataFrame(rows)
r['precio_prom'] = (r.ventas / r.unidades).round(0)
tot = d.groupby('brand').agg(unidades=('unidades','sum'), ventas=('ventas','sum'), publicaciones=('titulo','count'), vendedores=('vendedor','nunique')).sort_values('ventas', ascending=False)
cat = d.groupby(['brand','c3']).unidades.sum().reset_index().sort_values(['brand','unidades'], ascending=[True,False])
tot['categoria_principal'] = cat.groupby('brand').head(1).set_index('brand').c3
tot['share_unid_cat_ppal'] = (cat.groupby('brand').head(1).set_index('brand').unidades / tot.unidades).round(2)
print(tot.to_string())
pd.set_option('display.width', 250); pd.set_option('display.max_colwidth', 70)
for b in tot.index:
    t = r[r.marca == b].sort_values('unidades', ascending=False).head(6)
    print('\n###', b); print(t[['modelo','producto','categoria','unidades','ventas','precio_prom','vendedores']].to_string(index=False))
r.to_pickle(sys.argv[2] + '/r.pkl'); tot.to_pickle(sys.argv[2] + '/tot.pkl'); cat.to_pickle(sys.argv[2] + '/cat.pkl'); d.to_pickle(sys.argv[2] + '/d.pkl')
print('\nmercado total', df.unidades.sum(), df.ventas.sum())
