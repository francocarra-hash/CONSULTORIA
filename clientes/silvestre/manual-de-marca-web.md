# Silvestre: manual de marca para la web nueva

> Guía para desarrollar la tienda nueva en Tiendanube, más pensada para vender online, y para que todo se vea y hable igual: web, Mercado Libre, redes y WhatsApp.
>
> **v2.0, 26/10/2026.** Basado en el **kit de marca del cliente** (`SV - Kit de MARCA`, marzo 2024: logo, colores y tipografías), en capturas de [silvestre.com.ar](https://www.silvestre.com.ar/) y en la lista de marcas que pasó el cliente.
>
> Versión visual: [`marca/silvestre-manual-de-marca.pdf`](marca/silvestre-manual-de-marca.pdf). Logos en vector: [`marca/logos/`](marca/logos/). Maqueta de la portada de la tienda: [`web/portada-prototipo.html`](web/portada-prototipo.html).
>
> Las variables para el desarrollo están en [`marca/silvestre-tokens.css`](marca/silvestre-tokens.css).

## Resumen rápido

| Elemento | Valor |
|---|---|
| Nombre | **Silvestre** (bajada: *máquinas y jardines*) |
| Naranja Silvestre | `#F29100`: color principal del kit. Logo (SIL y TRE), ofertas, acentos |
| Verde Silvestre | `#39A935`: color principal del kit. Logo (VES, rama y bajada), íconos |
| Verde acción | `#2E7D32`: botones y links (texto blanco encima) |
| Verde claro | `#EAF9C7`: secundario del kit. Secciones de apoyo |
| Texto | `#1A1A1A` |
| Tipografía | Del kit: **Harabara Mais** (marca) y **Helvetica LT Std** (secundaria). En la web: **Montserrat** para títulos y Helvetica para textos |
| Voz | Especialista de mostrador: claro, práctico, de confianza |

---

## 1. La web actual: qué mantener y qué cambiar

**Mantener:**

- El **logo** y sus dos colores, naranja y verde. Son reconocibles y conectan con el rubro.
- La **barra superior** con envíos y retiro en Maipú (pasa a fondo oscuro con íconos naranja, para que se lea).
- El **pie de página verde claro**: es amable y separa bien el cierre de la página.
- El **botón de WhatsApp** fijo abajo a la derecha.
- La frase *"Somos distribuidores oficiales STIHL y especialistas en máquinas y herramientas para jardín y campo"*. Es el mejor texto de la web y tiene que subir de jerarquía.

**Cambiar:**

| Hoy | Problema | En la web nueva |
|---|---|---|
| Menú con solo Inicio, Productos y Contacto | El cliente no encuentra por dónde empezar | Menú por categorías de uso, más Marcas (sección 10) |
| "Bienvenido a nuestra Tienda online" como título principal | No dice qué venden ni por qué comprarles | Título con la propuesta y botón de compra (sección 6) |
| Foto de portada de troncos de pino, desenfocada | No muestra productos ni Mendoza ni uso | Banners con producto + uso real + oferta |
| "Ver productos" como link subrayado | No parece un botón y casi no se ve | Botón verde de acción |
| Listado de productos **sin precio** | La primera pregunta del comprador queda sin responder | Precio y cuotas siempre visibles en la tarjeta |
| Títulos mezclados: "Motosierra MS 162" y "MOTOSIERRA ELECTRICA MSE 141" | Se ve descuidado, sin tilde y sin marca | Fórmula fija de título (sección 11) |
| Fotos de producto de distintos tamaños y alineación | La grilla se ve desordenada | Fotos cuadradas, mismo encuadre (sección 8) |
| Texto blanco sobre naranja en la barra superior | Contraste 2,4:1, se lee mal | Texto casi negro sobre naranja (7,3:1) |
| Botón "Enviar" verde claro `#62C659` con texto blanco | Contraste 2,2:1 | Verde acción `#2E7D32` (5,1:1) |
| Teléfono repetido dos veces, sin formato | Confunde | Un solo número: **(261) 242-6888**, con link a WhatsApp |
| Mail @gmail.com | Resta confianza en compras grandes | Mail con dominio propio, por ejemplo `ventas@silvestre.com.ar` |

## 2. Quiénes somos

**Silvestre Máquinas y Jardines.** Casa especializada en máquinas y herramientas para jardín, parque y campo, en **Tropero Sosa 175, Maipú, Mendoza**. **Distribuidor oficial STIHL** y multimarca.

**Frase de posicionamiento** *(propuesta)*:

> **Máquinas para tu jardín y tu campo, con el asesoramiento de quien las conoce.**

**Por qué comprarnos** (los 4 argumentos de toda la web, en este orden):

1. **Somos especialistas.** Te ayudamos a elegir la máquina para tu terreno y tu uso.
2. **Marcas originales y garantía oficial.** Distribuidor oficial STIHL y marcas líderes.
3. **Repuestos y servicio** *(confirmar si tienen taller propio)*. No te dejamos solo después de la compra.
4. **Envíos a todo el país y retiro en Maipú.**

## 3. Logo

**Cómo es:** la palabra **silvestre** en Harabara Mais, partida por color: **SIL** y **TRE** en naranja `#F29100`, **VES** en verde `#39A935`. A la derecha, una **rama verde** que la cierra como un paréntesis. Debajo, la bajada **máquinas y jardines** en verde. El kit trae dos versiones: **horizontal** y **apilada** (SIL / VES / TRE).

**Versiones** (en vector en [`marca/logos/`](marca/logos/), sacadas del kit):

| Versión | Archivo | Uso |
|---|---|---|
| Horizontal color | `logo-horizontal.svg` | Encabezado de la web, documentos, Mercado Libre |
| Apilada color | `logo-apilado.svg` | Espacios cuadrados: perfil de redes, ícono de la tienda |
| Blanco | `logo-horizontal-blanco.svg`, `logo-apilado-blanco.svg` | Sobre fotos y sobre verde oscuro (como en la portada del kit) |
| Una tinta | `logo-horizontal-negro.svg`, `logo-apilado-negro.svg` | Facturas, sellos, usos de un solo color |

**Reglas:**

- **Fondos permitidos:** el logo color va sobre blanco, arena o verde claro `#EAF9C7`. Sobre fotos o verde oscuro va la versión blanca. Nunca el logo color sobre naranja ni sobre fotos: se pierden SIL y TRE.
- **Área de respeto:** alrededor del logo, un espacio libre igual al alto de la letra "s".
- **Tamaño mínimo:** 140 px de ancho con bajada, 100 px sin bajada. Debajo de 140 px la bajada no se lee: usar la versión sin bajada.
- **En el encabezado:** 200 px de ancho en computadora y entre 120 y 140 px en celular. En la tienda nueva va a la izquierda, con el buscador al centro (ver la maqueta).
- **No:** estirar, rotar, cambiar los colores, separar la rama de la palabra, agregar sombras o contornos, ni escribir "Silvestre" con otra letra en lugar del logo.

## 4. Colores

### De marca (kit oficial)

| Nombre | Hex | RGB | Uso |
|---|---|---|---|
| **Verde Silvestre** | `#39A935` | 57, 169, 53 | Principal. Logo, íconos grandes, estado en stock |
| **Naranja Silvestre** | `#F29100` | 242, 145, 0 | Principal. Logo, etiquetas de oferta, promos de temporada |
| Salvia | `#559E72` | 85, 158, 114 | Secundario. Detalles gráficos |
| Menta | `#93E98B` | 147, 233, 139 | Secundario. Ilustraciones y fondos de piezas gráficas |
| Verde claro | `#EAF9C7` | 234, 249, 199 | Secundario. Secciones de apoyo, etiqueta de envío gratis |
| Terracota | `#C16F1E` | 193, 111, 30 | Secundario. Acentos cálidos en piezas gráficas |
| Durazno | `#FFAF8D` | 255, 175, 141 | Secundario. Fondos de piezas gráficas |
| Rosa arena | `#FFCDBB` | 255, 205, 187 | Secundario. Fondos de piezas gráficas |

### Para la web (derivados del verde del kit, para que todo se lea bien)

| Nombre | Hex | Uso |
|---|---|---|
| **Verde acción** | `#2E7D32` | Botones principales y links |
| Verde acción, al pasar el mouse | `#1E5A23` | Estado *hover* de botones y links |
| Verde noche | `#143D18` | Fondos oscuros: portada, bloques de servicio |
| Arena | `#F7F6F2` | Fondos de tarjetas y secciones |
| Naranja claro | `#FFF4E0` | Fondo de avisos y de la franja de cuotas |
| Naranja para texto | `#A35500` | Si hace falta texto naranja sobre blanco (5,5:1) |

### Neutros

| Nombre | Hex | Uso |
|---|---|---|
| Fondo | `#FFFFFF` | Fondo general |
| Superficie | `#F6F6F3` | Fondos de sección, tarjetas |
| Borde | `#E4E4DE` | Líneas y bordes de campos |
| Texto | `#1A1A1A` | Títulos, textos y **precios** |
| Texto secundario | `#5F6368` | Bajadas, datos técnicos, cuotas |
| Error | `#C0392B` | Errores de formularios |

### Reglas de color

1. **Nunca texto blanco sobre naranja ni sobre el verde del logo.** No se lee (2,4:1 y 3,0:1). Sobre naranja va texto `#1A1A1A`.
2. **Los botones de compra son verde acción** con texto blanco. Es el único color "que llama" en la página.
3. **El naranja es acento, no fondo.** Barra superior, etiquetas de oferta y detalles chicos. Los productos STIHL ya son naranjas: si la web usa mucho naranja, las fotos se pierden y las otras marcas parecen de segunda.
4. **Los precios van en `#1A1A1A`**, no en color.
5. **Proporción aproximada:** 70 % blanco y neutros, 15 % verde, 10 % naranja, 5 % texto y detalles.

### Contraste medido (WCAG 2.1)

| Combinación | Contraste | Resultado |
|---|---|---|
| `#1A1A1A` sobre `#FFFFFF` | 17,4:1 | AAA |
| `#1A1A1A` sobre `#F29100` (barra superior) | 7,3:1 | AAA |
| Blanco sobre `#2E7D32` (botón) | 5,1:1 | AA |
| `#1E5A23` sobre `#EAF9C7` (textos del pie) | 7,4:1 | AAA |
| `#5F6368` sobre `#FFFFFF` | 6,1:1 | AA |
| Blanco sobre `#F29100` | 2,4:1 | **No usar** |
| Blanco sobre `#39A935` | 3,0:1 | **No usar** en textos chicos |
| Blanco sobre `#93E98B` | 1,5:1 | **No usar** |
| Blanco sobre `#62C659` (botón actual) | 2,2:1 | **No usar** |
| `#559E72` sobre `#EAF9C7` (textos del pie actual) | 2,9:1 | **No usar** |

## 5. Tipografía

Del kit de marca:

- **Harabara Mais** (tipografía de marca): logo, títulos de campaña y piezas gráficas. **Ojo:** el kit usa la versión *Demo*, que no habilita uso comercial. Hay que comprar la licencia completa (y la licencia web si se quiere usar en la tienda).
- **Helvetica LT Std** (secundaria, en todas sus variantes): textos, precios y datos. Es una fuente paga; en la web se usa la Helvetica del sistema con Arial de respaldo.

En la web, mientras no haya licencia web de Harabara:

- **Títulos:** **Montserrat**, peso 700 u 800. Es la que el kit usa para rótulos y es gratuita en Google Fonts.
- **Textos, precios y botones:** `"Helvetica Neue", Helvetica, Arial, sans-serif`.

| Elemento | Computadora | Celular | Peso |
|---|---|---|---|
| Título de portada (H1) | 56 px | 36 px | Montserrat 800 |
| Título de sección (H2) | 38 px | 28 px | Montserrat 800 |
| Título de ficha de producto | 28 px | 22 px | Montserrat 800 |
| Nombre en tarjeta de producto | 16 px | 15 px | Helvetica 600 |
| Precio en tarjeta | 20 px | 18 px | Helvetica 700 |
| Precio en ficha | 32 px | 26 px | Helvetica 700 |
| Texto | 16 px | 16 px | Helvetica 400 |
| Datos chicos (cuotas, envío) | 14 px | 13 px | Helvetica 400 |

Interlineado de 1,5 en textos y de 1,2 en títulos. Títulos en **tipo oración** ("Motosierras a batería"), nunca todo en mayúscula.

## 6. Componentes de la web

### Barra superior

- Fondo `#1A1A1A`, texto blanco semibold de 13 px e íconos en naranja `#F29100`. A la derecha, el teléfono de ayuda.
- Máximo tres mensajes, separados por un punto medio: **Envíos a todo el país · Retiro en Maipú · Hasta X cuotas sin interés**.
- En celular, un mensaje por vez, rotando.

### Encabezado

- Logo a la izquierda, **buscador grande al centro** ("Buscá por máquina, marca o modelo") y, a la derecha, Asesoramiento, Mi cuenta y Carrito.
- En celular: menú, logo centrado y carrito arriba, y el buscador a todo el ancho debajo.
- Debajo, el **menú de categorías** (sección 10), con submenú al pasar el mouse.

### Portada (de arriba hacia abajo)

1. **Banner principal:** producto o persona usando una máquina, título corto, bajada y botón. Ejemplo: *"Motosierras STIHL · Hasta 6 cuotas sin interés · [Ver motosierras]"*.
2. **Franja de beneficios** (fondo verde claro): los 4 argumentos de la sección 2, cada uno con un ícono.
3. **Categorías destacadas:** 6 a 8 tarjetas con foto y nombre.
4. **Más vendidos:** grilla de productos.
5. **Marcas:** franja con los logos (sección 9).
6. **Línea a batería** u otra campaña del momento.
7. **Nosotros:** foto del local y una frase. *"Nos encontrás en Tropero Sosa 175, Maipú."*

### Botones

| Tipo | Fondo | Texto | Borde | Uso |
|---|---|---|---|---|
| Principal | `#2E7D32` (hover `#1E5A23`) | Blanco, Helvetica 600 | Ninguno | Comprar, Agregar al carrito, Ver productos |
| Secundario | Transparente | `#2E7D32` | 2 px `#2E7D32` | Ver más, Ver ficha técnica |
| WhatsApp | `#25D366` | `#1A1A1A` | Ninguno | Consultar por WhatsApp (color oficial de WhatsApp) |

Esquinas redondeadas de **8 px**, alto mínimo de **48 px** en celular para tocar fácil.

### Tarjeta de producto

- Foto cuadrada sobre fondo blanco, toda la tarjeta clickeable.
- **Marca** en chico (gris, mayúscula solo si la marca se escribe así), **nombre** debajo, **precio** grande, **cuotas** debajo en gris.
- Etiquetas arriba a la izquierda, máximo dos:
  - **Oferta / % OFF:** fondo `#F29100`, texto `#1A1A1A`.
  - **Envío gratis:** fondo `#EAF9C7`, texto `#1E5A23`.
  - **A batería:** fondo `#F6F6F3`, texto `#1A1A1A`, con ícono de batería.
- Sin stock: foto en gris al 50 % y el texto "Sin stock por ahora".

### Ficha de producto

- Izquierda: galería de fotos. Derecha: marca, título, precio, cuotas, envío y botón de compra.
- Debajo del botón: **Consultar por WhatsApp** y tres sellos chicos: *Garantía oficial · Compra protegida · Retiro en Maipú*.
- Más abajo: descripción, ficha técnica en tabla, qué trae la caja y productos relacionados (repuestos y accesorios del mismo modelo).

### Pie de página

- Arriba, franja de newsletter en verde claro `#EAF9C7` con textos `#1E5A23`.
- El pie en sí va en `#1A1A1A` con textos blancos al 78 % y el logo en versión blanca.
- Columnas: **Categorías · Ayuda** (envíos, cambios, garantía, cómo comprar) **· Contacto · Seguinos**.
- Contacto: (261) 242-6888 · mail de dominio propio · Tropero Sosa 175, Maipú, Mendoza · horarios · mapa.
- Mantener lo legal: razón social y CUIT, Defensa del Consumidor y botón de arrepentimiento (es obligatorio).

### Íconos

Línea simple de 1,5 a 2 px, esquinas redondeadas (combinan con el logo), un solo color: `#2E7D32` sobre fondos claros. Íconos fijos para: envío, retiro en local, cuotas, garantía, servicio técnico, WhatsApp, batería, nafta y eléctrico.

## 7. Voz y tono

**Cómo somos:** el vendedor de mostrador que sabe. Práctico, claro, de confianza.

| Somos | No somos |
|---|---|
| Expertos que explican simple | Técnicos que hablan en código |
| Cercanos (tratamos de **vos**) | Informales de más |
| Concretos: datos, usos, medidas | Exagerados ("¡¡la mejor del mercado!!") |
| Honestos: si no te sirve, te lo decimos | Vendedores a cualquier costo |

**Reglas:** primero el **uso** y después el dato técnico. Frases cortas. Números con unidad y formato argentino (**$ 1.250.000**, **45,4 cc**, **40 cm**). Como mucho un signo de exclamación por pantalla. Siempre con tildes: *eléctrica, batería, jardín, máquinas*.

| En vez de | Escribimos |
|---|---|
| "Bienvenido a nuestra Tienda online" | "Máquinas para tu jardín y tu campo" |
| "¡¡Súper ofertas imperdibles!!" | "Motosierras STIHL con hasta 6 cuotas sin interés" |
| "Producto de excelente calidad" | "Motor de 2 tiempos de 45,4 cc, ideal para leña y poda" |
| "Consulte disponibilidad" | "¿Tenés dudas? Escribinos por WhatsApp y te asesoramos" |
| "Consultar Envíos" | "Envíos a todo el país" |

**Textos fijos de la tienda:**

| Lugar | Texto |
|---|---|
| Botón de compra | **Comprar** |
| Botón secundario | **Agregar al carrito** |
| Consulta | **Consultar por WhatsApp** |
| Buscador | *Buscá por máquina, marca o modelo* |
| Sin stock | **Sin stock por ahora.** Avisame cuando llegue |
| Garantía | **Garantía oficial [marca]** + plazo |
| Newsletter | *Recibí ofertas y novedades. Sin spam.* |

## 8. Fotos

**De producto** (en la web y en Mercado Libre):

- Fondo **blanco puro**, producto entero ocupando el 85 % del cuadro, **centrado** y con el mismo margen en todas.
- **Cuadradas, mínimo 1200 × 1200 px.**
- Las motosierras y cortacercos, que son alargados, van en diagonal o con más margen arriba y abajo, para que se vean del mismo tamaño que el resto en la grilla.
- Sin logos, textos ni marcas de agua encima.
- Orden: 1) de tres cuartos, 2) lateral, 3) detalle del motor o cabezal, 4) qué trae la caja, 5) en uso.

**De ambiente** (banners, categorías, redes):

- **Mendoza real:** jardines, parques, fincas, viñedos, montaña. Nos diferencia de una tienda de Buenos Aires.
- Gente usando las máquinas **con el equipo de protección puesto**. Nunca un uso inseguro.
- Luz natural, sin filtros fuertes. La foto de bosque de la portada actual puede quedar como fondo de la sección "Nosotros", no como portada.

## 9. Las marcas que vendemos

**Reglas:**

- Solo **logos oficiales**, del kit de cada marca o del proveedor. Nunca recortados de una foto.
- En la franja de marcas, todos del **mismo tamaño visual**, sobre blanco o gris muy claro.
- El sello **"Distribuidor oficial STIHL"** se usa con el formato y la autorización de STIHL. Pedirlo.
- Las marcas van **dentro** de la tienda Silvestre: encabezado, colores y botones siempre son de Silvestre.

| Marca | Qué vendemos | Notas |
|---|---|---|
| **STIHL** | Máquinas y repuestos | Marca principal, primera en la franja. Confirmar qué permite publicar online |
| **Oleo-Mac** | Cortadoras, tanzas, repuestos | Se escribe con guion |
| **Fiasa** | Cortadoras, repuestos | |
| **MTD / Yard Machines** | Tractores | Confirmar si se muestra como "Yard Machines by MTD" |
| **Tramontina** | Bordeadoras, accesorios y herramientas de jardín | |
| **Bahco** | Herramientas de poda | Aclarar que trabajamos la línea de poda |
| **Picasso** | Semillas de césped | |
| **Niwa** | Máquinas para jardinería | |
| **Konan** | Algunas máquinas para jardín | Mostrar solo los modelos que trabajan |
| **Dowen Pagio** | Robots cortacésped y de piscina | Los de piscina en categoría aparte. Confirmar cómo se escribe |
| **BTA** | Desmalezadoras | |

## 10. Organización de la tienda

El menú va **por uso**. La marca es un filtro y tiene su propia página.

1. **Corte de césped:** cortadoras, tractores, robots cortacésped
2. **Desmalezado y bordeado:** desmalezadoras, bordeadoras
3. **Motosierras y poda:** motosierras, podadoras de altura, cortacercos, herramientas de poda
4. **Soplado y limpieza:** sopladoras, aspiradoras
5. **Agua:** motobombas, robots de piscina
6. **Línea a batería:** máquinas a batería, baterías y cargadores
7. **Césped y semillas**
8. **Herramientas de jardín**
9. **Repuestos y accesorios:** cadenas, espadas, tanzas, cabezales, aceites, filtros, protección personal
10. **Marcas**

**Filtros:** marca, tipo de motor (nafta, batería, eléctrico), uso (hogar o profesional), precio y, según la categoría, potencia, ancho de corte o largo de espada.

## 11. Fichas de producto

**Título: tipo de producto + marca + modelo + dato clave**, en tipo oración y con tildes.

| Hoy | Nuevo |
|---|---|
| Motosierra MS 162 | Motosierra STIHL MS 162, espada 30 cm |
| MOTOSIERRA ELECTRICA MSE 141 | Motosierra eléctrica STIHL MSE 141, 1400 W |
| SOPLADOR BGE 71 | Soplador eléctrico STIHL BGE 71 |
| CORTACERCO HSE 61 | Cortacerco eléctrico STIHL HSE 61 |

*(Confirmar espada y potencia de cada modelo con la ficha oficial antes de cargarlos.)*

**Descripción:** 1) para qué sirve, en dos líneas · 2) lo que más importa, en 3 a 5 puntos · 3) ficha técnica en tabla · 4) qué trae la caja · 5) garantía y servicio · 6) cierre con invitación a WhatsApp.

**Datos obligatorios:**

| Tipo | Datos |
|---|---|
| A nafta | Cilindrada (cc), potencia (kW o HP), 2 o 4 tiempos, tanque (l), peso (kg) |
| A batería | Voltaje (V), **batería y cargador incluidos o no**, autonomía, peso |
| Eléctricas | Potencia (W), largo de cable |
| Cortadoras | Ancho de corte (cm), alturas de corte, bolsa (l), tracción o empuje |
| Motosierras | Largo de espada (cm), paso de cadena |
| Desmalezadoras | Cabezal (tanza o cuchilla), diámetro de tanza, manillar |
| Todas | **Código de barras (EAN)**, medidas y peso **con caja** |

## 12. Coherencia con Mercado Libre

- Mismo nombre, mismo ícono de perfil, mismos títulos y mismas fotos.
- Mismos precios de lista, salvo que se defina otra política por canal. Ver [publicación en catálogo](03-publicar-en-catalogo.md).

## 13. Cómo aplicarlo en Tiendanube

1. **Plantilla:** elegir una con encabezado centrado, menú desplegable por categorías, barra de anuncios y tarjetas de producto con precio y cuotas.
2. **Personalizar diseño → Colores:** cargar fondo `#FFFFFF`, textos `#1A1A1A`, botones `#2E7D32` con texto blanco, barra de anuncios `#1A1A1A` con texto blanco, y pie `#1A1A1A` con el logo blanco.
3. **Personalizar diseño → Tipografía:** elegir Montserrat para títulos y Helvetica (o Arial) para textos. Si hay licencia web de Harabara Mais, se puede cargar por CSS para los títulos.
4. **CSS avanzado:** si el plan permite editar el CSS, pegar [`marca/silvestre-tokens.css`](marca/silvestre-tokens.css). Primero hay que mapear las variables a las clases de la plantilla elegida. Revisar en el plan del cliente si está disponible la edición de CSS.
5. **Logo:** subir el SVG o un PNG de al menos 440 px de ancho (doble resolución). Favicon: el ícono cuadrado de 512 × 512 px.
6. **Revisar en celular** antes de publicar: barra superior, menú, tarjeta de producto, ficha y checkout.

## Pendientes

- [x] Logo original en vector y colores oficiales (vienen en el kit)
- [ ] Licencia comercial de Harabara Mais (el kit usa la versión Demo)
- [ ] Fotos en acción de las máquinas trabajando (ver la lista de tomas en el PDF)
- [ ] Logos oficiales de cada marca, en vector
- [ ] Armar las versiones blanca, una tinta e ícono
- [ ] Confirmar las tipografías de la propuesta
- [ ] Mail con dominio propio
- [ ] Confirmar horarios, WhatsApp de ventas y si tienen servicio técnico propio
- [ ] Usuarios de Instagram y Facebook
- [ ] Sello "Distribuidor oficial STIHL" y kits de logos de cada marca
- [ ] Fotos del local y del equipo para "Nosotros"
- [ ] Elegir la frase de posicionamiento
- [ ] Elegir la plantilla de Tiendanube y revisar si el plan permite editar CSS
