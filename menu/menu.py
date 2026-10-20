from ejercicios import ejercicio1_taxi as ej1
from ejercicios import ejercicio2_comision as ej2
from ejercicios import ejercicio3_biblioteca as ej3

def mostrar_menu():
    print("Seleccione un ejercicio:")
    print("1. Ejercicio 1: Viaje en taxi")
    print("2. Ejercicio 2: Comisión de ventas")
    print("3. Ejercicio 3: Biblioteca")
    print("4. Salir")

def menu():
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número del ejercicio a ejecutar (1-4): ")
        if opcion == "1":
            ejecutar_ejercicio1()
        elif opcion == "2":
            ejecutar_ejercicio2()
        elif opcion == "3":
            ejecutar_ejercicio3()
        elif opcion == "4":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")

def ejecutar_ejercicio1():
    kilometros = ej1.leerKilometros()
    importe = ej1.calcularImporte(kilometros)
    ej1.mostrarImporte(importe)

def ejecutar_ejercicio2():
    ventas = ej2.leerVentas()
    comision = ej2.calcularComision(ventas)
    bono = ej2.calcularBono(ventas)
    total = comision + bono
    ej2.mostrarPago(comision, bono, total)

def ejecutar_ejercicio3():
    dias = ej3.leerDias()
    multa = ej3.calcularMulta(dias)
    ej3.mostrarMulta(dias, multa)