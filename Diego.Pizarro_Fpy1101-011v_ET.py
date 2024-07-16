from random import *
import csv
import os

s1 = 0
s2 = 0
s3 = 0
s4 = 0
s5 = 0
s6 = 0
s7 = 0
s8 = 0
s9 = 0
s10 = 0
trabajadores = []
menos = ["Nombre Empleado", "Sueldo"]
def asignar_sueldos_aleatorios(trabajadores):
    trabajador = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
    s1 = randint(300000, 2500000)
    s2 = randint(300000, 2500000)
    s3 = randint(300000, 2500000)
    s4 = randint(300000, 2500000)
    s5 = randint(300000, 2500000)
    s6 = randint(300000, 2500000)
    s7 = randint(300000, 2500000)
    s8 = randint(300000, 2500000)
    s9 = randint(300000, 2500000)
    s10 = randint(300000, 2500000)
    trabajadores.append(trabajador)
    sueldos = ["$",s1,"$",s2,"$",s3,"$",s4,"$",s5,"$",s6,"$",s7,"$",s8,"$",s9,"$",s10]
    trabajadores.append(sueldos)
   
    for trabajadores in trabajadores:
        print(trabajadores)
def clasificar_sueldos():
    print("")



def ver_estadisticas():
    print("")


def reporte_de_sueldos():
    print("")


def salir():
    print("Finalizando Programa...")
    print("Desarrollado por Diego Pizarro")
    print("RUT: 21751824-5")

    


while True:
    print("\n===BIENVENIDO===")
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos ")
    print("3. Ver estadisticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
    while True:
        try:
            opc = int(input("Ingrese la opcion(1-5):"))
            if opc < 1 or opc >5:
                print("Ingrese un numero entre 1 y 5 ")
                continue
            elif opc >0 and opc < 6 :
                print("")
                break
            else:
                print("")
        except ValueError:
            print("Ingrese un numero entre el 1 y el 5 ")
            continue
    if opc == 1:
        print("")
        asignar_sueldos_aleatorios(trabajadores)
    elif opc == 2:
        clasificar_sueldos(trabajadores)
    elif opc == 3:
        ver_estadisticas
    elif opc == 4:
        reporte_de_sueldos
    elif opc == 5:
        salir()
        break






    
 

