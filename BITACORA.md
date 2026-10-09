# Bitácora de pruebas y rechazos

## Ejercicio 1. Recibo de luz

### Casos de prueba

| Caso | Entrada | Esperado (a mano) | Obtenido | Coincide |
|---|---|---|---|---|
| 1 | 100 kWh | $100.00 | $100.00 | Sí |
| 2 | 150 kWh | $150.00 | $150.00 | Sí |
| 3 | 200 kWh | $225.00 | $225.00 | Sí |
| 4 | 280 kWh | $345.00 | $345.00 | Sí |
| 5 | 300 kWh | $405.00 | $405.00 | Sí |

### Rechazos

Sin rechazos.

Se verificó que leerConsumo solicita y devuelve el consumo,
calcularPago realiza únicamente el cálculo indicado
y mostrarRecibo muestra el consumo y el importe.


## Ejercicio 2. Calificación final

### Casos de prueba

| Caso | Entrada | Esperado (a mano) | Obtenido | Coincide |
|---|---|---|---|---|
| 1 | (80, 70, 90) | 81.00, Aprobado | 81.00, Aprobado | Sí |
| 2 | (70, 70, 70) | 70.00, Aprobado | 70.00, Aprobado | Sí |
| 3 | (100, 100, 40) | 76.00, Reprobado | 76.00, Reprobado | Sí |
| 4 | (69, 70, 70) | 69.70, Reprobado | 69.70, Reprobado | Sí |

### Rechazos

Sin rechazos.

Se verificó que leerParciales solicita y devuelve las tres calificaciones,
calcularFinal calcula únicamente la calificación final,
determinarEstado evalúa si el alumno aprueba o reprueba
y mostrarResultado muestra la calificación final y el estado.

## Ejercicio 3. Total de compra

### Casos de prueba

| Caso | Entrada | Esperado (a mano) | Obtenido | Coincide |
|---|---|---|---|---|
| 1 | $500 | Descuento $0.00, IVA $80.00, Total $580.00 | | |
| 2 | $900 | Descuento $0.00, IVA $144.00, Total $1044.00 | | |
| 3 | $1000 | Descuento $100.00, IVA $144.00, Total $1044.00 | | |
| 4 | $5000 | Descuento $1000.00, IVA $640.00, Total $4640.00 | | |