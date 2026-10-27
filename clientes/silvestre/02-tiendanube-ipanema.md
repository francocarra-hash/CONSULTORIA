# Silvestre: paso 2, armar la tienda en Tiendanube (plantilla Ipanema)

> Guía para pasar el [manual de marca](manual-de-marca-web.md) y la [maqueta de la portada](web/portada-prototipo.html) al borrador en Tiendanube con la plantilla Ipanema. Ipanema está armada con **secciones y bloques** que se agregan, quitan y reordenan, y colores, tipografías y botones se definen una sola vez para toda la tienda ([ayuda de Tiendanube](https://ayuda.tiendanube.com/es_AR/diseno-ipanema/como-personalizar-mi-diseno-ipanema)).
>
> Los nombres exactos de los menús del editor pueden variar: seguir la opción más parecida.
>
> Borrador del 27/10/2026.

## Orden de trabajo

1. Base visual: colores, tipografía, botones y logo.
2. Categorías y menú.
3. Encabezado y barra de anuncios.
4. Portada, sección por sección.
5. Ficha de producto y listado.
6. Pie de página y páginas institucionales.
7. Carga de los primeros productos.
8. Revisión en celular.

## 1. Base visual (Editor de diseño → configuración general)

**Colores:**

| Uso en el editor | Color |
|---|---|
| Fondo | `#FFFFFF` |
| Textos | `#1A1A1A` |
| Botón principal (fondo / texto) | `#2E7D32` / `#FFFFFF` |
| Botón principal al pasar el mouse | `#1E5A23` |
| Links y acentos | `#2E7D32` |
| Etiqueta de oferta o descuento | `#F29100` con texto `#1A1A1A` |
| Fondos de sección alternativos | `#F7F6F2` (arena) o `#EAF9C7` (verde claro) |
| Secciones oscuras | `#143D18` con texto blanco |

**No usar** texto blanco sobre el naranja `#F29100` ni sobre el verde del logo `#39A935`: no se lee.

**Tipografía:** títulos en **Montserrat** (Bold/ExtraBold), textos en **Helvetica** o la más parecida de la lista (Arial, Inter o Roboto). Si Montserrat no está, cargarla por CSS (sección 9).

**Botones:** esquinas levemente redondeadas (8 px), texto en tipo oración ("Agregar al carrito"), nunca todo en mayúscula.

**Logo:**
- Encabezado: `marca/logos/logo-horizontal.svg` (o un PNG de al menos 440 px de ancho).
- Pie oscuro: `marca/logos/logo-horizontal-blanco.svg`.
- Favicon: armar uno cuadrado de 512 × 512 a partir de `logo-apilado.svg` o de la rama sola.

## 2. Categorías (Productos → Categorías) y menú principal

Crear este árbol. El menú principal muestra el primer nivel.

- **Corte de césped:** Cortadoras a nafta · Cortadoras eléctricas · Cortadoras a batería · Tractores de jardín · Robots cortacésped
- **Desmalezado y bordeado:** Desmalezadoras · Bordeadoras
- **Motosierras y poda:** Motosierras a nafta · Motosierras eléctricas y a batería · Podadoras de altura · Cortacercos · Herramientas de poda
- **Soplado y limpieza:** Sopladoras · Aspiradoras
- **Agua:** Motobombas · Robots de piscina
- **Línea a batería**
- **Césped y semillas**
- **Herramientas de jardín**
- **Repuestos y accesorios:** Cadenas y espadas · Tanzas y cabezales · Cuchillas · Aceites y lubricantes · Filtros · Motores · Protección personal
- **Marcas** (link a una página o a una categoría por marca)
- **Ofertas** (al final del menú, en naranja si la plantilla lo permite)

Filtros a activar en el listado: marca, precio y, si se cargan como propiedades, tipo de motor (nafta, eléctrico, batería).

## 3. Encabezado y barra de anuncios

- **Barra de anuncios:** fondo `#1A1A1A`, texto blanco. Mensajes: *Envíos a todo el país · Retiro gratis en Maipú · Hasta 6 cuotas sin interés* (ajustar las cuotas a lo que se ofrezca de verdad).
- **Encabezado:** logo a la izquierda, **buscador visible** (no solo la lupa) con el texto *Buscá por máquina, marca o modelo*, y a la derecha cuenta y carrito.
- **Menú:** el árbol del punto 2 debajo del logo.

## 4. Portada (agregar secciones en este orden)

| # | Sección de Ipanema | Contenido |
|---|---|---|
| 1 | Banner / imagen con texto | Fondo: foto del bosque del kit con capa verde oscura. Eyebrow: *Distribuidor oficial STIHL · Maipú, Mendoza*. Título: **Máquinas para tu jardín y tu campo.** Texto: *Te asesoramos para que elijas la máquina justa para tu terreno. Con garantía oficial, repuestos y servicio.* Botones: *Ver productos* y *Hablá con un asesor* (link a WhatsApp) |
| 2 | Banners secundarios (2) | *Temporada de poda · Motosierras STIHL · Ver modelos* (fondo naranja) y *Desmalezado · Para terrenos grandes · Ver modelos* (fondo verde claro) |
| 3 | Beneficios / íconos con texto | Distribuidor oficial · Asesoramiento real · Repuestos y servicio · Retiro en Maipú |
| 4 | Categorías destacadas | Título *¿Qué necesitás hacer?*: Corte de césped, Desmalezado, Motosierras y poda, Soplado, Línea a batería, Repuestos |
| 5 | Texto + 3 bloques (o banners con texto) | *Elegí por tu terreno*: Jardín de casa (hasta 500 m²) · Parque o quinta (500 a 3.000 m²) · Finca o campo (más de 3.000 m²), cada uno con link a los equipos que van |
| 6 | Productos destacados | Título *Lo que más se llevan*. Empezar con: Motosierra STIHL MS 162, Desmalezadora STIHL FS 230, Motosierra STIHL MS 182, Desmalezadora STIHL FS 55 (los más vendidos de STIHL en ML este año) |
| 7 | Banner ancho | *Línea eléctrica y a batería · Livianas, silenciosas y sin nafta.* |
| 8 | Logos de marcas | STIHL primero y después el resto, todos del mismo tamaño |
| 9 | Imagen con texto (2) | *No te dejamos solo después de la compra* (repuestos) y *Vení a conocernos a Maipú* (dirección y horarios) |
| 10 | Newsletter | *Recibí ofertas y novedades. Una vez por mes, sin spam.* |

## 5. Ficha de producto y listado

- **Título:** tipo + marca + modelo + dato clave. Ejemplo: *Motosierra STIHL MS 182, espada 40 cm*.
- **Fotos:** cuadradas, fondo blanco, mínimo 1200 × 1200 px.
- **Descripción:** para qué sirve (2 líneas) · lo más importante (3 a 5 puntos) · ficha técnica en tabla · qué trae la caja · garantía · cierre con WhatsApp.
- **Debajo del botón de compra:** cuotas, envío y retiro en Maipú, y botón de WhatsApp.
- **Productos relacionados:** repuestos y accesorios del mismo modelo.
- **Plantilla propia para STIHL** (Ipanema permite plantillas personalizadas por producto): sello de distribuidor oficial (si STIHL lo autoriza) y bloque de garantía oficial.
- **Listado:** precio y cuotas siempre visibles en la tarjeta.

## 6. Pie de página y páginas

- **Pie:** fondo `#1A1A1A`, logo blanco, columnas Categorías · Ayuda · Contacto, medios de pago, newsletter arriba en verde claro.
- **Contacto:** (261) 242-6888 (una sola vez), mail con dominio propio, Tropero Sosa 175, Maipú, Mendoza, horarios.
- **Legales (obligatorios):** razón social y CUIT, link a Defensa del Consumidor y **botón de arrepentimiento**.
- **Páginas a crear:** Cómo comprar · Envíos y retiro · Cambios y devoluciones · Garantía · Nosotros · Preguntas frecuentes.

## 7. Primeros productos

Empezar por lo más vendido de cada marca según [`datos/silvestre-marcas-mas-vendidas-meli-2026.xlsx`](datos/silvestre-marcas-mas-vendidas-meli-2026.xlsx), revisando precio y margen en [`datos/Calculo_Rentabilidad_Silvestre.xlsx`](datos/Calculo_Rentabilidad_Silvestre.xlsx). Cargar **siempre** el código de barras (EAN), el peso y las medidas con caja.

## 8. Revisión en celular

Barra de anuncios, menú, buscador, tarjeta de producto, ficha, botón de WhatsApp y checkout completo con un producto de prueba.

## 9. CSS (si el plan lo permite)

```css
@import url("https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&display=swap");
h1, h2, h3, .h1, .h2, .h3 { font-family: "Montserrat", "Helvetica Neue", Arial, sans-serif; letter-spacing: -0.02em; }
body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; }
```

Las clases exactas de Ipanema hay que verlas en el editor. El resto de las variables está en [`marca/silvestre-tokens.css`](marca/silvestre-tokens.css).

## Pendientes del cliente

- [ ] Fotos de producto en buena calidad y fotos en acción
- [ ] Logos oficiales de cada marca
- [ ] Horarios del local y mail con dominio propio
- [ ] Cuotas sin interés que se van a ofrecer
- [ ] Autorización de STIHL para el sello de distribuidor oficial
