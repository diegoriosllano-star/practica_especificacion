# ENUNCIADO
# Un estacionamiento cobra $20 la primera hora y $15 por cada
# hora adicional o fracción.
# El cobro máximo es de $150.
# El sistema recibe el tiempo de estancia en minutos
# y muestra el importe a cobrar.


# PROBLEMA
# Calcular el importe a cobrar por el tiempo de estancia
# de un vehículo en el estacionamiento.


# ENTRADAS
# minutos : int, minutos, rango válido de 0 en adelante.


# SALIDAS
# cobro : float, pesos mexicanos.


# REGLAS Y SUPUESTOS
# - El tiempo de estancia se maneja únicamente con minutos enteros.
# - El tiempo mínimo válido es 0 minutos.
# - Si la estancia es de 0 minutos, el cobro es $0.
# - Desde 1 hasta 60 minutos se cobran $20.
# - Después de los primeros 60 minutos, cada hora adicional cuesta $15.
# - Cualquier fracción de una hora adicional se cobra como una hora completa.
# - El cobro máximo permitido es de $150.
# - Se permite utilizar módulos de la biblioteca estándar de Python,
#   siempre que su uso respete la especificación y pueda explicarse.


# ALGORITMO
# 1. Leer el tiempo de estancia en minutos.
# 2. Si minutos == 0:
#       cobro = 0
# 3. En caso contrario, si minutos <= 60:
#       cobro = 20
# 4. En caso contrario:
#       calcular los minutos adicionales después de los primeros 60 minutos.
#       convertir los minutos adicionales a horas, redondeando siempre
#       hacia arriba cualquier fracción.
#       cobro = 20 + (horas_adicionales * 15)
# 5. Si cobro > 150:
#       cobro = 150
# 6. Mostrar el importe a cobrar.


# CASOS DE PRUEBA
# 45 minutos  -> $20
# 60 minutos  -> $20
# 61 minutos  -> $35
# 150 minutos -> $50
# 600 minutos -> $150


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases ni funciones auxiliares.
# - Se permite utilizar módulos de la biblioteca estándar de Python.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerMinutos() -> int :
#   Solicita el tiempo de estancia en minutos y lo devuelve como entero.
#
# calcularCobro(minutos) -> float :
#   Calcula el importe del estacionamiento considerando las horas
#   adicionales o fracciones y el cobro máximo.
#
# mostrarCobro(cobro) -> None :
#   Muestra el importe a cobrar.


# Implementa el algoritmo anterior utilizando las funciones del contrato.