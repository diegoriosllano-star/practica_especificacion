# ENUNCIADO
# La calificación final de una materia se obtiene de tres parciales
# que valen 30%, 30% y 40%.
# La materia se aprueba con 70.
# Un parcial menor a 50 reprueba la materia.
# Se necesita mostrar la calificación final y si el alumno aprobó.


# PROBLEMA
# Calcular la calificación final de un alumno y determinar
# si aprueba o reprueba la materia.


# ENTRADAS
# parcial1 : int, calificación, rango válido de 0 a 100.
# parcial2 : int, calificación, rango válido de 0 a 100.
# parcial3 : int, calificación, rango válido de 0 a 100.


# SALIDAS
# calificacionFinal : float, calificación mostrada con dos decimales.
# estado : str, "Aprobado" o "Reprobado".


# REGLAS Y SUPUESTOS
# - Las calificaciones se manejan con números enteros de 0 a 100.
# - El primer parcial vale 30%.
# - El segundo parcial vale 30%.
# - El tercer parcial vale 40%.
# - La materia se aprueba con una calificación final de 70 o más.
# - Si cualquiera de los tres parciales es menor a 50, el alumno reprueba.
# - La calificación final se muestra con dos decimales.
# - No se aplica una regla adicional de redondeo.
# - Se supone que el usuario introduce calificaciones válidas.


# ALGORITMO
# 1. Leer las calificaciones de los tres parciales.
# 2. Calcular la calificación final:
#       calificacionFinal = (parcial1 * 0.30) + (parcial2 * 0.30) + (parcial3 * 0.40)
# 3. Si parcial1 < 50 o parcial2 < 50 o parcial3 < 50:
#       estado = "Reprobado"
# 4. En caso contrario, si calificacionFinal >= 70:
#       estado = "Aprobado"
# 5. En caso contrario:
#       estado = "Reprobado"
# 6. Mostrar la calificación final y el estado.


# CASOS DE PRUEBA
# (80, 70, 90)   -> 81.00, Aprobado
# (70, 70, 70)   -> 70.00, Aprobado
# (100, 100, 40) -> 76.00, Reprobado
# (69, 70, 70)   -> 69.70, Reprobado


# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.


# CONTRATO DE FUNCIONES
# leerParciales() -> int, int, int :
#   Solicita las tres calificaciones y las devuelve como enteros.
#
# calcularFinal(parcial1, parcial2, parcial3) -> float :
#   Calcula y devuelve la calificación final usando los porcentajes indicados.
#
# determinarEstado(parcial1, parcial2, parcial3, calificacionFinal) -> str :
#   Determina si el alumno está aprobado o reprobado.
#
# mostrarResultado(calificacionFinal, estado) -> None :
#   Muestra la calificación final y el estado del alumno.


# Implementa el algoritmo anterior utilizando las funciones del contrato.