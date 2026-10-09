# ENUNCIADO
# Una compa+¦+¡a el+®ctrica cobra el consumo mensual con tres tarifas:
# $1.00 por kWh hasta 150 kWh, $1.50 por kWh de 151 a 280 kWh
# y $3.00 por kWh arriba de 280 kWh.
# Se necesita calcular el importe del recibo a partir del consumo del mes.


# PROBLEMA
# Calcular el importe mensual del recibo de luz de un cliente
# a partir de su consumo de energ+¡a el+®ctrica.


# ENTRADAS
# consumo : int, kilowatt-hora (kWh), rango v+ílido de 0 en adelante.


# SALIDAS
# consumo : int, kilowatt-hora (kWh).
# pago : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - El consumo se maneja +¦nicamente con n+¦meros enteros.
# - El consumo m+¡nimo v+ílido es 0 kWh.
# - Los primeros 150 kWh se cobran a $1.00 por kWh.
# - Del kWh 151 al 280, solo el excedente de 150 kWh se cobra a $1.50 por kWh.
# - Arriba de 280 kWh, solo el excedente de 280 kWh se cobra a $3.00 por kWh.
# - Las tarifas se aplican por bloques acumulados.
# - El importe se muestra con dos decimales.
# - Se supone que el usuario introduce un consumo v+ílido.


# ALGORITMO
# 1. Leer el consumo mensual en kWh.
# 2. Si consumo <= 150:
#       pago = consumo * 1.00
# 3. En caso contrario, si consumo <= 280:
#       pago = (150 * 1.00) + ((consumo - 150) * 1.50)
# 4. En caso contrario:
#       pago = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)
# 5. Mostrar el consumo y el importe del recibo.


# CASOS DE PRUEBA
# 100 kWh -> $100.00
# 150 kWh -> $150.00
# 200 kWh -> $225.00
# 280 kWh -> $345.00
# 300 kWh -> $405.00


# RESTRICCIONES PARA LA IA
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa +¦nicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni c+ílculos que no est+®n aqu+¡.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerConsumo() -> int :
#   Solicita al usuario el consumo mensual en kWh y lo devuelve como entero.
#
# calcularPago(consumo) -> float :
#   Recibe el consumo mensual y calcula el importe aplicando las tarifas por bloques.
#
# mostrarRecibo(consumo, pago) -> None :
#   Recibe el consumo y el importe calculado y muestra el recibo al usuario.


# Implementa el algoritmo anterior utilizando las funciones del contrato.



def leerConsumo() -> int:
    return int(input("Ingrese el consumo mensual en kWh: "))


def calcularPago(consumo: int) -> float:
    if consumo <= 150:
        pago = consumo * 1.00
    elif consumo <= 280:
        pago = (150 * 1.00) + ((consumo - 150) * 1.50)
    else:
        pago = (150 * 1.00) + (130 * 1.50) + ((consumo - 280) * 3.00)
    return pago


def mostrarRecibo(consumo: int, pago: float) -> None:
    print(f"Consumo: {consumo} kWh")
    print(f"Importe del recibo: ${pago:.2f}")
