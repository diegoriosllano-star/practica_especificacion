# ENUNCIADO
# Una tienda aplica 10% de descuento en compras de $1,000 o más
# y 20% en compras de $5,000 o más.
# A la compra se le agrega el 16% de IVA.
# Se necesita mostrar el ticket con subtotal, descuento, IVA y total.


# PROBLEMA
# Calcular el descuento, IVA y total de una compra
# a partir del subtotal ingresado.


# ENTRADAS
# subtotal : float, pesos mexicanos, rango válido de 0 en adelante.


# SALIDAS
# subtotal : float, pesos mexicanos, mostrado con dos decimales.
# descuento : float, pesos mexicanos, mostrado con dos decimales.
# iva : float, pesos mexicanos, mostrado con dos decimales.
# total : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - El subtotal puede contener decimales.
# - El subtotal mínimo válido es $0.
# - Si el subtotal es menor a $1,000, no se aplica descuento.
# - Si el subtotal es de $1,000 o más y menor a $5,000, se aplica 10% de descuento.
# - Si el subtotal es de $5,000 o más, se aplica únicamente 20% de descuento.
# - Los descuentos no se acumulan.
# - El IVA es de 16%.
# - El IVA se calcula después de restar el descuento al subtotal.
# - Los importes se muestran con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce un subtotal válido.


# ALGORITMO
# 1. Leer el subtotal de la compra.
# 2. Si subtotal >= 5000:
#       descuento = subtotal * 0.20
# 3. En caso contrario, si subtotal >= 1000:
#       descuento = subtotal * 0.10
# 4. En caso contrario:
#       descuento = 0
# 5. Calcular el IVA:
#       iva = (subtotal - descuento) * 0.16
# 6. Calcular el total:
#       total = subtotal - descuento + iva
# 7. Mostrar subtotal, descuento, IVA y total.


# CASOS DE PRUEBA
# $500    -> descuento $0.00, IVA $80.00, total $580.00
# $900    -> descuento $0.00, IVA $144.00, total $1044.00
# $1000   -> descuento $100.00, IVA $144.00, total $1044.00
# $5000   -> descuento $1000.00, IVA $640.00, total $4640.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerSubtotal() -> float :
#   Solicita el subtotal de la compra y lo devuelve como número decimal.
#
# calcularDescuento(subtotal) -> float :
#   Calcula y devuelve el descuento correspondiente al subtotal.
#
# calcularIVA(subtotal, descuento) -> float :
#   Calcula el IVA sobre el subtotal después de restar el descuento.
#
# calcularTotal(subtotal, descuento, iva) -> float :
#   Calcula y devuelve el total final de la compra.
#
# mostrarTicket(subtotal, descuento, iva, total) -> None :
#   Muestra el subtotal, descuento, IVA y total de la compra.


# Implementa el algoritmo anterior utilizando las funciones del contrato.