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