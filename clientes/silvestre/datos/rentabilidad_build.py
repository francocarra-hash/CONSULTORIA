import sys, openpyxl, warnings
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.comments import Comment
from openpyxl.utils import get_column_letter as L
warnings.filterwarnings('ignore')
src, out = sys.argv[1], sys.argv[2]
wb = openpyxl.load_workbook(src)
dat, dr, pr = wb['Datos'], wb['Directa'], wb['Productos']

# --- Datos: lista de IVA para Argentina
dat['M1'] = 'IVA Argentina'; dat['M1'].font = Font(name='Calibri', bold=True)
dat['M2'] = 0.21; dat['M3'] = 0.105
for c in ('M2', 'M3'): dat[c].number_format = '0.0%'

# --- Directa: openpyxl no conserva los desplegables "x14" del original; se vuelven a crear igual
dr.data_validations.dataValidation = []
def dv(ws, formula, sqref, prompt=None):
    v = DataValidation(type='list', formula1=formula, allow_blank=True, showDropDown=False)
    if prompt: v.promptTitle, v.prompt, v.showInputMessage = 'IVA', prompt, True
    for part in sqref.split(): v.add(part)
    ws.add_data_validation(v)
dv(dr, '$D$2:$D$17', 'B21:C21')
dv(dr, 'Datos!$A$2:$A$5', 'B2 F2')
dv(dr, 'Datos!$K$2:$K$10', 'B4 F4')
dv(dr, 'Datos!$B$8:$B$29', 'B3 F3')
dv(dr, 'Datos!$M$2:$M$3', 'C7:C8 G7:G8', 'Elegí 21% o 10,5% según el producto (solo aplica si el país es Argentina).')

# --- Productos: calculadora lateral
F = 'Calibri'; NF = Font(name=F, size=11); HF = Font(name=F, size=11, bold=True, color='FFFFFF')
CALC = PatternFill('solid', fgColor='1E5A23'); ML = PatternFill('solid', fgColor='C16F1E'); INP = PatternFill('solid', fgColor='FFF2CC')
MONEY = '"$"\\ #,##0;-"$"\\ #,##0;"-"'; PCT = '0.0%'
LAST = 300
cols = [
 # (col, header, kind, fmt, formula-template or default, comment)
 ('J', 'Vertical ML', 'in', None, None, 'Desplegable. Define la comisión (hoja Datos).'),
 ('K', 'Tipo de publicación', 'in', None, None, 'Desplegable: Clásica o con cuotas.'),
 ('L', 'IVA venta', 'in', PCT, None, 'Desplegable 21% o 10,5%. Por defecto, el mismo IVA de compra (columna D).'),
 ('M', 'Precio de venta (c/IVA)', 'in', MONEY, None, 'Cargá tu precio. Viene precargado con el precio de referencia de ML (columna AD) cuando lo hay.'),
 ('N', 'Envío (costo, en positivo)', 'in', MONEY, None, 'Costo de envío que pagás vos. Poner manual, como en la hoja Directa.'),
 ('O', 'Comisión %', 'f', PCT, '=IF($M{r}="","",IFERROR(IF($K{r}="Clásica",VLOOKUP("Argentina"&$J{r},Datos!$C:$D,2,0),VLOOKUP("Argentina"&$J{r},Datos!$C:$D,2,0)+VLOOKUP("Argentina"&$K{r},Datos!$H:$I,2,0)),"Error"))', None),
 ('P', 'Comisión', 'f', MONEY, '=IF($M{r}="","",IFERROR(-$M{r}*$O{r},"Error"))', None),
 ('Q', 'IVA comisión', 'f', MONEY, '=IF($M{r}="","",IFERROR(-($P{r}-$P{r}/(1+Datos!$B$2)),"Error"))', None),
 ('R', 'Costo fijo', 'f', MONEY, '=IF($M{r}="","",IF($M{r}<=15000,-1000,IF($M{r}<=25000,-2000,IF($M{r}<=33000,-2400,0))))', 'Mismos tramos que la hoja Directa.'),
 ('S', 'IVA costo fijo', 'f', MONEY, '=IF($M{r}="","",-($R{r}-$R{r}/(1+Datos!$B$2)))', None),
 ('T', 'IVA venta $', 'f', MONEY, '=IF($M{r}="","",-$M{r}/(1+$L{r})*$L{r})', None),
 ('U', 'IVA compra $', 'f', MONEY, '=IF($M{r}="","",$C{r}*$D{r})', 'Crédito fiscal: costo sin IVA × IVA de compra (columna D).'),
 ('V', 'Envío', 'f', MONEY, '=IF($M{r}="","",-N($N{r}))', None),
 ('W', 'IVA envío', 'f', MONEY, '=IF($M{r}="","",-($V{r}-$V{r}/(1+Datos!$B$2)))', None),
 ('X', 'Otros impuestos', 'f', MONEY, '=IF($M{r}="","",-$M{r}*Datos!$C$2)', 'Alícuota de Datos!C2 (Argentina).'),
 ('Y', 'Plata en mano', 'f', MONEY, '=IF($M{r}="","",IFERROR($M{r}+$U{r}+$T{r}+$P{r}+$Q{r}+$R{r}+$S{r}+$V{r}+$W{r}+$X{r},"Error"))', None),
 ('Z', 'Utilidad', 'f', MONEY, '=IF($M{r}="","",IFERROR($Y{r}-$E{r},"Error"))', 'Igual que en Directa: suma de todo, incluido el costo con IVA.'),
 ('AA', 'Margen %', 'f', PCT, '=IF($M{r}="","",IFERROR($Z{r}/($M{r}+$T{r}),"Error"))', 'Utilidad sobre precio sin IVA, como en Directa.'),
 ('AB', 'MarkUp', 'f', '0.00', '=IF($M{r}="","",IFERROR($M{r}/$E{r},"Error"))', None),
 ('AD', 'Precio más bajo ML (c/IVA)', 'in', MONEY, None, 'Precio más bajo de la competencia. Precargado con el menor precio promedio del export Jardin_YTD 2026 (ventas ÷ unidades). Reemplazalo por el precio actual de ML.'),
 ('AE', 'Publicación de referencia', 'in', None, None, 'De dónde salió el precio de AD.'),
 ('AF', 'Margen objetivo', 'in', PCT, None, 'Margen que querés ganar a ese precio (sobre precio sin IVA).'),
 ('AG', 'Margen a precio ML con costo actual', 'f', PCT, '=IF(N($AD{r})=0,"",IFERROR(($AD{r}/(1+$L{r})-($AD{r}*$O{r}+IF($AD{r}<=15000,1000,IF($AD{r}<=25000,2000,IF($AD{r}<=33000,2400,0)))+N($N{r}))/(1+Datos!$B$2)-$AD{r}*Datos!$C$2-$C{r})/($AD{r}/(1+$L{r})),"Error"))', None),
 ('AH', 'Costo máximo (s/IVA) para precio ML', 'f', MONEY, '=IF(N($AD{r})=0,"",IFERROR($AD{r}/(1+$L{r})*(1-$AF{r})-($AD{r}*$O{r}+IF($AD{r}<=15000,1000,IF($AD{r}<=25000,2000,IF($AD{r}<=33000,2400,0)))+N($N{r}))/(1+Datos!$B$2)-$AD{r}*Datos!$C$2,"Error"))', 'Costo sin IVA que te deja el margen objetivo vendiendo al precio de AD.'),
 ('AI', 'Costo máximo (c/IVA)', 'f', MONEY, '=IF($AH{r}="","",IFERROR($AH{r}*(1+$D{r}),"Error"))', None),
 ('AJ', 'Costo actual vs máximo', 'f', PCT, '=IF($AH{r}="","",IFERROR($C{r}/$AH{r}-1,"Error"))', 'Positivo: tu costo está por encima del máximo, hay que bajarlo ese %.'),
 ('AK', 'Estado', 'f', None, '=IF($AH{r}="","",IFERROR(IF($C{r}<=$AH{r},"OK a ese precio","Bajar costo"),"Error"))', None),
]
# precios de referencia del export (menor precio promedio de publicaciones del mismo producto)
REF = {
 2: (180000, 'Sopladora Aspiradora A Explosión 26cc Pampa Pro · 10 u.'),
 3: (308889, 'Motor Niwa Cortacésped 6,5hp Tipo Briggs · 90 u.'),
 4: (195000, 'Motor Vertical Niwa Mvnw-149 4.5 Hp · 20 u.'),
 5: (173000, 'Cortadora Césped Eléctrica Konan 1400w · 2 u.'),
 6: (480000, 'Cortadora Césped Nafta Fiasa Fc1111410 140cc 46cm · 5 u.'),
 7: (750000, 'Cortadora De Césped Naftera Oleo-mac® FC1111700 · 2 u.'),
 10: (25700, 'Repuesto Cuchilla Cortadora Oleo Mac Ge47 Ra · 30 u. (confirmar que sea la misma cuchilla)'),
}
for col, h, kind, fmt, tpl, com in cols:
    c = pr[f'{col}1']; c.value = h; c.font = HF; c.fill = ML if L(openpyxl.utils.column_index_from_string(col)) in ('AD','AE','AF','AG','AH','AI','AJ','AK') else CALC
    c.alignment = Alignment(wrap_text=True, vertical='center', horizontal='center')
    if com: c.comment = Comment(com, 'Consultoría')
    pr.column_dimensions[col].width = 40 if col == 'AE' else (24 if col == 'J' else 15)
    for r in range(2, LAST + 1):
        x = pr[f'{col}{r}']; x.font = NF
        if fmt: x.number_format = fmt
        if kind == 'f': x.value = tpl.format(r=r)
        else: x.fill = INP
pr.row_dimensions[1].height = 45
pr['I1'].value = None
for r in range(2, LAST + 1):
    has = pr[f'C{r}'].value is not None
    if has:
        pr[f'J{r}'] = 'Hogar, muebles y jardín'; pr[f'K{r}'] = 'Clásica'; pr[f'L{r}'] = pr[f'D{r}'].value
        pr[f'N{r}'] = 0; pr[f'AF{r}'] = 0.15
        if r in REF:
            pr[f'AD{r}'] = REF[r][0]; pr[f'AE{r}'] = REF[r][1]; pr[f'M{r}'] = REF[r][0]
        else:
            pr[f'AE{r}'] = 'Sin referencia en el export: cargar precio de ML'
    # IVA compra/venta: desplegable
dv(pr, 'Datos!$M$2:$M$3', f'D2:D{LAST} L2:L{LAST}', 'Elegí 21% o 10,5% según el producto.')
dv(pr, 'Datos!$B$8:$B$19', f'J2:J{LAST}')
dv(pr, 'Datos!$K$2:$K$10', f'K2:K{LAST}')
for r in range(2, LAST + 1):
    if pr[f'E{r}'].value is None: pr[f'E{r}'] = f'=IF($C{r}="","",$C{r}*(1+$D{r}))'
pr.freeze_panes = 'C2'
wb.save(out); print('ok')
