# 6. Números

> Modelo simple, en dólares por mes, para tener órdenes de magnitud. Todo es **estimado**: hay que ajustarlo con datos reales (lo que se le cobra hoy a Lioy, cotizaciones de herramientas, contador).

## Supuestos

| Supuesto | Valor | Comentario |
|---|---|---|
| Abono promedio | **USD 650/mes** | Mezcla: 40 % Base (400), 40 % Crecimiento (700), 20 % Integral (1.100), que da 660 |
| Setup promedio por cliente nuevo | USD 700, por única vez | No entra en el ingreso recurrente |
| Costos fijos al inicio | USD 400/mes | Herramientas, IA, Workspace, contador, dominio y algo de publicidad propia |
| Capacidad por persona | 6 a 8 cuentas en gestión | Depende del catálogo y del plan. Hay que medirlo con horas reales |
| Operador junior, cuando haga falta | USD 900/mes | Freelance o monotributista. Gestiona 6 a 8 cuentas con supervisión. Estimado a validar |
| Tipo de cambio | $1.535 por USD | BNA vendedor, 23/09/2026 |

## Escenarios (ingreso recurrente por mes, antes de impuestos)

| | **5 clientes** | **10 clientes** | **15 clientes** |
|---|---|---|---|
| Ingreso recurrente | USD 3.250 | USD 6.500 | USD 9.750 |
| Costos fijos | USD 400 | USD 500 | USD 600 |
| Operador junior | — | — | USD 900 |
| **Resultado** | **USD 2.850** | **USD 6.000** | **USD 8.250** |
| Fondo de reserva (10 %) | USD 285 | USD 600 | USD 825 |
| **Para cada socio (50/50)** | **≈ USD 1.280** | **≈ USD 2.700** | **≈ USD 3.710** |
| En pesos, por socio | ≈ $1,97 millones | ≈ $4,14 millones | ≈ $5,70 millones |

**Lo que no está en la tabla (y suma):**

- Setups y diagnósticos de clientes nuevos. Con un cliente nuevo por mes son unos USD 700 extra.
- Proyectos de consultoría y mentorías.
- Comisiones de Tiendanube: unos USD 8 a 10 por tienda por mes.

**Impuestos:** como monotributistas, cada uno paga su cuota fija mensual. Como SAS, hay Ingresos Brutos (alrededor de 3 a 5 % según la jurisdicción) y Ganancias sobre la utilidad. Ver [figura legal](05-sociedad-y-operacion.md#figura-legal-e-impuestos) y confirmarlo con el contador.

## ¿Cuántos clientes necesitamos?

**Fórmula:** clientes = (ingreso objetivo por socio × 2 + costos fijos) ÷ abono promedio

| Si cada socio quiere sacar… | Cuenta | Clientes necesarios |
|---|---|---|
| USD 1.000/mes (≈ $1,5 millones) | (2.000 + 400) ÷ 650 = 3,7 | **4** |
| USD 1.500/mes (≈ $2,3 millones) | (3.000 + 400) ÷ 650 = 5,2 | **6** |
| USD 2.500/mes (≈ $3,8 millones) | (5.000 + 500) ÷ 650 = 8,5 | **9** |

No incluye el fondo de reserva ni los impuestos.

**Primer límite de capacidad:** si Joaquín se dedica sobre todo a vender y administrar, casi toda la operación queda del lado de Franco. Entre los dos llegan a unas **10 a 12 cuentas**. Ahí hace falta el primer operador junior, y conviene tener el proceso de trabajo escrito para poder delegarlo.

## Rentabilidad por cliente: la cuenta que hay que mirar

Registrar las **horas por cliente** todos los meses. Ejemplo: un cliente Base (USD 400) que consume 20 horas por mes deja USD 20 por hora. Hay que subirlo de plan o recortar el alcance. Objetivo: que ningún cliente deje menos de **USD 35 por hora**.

## Inversión inicial estimada

| Concepto | Estimado |
|---|---|
| Dominio `.com.ar` y mail con dominio | Bajo (NIC Argentina y Workspace) |
| Logo y marca básica | USD 0 a 300 (Canva o diseñador) |
| Registro de marca en INPI (clase 35) | A cotizar (tasas y gestor) |
| Landing | USD 0 si la publicamos desde este repositorio con GitHub Pages |
| Colchón de costos fijos para los primeros 3 meses | USD 1.200 |
| SAS, cuando corresponda | $335.000 a $1.500.000 |
| **Total para arrancar, sin SAS** | **≈ USD 1.500 a 2.000** |
