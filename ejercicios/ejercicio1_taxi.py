'''

Ejercicio 1. Viaje en taxi

Un taxi cobra $35 de banderazo y $9 por kilómetro recorrido. Los viajes de más de 20 km tienen 10% de descuento. Se necesita mostrar el importe del viaje.

'''

# PROBLEMA
# Calcular el importe de un viaje en taxi considerando el banderazo, los kilómetros recorridos y el descuento correspondiente.

# ENTRADAS
# kilometros : real, kilómetros, mayor o igual a 0.

# SALIDAS
# importe : real, pesos mexicanos, formato de moneda con 2 decimales.

# REGLAS Y SUPUESTOS
# - El banderazo tiene un costo fijo de $35.
# - Cada kilómetro recorrido cuesta $9.
# - Si el viaje es de más de 20 km, se aplica un descuento del 10%.
# - Si el viaje es de 20 km o menos, no se aplica descuento.
# - El descuento se aplica al importe total, incluyendo el banderazo.
# - El resultado se muestra con 2 decimales.

# ALGORITMO
# 1. Leer los kilómetros recorridos.
# 2. Calcular el importe inicial: 35 + kilometros * 9.
# 3. Si kilometros > 20:
#       importe = importe inicial * 0.90
# 4. En caso contrario:
#       importe = importe inicial
# 5. Mostrar el importe del viaje.

# CASOS DE PRUEBA
# 5 km -> $80.00
# 20 km -> $215.00
# 21 km -> $201.60
# 30 km -> $274.50

# RESTRICCIONES PARA EL AGENTE
# - Implementa exactamente este algoritmo, en el mismo orden.
# - Usa únicamente las funciones del contrato, con esas firmas.
# - No agregues clases, funciones auxiliares ni bibliotecas.
# - No agregues validaciones, mensajes ni cálculos que no estén aquí.
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerKilometros() -> kilometros : leer y devolver los kilómetros recorridos.
# calcularImporte(kilometros) -> importe : calcular el importe total del viaje.
# mostrarImporte(importe) -> None : mostrar el importe con 2 decimales.

# Implementa el algoritmo anterior utilizando las funciones del contrato.
from tabulate import tabulate

def leerKilometros():
    return float(input("Ingrese los kilómetros recorridos: "))

def calcularImporte(kilometros):
    importe = 35 + kilometros * 9
    if kilometros > 20:
        importe *= 0.90
    return importe

def mostrarImporte(importe):
   filas = [
       ["Banderazo", "$35.00"],
       ["Costo por km", "$9.00"],
       ["Total", f"${importe:.2f}"]
   ]

   print(tabulate(filas, headers=["Concepto", "Importe"], tablefmt="grid"))
