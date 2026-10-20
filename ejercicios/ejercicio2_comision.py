'''
Ejercicio 2. Comisión de ventas

Un vendedor gana 5% de comisión sobre sus ventas del mes. Si vende $10,000 o más, la comisión es de 8%. Si vende más de $50,000, recibe además un bono de $1,000. Se necesita mostrar la comisión, el bono y el total a pagar.

'''

# PROBLEMA
# Calcular la comisión, el bono y el total a pagar a un vendedor según sus ventas mensuales.

# ENTRADAS
# ventas : real, pesos mexicanos, mayor o igual a 0.

# SALIDAS
# comision : real, pesos mexicanos, formato de moneda con 2 decimales.
# bono : real, pesos mexicanos, formato de moneda con 2 decimales.
# total : real, pesos mexicanos, formato de moneda con 2 decimales.

# REGLAS Y SUPUESTOS
# - Las ventas menores a $10,000 generan una comisión del 5%.
# - Las ventas de $10,000 o más generan una comisión del 8%.
# - Las ventas mayores a $50,000 reciben un bono adicional de $1,000.
# - Las ventas de $50,000 o menos no reciben bono.
# - El total a pagar es la comisión más el bono.
# - La comisión se calcula sobre el total de ventas.
# - Los resultados se muestran con 2 decimales.

# ALGORITMO
# 1. Leer las ventas del mes.
# 2. Si ventas >= 10000:
#       comision = ventas * 0.08
# 3. En caso contrario:
#       comision = ventas * 0.05
# 4. Si ventas > 50000:
#       bono = 1000
# 5. En caso contrario:
#       bono = 0
# 6. Calcular total = comision + bono.
# 7. Mostrar la comisión, el bono y el total a pagar.

# CASOS DE PRUEBA
# $5,000 -> Comisión: $250.00, Bono: $0.00, Total: $250.00
# $10,000 -> Comisión: $800.00, Bono: $0.00, Total: $800.00
# $50,000 -> Comisión: $4,000.00, Bono: $0.00, Total: $4,000.00
# $50,001 -> Comisión: $4,000.08, Bono: $1,000.00, Total: $5,000.08

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerVentas() -> ventas : leer y devolver las ventas del mes.
# calcularComision(ventas) -> comision : calcular la comisión según las ventas.
# calcularBono(ventas) -> bono : calcular el bono correspondiente.
# mostrarPago(comision, bono, total) -> None : mostrar la comisión, el bono y el total a pagar.

# Implementa el algoritmo anterior utilizando las funciones del contrato.
from tabulate import tabulate

def leerVentas():
    return float(input("Ingrese las ventas del mes: "))

def calcularComision(ventas):
    if ventas >= 10000:
        comision = ventas * 0.08
    else:
        comision = ventas * 0.05
    return comision

def calcularBono(ventas):
    if ventas > 50000:
        bono = 1000
    else:
        bono = 0
    return bono

def mostrarPago(comision, bono, total):
    filas = [
        ["Comisión", f"${comision:.2f}"],
        ["Bono", f"${bono:.2f}"],
        ["Total a pagar", f"${total:.2f}"]
    ]

    print(tabulate(filas, headers=["Concepto", "Importe"], tablefmt="grid"))