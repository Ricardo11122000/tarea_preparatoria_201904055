#Aplicacion para mostrar el tipo de triangulo segun la longitud de sus lados

import math
from numpy import empty
import psycopg2
import os



while True: 
    try:
        conexion = psycopg2.connect(
        host = "localhost",
        port =  "5432",
        user = "postgres", 
        password = "11122000", 
        dbname = "postgres"
    ) 
        print("Conexion exitosa")
    except psycopg2.Error as e:
        print("Conexion fallida") 


    print("Aplicacion para mostrar el tipo de triangulo segun la longitud de sus lados")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar lados de triangulo ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    if(opcion_escogida == "1"):
        for i in range(0,3,1):
            if(i==0):
                lado1 = int(input("Ingrese el lado numero "+str(i+1)+": "))
            elif(i==1):
                lado2 = int(input("Ingrese el lado numero "+str(i+1)+": "))
            elif(i==2):
                lado3 = int(input("Ingrese el lado numero "+str(i+1)+": "))
        if(lado1 == lado2 and lado1 == lado3):
            tipo = "triangulo equilatero"
        elif(lado1 == lado2 or lado1 == lado3 or lado3 == lado2):
            tipo = "triangulo isosceles"
        elif(lado1 != lado2 and lado1 != lado3 and lado2 != lado3):
            tipo = "triangulo escaleno"
        
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO triangulos(lado1, lado2, lado3, tipo) VALUES( %s,%s,%s,%s);",(lado1,lado2,lado3,tipo))
        conexion.commit()
        cursor.close()
        conexion.close()   

        file = open("triangulos.txt", "w")
        file.write(str(lado1) +os.linesep)
        file.write(str(lado2) +os.linesep)
        file.write(str(lado3) +os.linesep)
        file.write(str(tipo) +os.linesep)

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM triangulos;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 