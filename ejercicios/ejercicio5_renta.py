# ENUNCIADO
# Un parque renta bicicletas a $30 por hora.
# Si se rentan 3 horas o más, se aplica un 15% de descuento.
# Se necesita mostrar el importe a pagar según las horas de renta.


# PROBLEMA
# Calcular el importe a pagar por la renta de una bicicleta
# según el número de horas rentadas.


# ENTRADAS
# horas : int, horas de renta, rango válido de 1 en adelante.


# SALIDAS
# importe : float, pesos mexicanos, mostrado con dos decimales.


# REGLAS Y SUPUESTOS
# - Las horas de renta se manejan únicamente con números enteros.
# - La renta mínima es de 1 hora.
# - Cada hora cuesta $30.
# - Si se rentan menos de 3 horas, no se aplica descuento.
# - Si se rentan 3 horas o más, se aplica 15% de descuento
#   sobre el importe total de la renta.
# - El importe final se muestra con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce un número válido de horas.


# ALGORITMO
# 1. Leer el número de horas de renta.
# 2. Calcular el importe inicial:
#       importe = horas * 30
# 3. Si horas >= 3:
#       descuento = importe * 0.15
#       importe = importe - descuento
# 4. Mostrar las horas de renta y el importe a pagar.


# CASOS DE PRUEBA
# 1 hora  -> $30.00
# 2 horas -> $60.00
# 3 horas -> $76.50
# 4 horas -> $102.00


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerHoras() -> int :
#   Solicita las horas de renta y las devuelve como entero.
#
# calcularRenta(horas) -> float :
#   Calcula y devuelve el importe a pagar aplicando el descuento si corresponde.
#
# mostrarRenta(horas, importe) -> None :
#   Muestra las horas rentadas y el importe a pagar.


# Implementa el algoritmo anterior utilizando las funciones del contrato.

def leerHoras():
    horas = int(input("Ingrese las horas de renta: "))
    return horas


def calcularRenta(horas):
    importe = horas * 30

    if horas >= 3:
        descuento = importe * 0.15
        importe = importe - descuento

    return importe


def mostrarRenta(horas, importe):
    print("Horas de renta:", horas)
    print(f"Importe a pagar: ${importe:.2f}")