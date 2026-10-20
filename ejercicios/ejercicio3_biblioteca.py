'''
Ejercicio 3. Multa de biblioteca

Una biblioteca cobra $5 por cada día de retraso en la devolución de un libro. A partir del día 11 de retraso, cada día cuesta $10. La multa máxima es de $200. Se necesita mostrar la multa a partir de los días de retraso.

'''

# PROBLEMA
# Calcular la multa por retraso en la devolución de un libro, considerando las tarifas por día y la multa máxima.

# ENTRADAS
# dias : entero, días de retraso, mayor o igual a 0.

# SALIDAS
# multa : real, pesos mexicanos, formato de moneda con 2 decimales.

# REGLAS Y SUPUESTOS
# - Los primeros 10 días de retraso cuestan $5 por día.
# - A partir del día 11, cada día adicional cuesta $10.
# - La multa máxima es de $200.
# - Si no hay días de retraso, la multa es de $0.
# - La multa calculada no puede superar los $200.
# - El resultado se muestra con 2 decimales.

# ALGORITMO
# 1. Leer los días de retraso.
# 2. Si dias <= 10:
#       multa = dias * 5
# 3. En caso contrario:
#       multa = 10 * 5 + (dias - 10) * 10
# 4. Si multa > 200:
#       multa = 200
# 5. Mostrar la multa.

# CASOS DE PRUEBA
# 0 días -> $0.00
# 10 días -> $50.00
# 11 días -> $60.00
# 25 días -> $200.00
# 40 días -> $200.00

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerDias() -> dias : leer y devolver los días de retraso.
# calcularMulta(dias) -> multa : calcular la multa aplicando las tarifas y el límite máximo.
# mostrarMulta(multa) -> None : mostrar la multa con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones del contrato.

from tabulate import tabulate

def leerDias():
    return int(input("Ingrese los días de retraso: "))

def calcularMulta(dias):
    if dias <= 10:
        multa = dias * 5
    else:
        multa = 10 * 5 + (dias - 10) * 10
    if multa > 200:
        multa = 200
    return multa

def mostrarMulta(dias, multa):
    filas = [
        ["Días de retraso", f"{dias}"],
        ["Multa", f"${multa:.2f}"]
    ]

    print(tabulate(filas, headers=["Concepto", "Importe"], tablefmt="grid"))
