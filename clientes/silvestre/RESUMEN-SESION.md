# Silvestre: resumen para retomar en una sesión nueva

> Estado al 27/10/2026. Todo está en el repo `francocarra-hash/consultoria`, rama `claude/busy-cerf-ebp54x`, carpeta `clientes/silvestre/`.

## El cliente

- **Silvestre Máquinas y Jardines**, Tropero Sosa 175, Maipú, Mendoza. Tel. (261) 242-6888, mail actual infosilvestremendoza@gmail.com.
- **Titular:** persona física, CUIT 20-34853967-2 (figura en el pie de su web).
- **Distribuidor oficial STIHL** y multimarca: STIHL (máquinas y repuestos), Oleo-Mac, Fiasa, MTD / Yard Machines, Tramontina, Bahco (poda), Picasso (semillas), Niwa, Konan (algunas), Dowen Pagio (robots cortacésped y de piscina), BTA (desmalezadoras).
- **Web actual:** silvestre.com.ar, ya en Tiendanube. Están armando un borrador nuevo con la **plantilla Ipanema**.

## Qué está hecho (archivos)

| Tema | Archivo |
|---|---|
| Paso 1: alta en Mercado Libre | `01-alta-mercado-libre.md` |
| Paso 2: configurar Tiendanube con Ipanema | `02-tiendanube-ipanema.md` |
| Paso 3: publicar en el catálogo de ML | `03-publicar-en-catalogo.md` |
| Manual de marca (texto) | `manual-de-marca-web.md` |
| Manual de marca (PDF visual, 16 páginas) | `marca/silvestre-manual-de-marca.pdf` |
| Logos en vector (horizontal y apilado; color, blanco y negro) | `marca/logos/` |
| Variables CSS de marca | `marca/silvestre-tokens.css` |
| Maqueta de la portada de la tienda (computadora y celular) | `web/portada-prototipo.html` |
| Lo más vendido de cada marca en ML (Jardín 2026) | `datos/silvestre-marcas-mas-vendidas-meli-2026.xlsx` |
| Calculadora de rentabilidad con cálculo masivo | `datos/Calculo_Rentabilidad_Silvestre.xlsx` |
| Fuentes para regenerar el PDF y la maqueta | `marca/pdf-fuente-v2/` |

También hay un sistema de diseño publicado (https://claude.ai/artifact/TSSiUPGXJFENHWvWw1saFa), pero **está desactualizado**: tiene los colores y la tipografía anteriores al kit.

## Marca (del kit oficial del cliente, "SV - Kit de MARCA", 2024)

- **Logo:** la palabra silvestre en Harabara Mais. **SIL** y **TRE** van en naranja y **VES** en verde, con una rama verde a la derecha y la bajada "máquinas y jardines". Hay versión horizontal y apilada.
- **Colores principales:** verde `#39A935` y naranja `#F29100`.
- **Colores secundarios:** `#559E72`, `#93E98B`, `#EAF9C7`, `#C16F1E`, `#FFAF8D`, `#FFCDBB`.
- **Derivados para la web** (para que se lea bien):
  - Botones `#2E7D32`, con `#1E5A23` al pasar el mouse.
  - Fondos oscuros `#143D18`, texto `#1A1A1A`, arena `#F7F6F2`.
  - Nunca texto blanco sobre el naranja ni sobre el verde `#39A935`.
- **Tipografías:**
  - Del kit: Harabara Mais (de marca) y Helvetica LT Std (secundaria). El kit usa la **versión Demo** de Harabara, que no permite uso comercial: hay que comprar la licencia.
  - En la web: Montserrat para títulos y Helvetica o Arial para textos.
- **Fotos:** ambiente verde fuera de foco y con grano, como la portada del kit. Producto sobre fondo blanco, cuadrado, de 1200 px como mínimo. Faltan fotos en acción en paisajes de Mendoza.
- **Voz:** como el vendedor de mostrador que sabe. Tratamos de vos, frases claras y concretas, primero el uso y después el dato técnico, siempre con tildes.

## Decisiones para la tienda (ver maqueta y guía de Ipanema)

- **Encabezado:** barra de anuncios oscura (envíos, retiro en Maipú, cuotas). Logo a la izquierda, buscador visible al centro, y Asesoramiento, Cuenta y Carrito a la derecha.
- **Menú por uso:** Corte de césped, Desmalezado, Motosierras y poda, Soplado, Agua, Línea a batería, Herramientas, Repuestos, Marcas y Ofertas.
- **Portada, en orden:**
  1. Banner principal con la promesa y dos botones: Ver productos y Hablá con un asesor.
  2. Dos promos de temporada.
  3. Franja de confianza.
  4. Categorías.
  5. "Elegí por tu terreno": jardín, quinta o finca.
  6. Más vendidos.
  7. Banner de la línea eléctrica y a batería.
  8. Marcas.
  9. Servicio y local.
  10. Newsletter.
  11. Pie oscuro con los datos legales y el botón de arrepentimiento.
- **Título de producto:** tipo + marca + modelo + dato clave. Ejemplo: "Motosierra eléctrica STIHL MSE 141, 1400 W".

## Mercado Libre

- La cuenta se abre a nombre del titular del CUIT (persona física), con un mail y un celular de la empresa. La consultora entra como colaboradora, sin usar la clave del dueño.
- **Riesgo principal:** confirmar por escrito con STIHL qué permite publicar online, si hay precio mínimo sugerido y si STIHL tiene tienda oficial en ML.
- **Catálogo:** hace falta el EAN de cada producto. Conviene arrancar por repuestos y consumibles.
- **Lo más vendido este año en ML** (export Jardín 2026):
  - STIHL: FS 230, MS 182, MS 172, MS 250 y FS 55. Muchos repuestos con poca competencia, como las cuchillas Polycut.
  - Tramontina: bordeadora eléctrica de 1500 W.
  - Niwa: DNW-52.
  - Bahco: GS-76.
  - Fiasa: FC1111400.

## Calculadora de rentabilidad

- **Hoja Directa:** IVA de venta y de compra con desplegable de 21 % o 10,5 %.
- **Hoja Productos:** calculadora en fila, hasta 300 productos, con precio, envío, comisión, costo fijo, impuestos, utilidad y margen.
- **Cruce con el precio más bajo de ML:** a partir de un margen objetivo calcula el costo máximo sin IVA y con IVA.
- **Pendiente de definir con el cliente:**
  - Los tramos del costo fijo: la fórmula usa $ 1.000, $ 2.000 y $ 2.400, y la hoja Datos dice $ 1.095, $ 2.190 y $ 2.628.
  - Otros impuestos: la celda muestra 4,5 %, pero el cálculo usa 4,7 %.
  - Los precios de ML precargados son promedios del año: hay que reemplazarlos por los actuales.

## Próximo paso

**Editar el borrador de Tiendanube (Ipanema)** desde una sesión con acceso al Chrome del usuario, siguiendo `02-tiendanube-ipanema.md`:
1. Base visual.
2. Categorías.
3. Encabezado.
4. Portada.
5. Ficha de producto.
6. Pie y páginas.
7. Primeros productos.

No publicar la tienda ni tocar pagos, envíos ni datos fiscales sin confirmar con el usuario.

## Pendientes del cliente

- Licencia de Harabara Mais.
- Fotos en acción y fotos de producto en alta calidad.
- Logos oficiales de cada marca.
- Autorización de STIHL y formato del sello de distribuidor oficial.
- Mail con dominio propio, horarios del local y cuotas que se van a ofrecer.
- ¿Tienen servicio técnico propio?
- EAN, peso y medidas de cada producto.
