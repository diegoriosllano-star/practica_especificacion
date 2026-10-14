# ENUNCIADO
# Un cine cobra $80 por boleto.
# Los niños de hasta 12 años y los adultos de 60 años o más
# pagan la mitad.
# Se necesita mostrar el precio del boleto según la edad.


# PROBLEMA
# Calcular el precio de un boleto de cine según la edad
# de la persona.


# ENTRADAS
# edad : int, años, rango válido de 0 en adelante.


# SALIDAS
# precio : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - La edad se maneja únicamente con números enteros.
# - La edad mínima válida es 0 años.
# - El precio normal del boleto es de $80.
# - Si la edad es menor o igual a 12 años, se paga la mitad.
# - Si la edad está entre 13 y 59 años, se paga el precio normal.
# - Si la edad es mayor o igual a 60 años, se paga la mitad.
# - El precio con descuento es de $40.
# - El precio se muestra con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce una edad válida.


# ALGORITMO
# 1. Leer la edad de la persona.
# 2. Si edad <= 12:
#       precio = 80 * 0.50
# 3. En caso contrario, si edad >= 60:
#       precio = 80 * 0.50
# 4. En caso contrario:
#       precio = 80
# 5. Mostrar la edad y el precio del boleto.


# CASOS DE PRUEBA
# 8 años  -> $40.00
# 12 años -> $40.00
# 13 años -> $80.00
# 59 años -> $80.00
# 60 años -> $40.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerEdad() -> int :
#   Solicita la edad y la devuelve como entero.
#
# calcularPrecio(edad) -> float :
#   Calcula y devuelve el precio del boleto según la edad.
#
# mostrarPrecio(edad, precio) -> None :
#   Muestra la edad y el precio del boleto.


# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerEdad():
    edad = int(input("Ingrese la edad: "))
    return edad


def calcularPrecio(edad):
    if edad <= 12:
        precio = 80 * 0.50
    elif edad >= 60:
        precio = 80 * 0.50
    else:
        precio = 80

    return precio


def mostrarPrecio(edad, precio):
    print("Edad:", edad, "años")
    print(f"Precio del boleto: ${precio:.2f}")