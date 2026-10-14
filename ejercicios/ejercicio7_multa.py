# ENUNCIADO
# En una avenida el límite es de 60 km/h.
# Si se excede hasta por 20 km/h, la multa es de $500.
# Si se excede por más de 20 km/h, la multa es de $1,000.
# Se necesita mostrar la multa a partir de la velocidad del vehículo.


# PROBLEMA
# Calcular la multa de un vehículo según la velocidad
# a la que circula.


# ENTRADAS
# velocidad : int, kilómetros por hora (km/h),
# rango válido de 0 en adelante.


# SALIDAS
# multa : float, pesos mexicanos, mostrada con dos decimales.


# REGLAS Y SUPUESTOS
# - La velocidad se maneja únicamente con números enteros.
# - La velocidad mínima válida es 0 km/h.
# - El límite de velocidad es de 60 km/h.
# - Si la velocidad es menor o igual a 60 km/h, no hay multa.
# - Si la velocidad está entre 61 y 80 km/h, la multa es de $500.
# - Si la velocidad es mayor a 80 km/h, la multa es de $1,000.
# - La multa se muestra con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce una velocidad válida.


# ALGORITMO
# 1. Leer la velocidad del vehículo.
# 2. Si velocidad <= 60:
#       multa = 0
# 3. En caso contrario, si velocidad <= 80:
#       multa = 500
# 4. En caso contrario:
#       multa = 1000
# 5. Mostrar la velocidad y la multa correspondiente.


# CASOS DE PRUEBA
# 50 km/h -> $0.00
# 60 km/h -> $0.00
# 61 km/h -> $500.00
# 80 km/h -> $500.00
# 81 km/h -> $1000.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerVelocidad() -> int :
#   Solicita la velocidad del vehículo y la devuelve como entero.
#
# calcularMulta(velocidad) -> float :
#   Calcula y devuelve la multa correspondiente según la velocidad.
#
# mostrarMulta(velocidad, multa) -> None :
#   Muestra la velocidad y la multa correspondiente.


# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerVelocidad():
    velocidad = int(input("Ingrese la velocidad del vehículo en km/h: "))
    return velocidad


def calcularMulta(velocidad):
    if velocidad <= 60:
        multa = 0
    elif velocidad <= 80:
        multa = 500
    else:
        multa = 1000

    return multa


def mostrarMulta(velocidad, multa):
    print("Velocidad:", velocidad, "km/h")
    print(f"Multa: ${multa:.2f}")