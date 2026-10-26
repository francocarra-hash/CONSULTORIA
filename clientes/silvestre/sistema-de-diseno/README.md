Silvestre Máquinas y Jardines es una casa especializada en máquinas y herramientas para jardín, parque y campo, en Tropero Sosa 175, Maipú, Mendoza. Es distribuidor oficial STIHL y multimarca. Este sistema sirve para armar la tienda en Tiendanube y para que la web, Mercado Libre, las redes y WhatsApp se vean y hablen igual. Usá el nombre **Silvestre**, con la bajada *máquinas y jardines*.

## Contenido

### Voz

Escribí como el vendedor de mostrador que sabe: práctico, claro y de confianza. Tratá al cliente de **vos**. Sin emojis en la tienda.

| Somos | No somos |
|---|---|
| Expertos que explican simple | Técnicos que hablan en código |
| Cercanos | Informales de más |
| Concretos: datos, usos, medidas | Exagerados ("¡¡la mejor del mercado!!") |
| Honestos: si no te sirve, te lo decimos | Vendedores a cualquier costo |

- Contá primero el **uso** y después el dato técnico.
- Escribí frases cortas, una idea por frase.
- Escribí números con unidad y formato argentino: **$ 1.250.000**, **45,4 cc**, **40 cm**, **1400 W**.
- Usá como mucho un signo de exclamación por pantalla.
- Poné siempre las tildes: *eléctrica, batería, jardín, máquinas*.
- Escribí títulos en tipo oración ("Motosierras a batería"), nunca todo en mayúscula. La excepción son las marcas que se escriben así, como STIHL.

| En vez de | Escribí |
|---|---|
| "Bienvenido a nuestra Tienda online" | "Máquinas para tu jardín y tu campo" |
| "¡¡Súper ofertas imperdibles!!" | "Motosierras STIHL con hasta 6 cuotas sin interés" |
| "Producto de excelente calidad" | "Motor de 2 tiempos de 45,4 cc, ideal para leña y poda" |
| "Consulte disponibilidad" | "¿Tenés dudas? Escribinos por WhatsApp y te asesoramos" |
| "Consultar Envíos" | "Envíos a todo el país" |

### Textos fijos

| Lugar | Texto |
|---|---|
| Botón de compra | **Comprar** |
| Botón secundario | **Agregar al carrito** |
| Consulta | **Consultar por WhatsApp** |
| Buscador | *Buscá por máquina, marca o modelo* |
| Sin stock | **Sin stock por ahora.** Avisame cuando llegue |
| Garantía | **Garantía oficial [marca]** + plazo |
| Newsletter | *Recibí ofertas y novedades. Sin spam.* |

### Por qué comprarnos

Repetí estos cuatro argumentos en la portada, en la ficha y en Mercado Libre, en este orden:

1. **Somos especialistas.** Te ayudamos a elegir la máquina para tu terreno y tu uso.
2. **Marcas originales y garantía oficial.** Distribuidor oficial STIHL y marcas líderes.
3. **Repuestos y servicio.** No te dejamos solo después de la compra.
4. **Envíos a todo el país y retiro en Maipú.**

## Fundamentos visuales

### Color

- Pintá el fondo de la tienda en `fondo` y los textos y **precios** en `texto`.
- Usá `verde-accion` para todos los botones principales y links, con `sobre-accion` encima, y `verde-accion-hover` al pasar el mouse.
- Usá `naranja` como acento: barra superior, etiqueta de oferta y detalles chicos. Los productos STIHL ya son naranjas: si la tienda usa mucho naranja, las fotos se pierden y las otras marcas parecen de segunda.
- **Nunca pongas texto blanco sobre `naranja` ni sobre `verde`.** No se lee. Sobre `naranja` va `texto`.
- Usá `verde-claro` para el pie y la franja de beneficios, con textos en `verde-accion-hover`.
- Proporción aproximada: 70 % `fondo` y neutros, 15 % verdes, 10 % `naranja`, 5 % texto y detalles.
- El color de `whatsapp` va solo en el botón de consulta.

### Tipografía

- Poné los títulos en la familia `titulos` (Nunito, 700 y 800). Es redondeada y acompaña al logo.
- Poné textos, precios y botones en la familia `texto` (Nunito Sans, 400, 600 y 700).
- Las dos son de Google Fonts. Si la plantilla de Tiendanube no las ofrece, cargalas por CSS o elegí la más parecida.
- Usá solo los estilos del sistema: `titulo-portada`, `titulo-seccion`, `titulo-ficha`, `precio-ficha`, `precio-tarjeta`, `nombre-tarjeta`, `boton`, `cuerpo`, `chico`, `barra` y `etiqueta`. Cada uno dice su tamaño en celular.

### Espacios, bordes y radios

- Dejá `space-4` de margen lateral en celular y `space-12` entre secciones en computadora (`space-8` en celular).
- Redondeá botones, campos y tarjetas con `radius-md`, etiquetas con `radius-sm` y banners con `radius-lg`.
- Separá con `borde`, no con sombras. La única sombra es la de la tarjeta de producto al pasar el mouse.
- Dale a los botones y campos un alto mínimo de `boton-alto`.
- Marcá el foco del teclado con un anillo sólido de 2px en `verde-accion-hover`, separado 2px del elemento.

### Fotos

- **Producto:** fondo `fondo` puro, cuadradas, de mínimo 1200 × 1200 px, producto entero y centrado ocupando el 85 % del cuadro. Las piezas alargadas, como motosierras y cortacercos, van con más margen arriba y abajo para que se vean del mismo tamaño en la grilla. Sin logos, textos ni marcas de agua encima. Orden: de tres cuartos, lateral, detalle, qué trae la caja, en uso.
- **Ambiente:** Mendoza real (jardines, parques, fincas, viñedos, montaña), luz natural, sin filtros fuertes. La gente usa las máquinas **con el equipo de protección puesto**.

### Diseño de página

- Encabezado como el actual: buscador a la izquierda, logo al centro y cuenta y carrito a la derecha. Debajo va el menú de categorías.
- Portada, de arriba hacia abajo: banner principal, franja de beneficios, categorías destacadas, más vendidos, marcas, una campaña y "Nosotros".
- Diseñá primero para celular: la mayoría de las visitas llegan por ahí.

## Logo

Usá `silvestre-logo-captura.png` (grupo Logos) solo como referencia: está recortado de una captura de la web. Para producción hace falta el archivo original en vector. El logo es la palabra **silvestre** en minúscula, redondeada y en `naranja`, con una rama `verde` a la derecha y la bajada *máquinas y jardines* en `verde`.

- Ponelo sobre `fondo`, `verde-claro` o fotos con una zona limpia. **Nunca sobre `naranja`.**
- Dejá alrededor un espacio libre igual al alto de la letra "s".
- Tamaño mínimo: 140 px de ancho con bajada y 100 px sin bajada.
- En el encabezado, `logo-encabezado` de ancho en computadora y entre 120 y 140 px en celular, centrado.
- No lo estires, rotes ni recolores. No separes la rama de la palabra, no le agregues sombras ni contornos y no escribas "Silvestre" con otra letra en su lugar.
- Faltan armar las versiones blanca, de una tinta (`texto`) e ícono cuadrado para favicon, Mercado Libre, Instagram y WhatsApp.

## Iconografía

Usá íconos de línea de 1,5 a 2 px con esquinas redondeadas, en `verde-accion` sobre fondos claros. Íconos fijos: envío, retiro en local, cuotas, garantía, servicio técnico, WhatsApp, batería, nafta y eléctrico. El sistema todavía no tiene un set propio: elegí uno abierto de línea redondeada y usalo para todo.

## Marcas que vendemos

- Usá solo los logos oficiales de cada marca, sacados de su kit o pedidos al proveedor. Nunca recortados de una foto.
- En la franja de marcas, poné todos los logos del mismo tamaño visual sobre `fondo` o `superficie`.
- El sello "Distribuidor oficial STIHL" se usa con el formato y la autorización de STIHL.
- Las marcas van dentro de la tienda Silvestre: encabezado, colores y botones siempre son de Silvestre.

| Marca | Qué vendemos |
|---|---|
| STIHL | Máquinas y repuestos. Marca principal, primera en la franja |
| Oleo-Mac (con guion) | Cortadoras, tanzas, repuestos |
| Fiasa | Cortadoras, repuestos |
| MTD / Yard Machines | Tractores |
| Tramontina | Bordeadoras, accesorios y herramientas de jardín |
| Bahco | Herramientas de poda |
| Picasso | Semillas de césped |
| Niwa | Máquinas para jardinería |
| Konan | Algunas máquinas para jardín |
| Dowen Pagio | Robots cortacésped y de piscina (los de piscina, en categoría aparte) |
| BTA | Desmalezadoras |
