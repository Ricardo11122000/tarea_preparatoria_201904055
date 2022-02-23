#PROGRAMA PARA ORDENAR LOS NUMEROS EN UN RANGO
# BASE DE DATOS = MAYOR

import math
import numpy
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


    print("Aplicacion para ordenar un rango")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un rango ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion = input("Ingrese una opcion: ")

    if(opcion == "1"):

        numero_1 = int(input("Ingrese el primer numero: "))
        numero_2 = int(input("Ingrese el segundo numero: "))

        lista = []

        if(numero_1 > numero_2):
            for n in range(numero_2, numero_1, 1):
                lista.append(n)
        else:
            for n in range(numero_1, numero_2, 1):
                lista.append(n)
        lista.sort(reverse=True)

        print("Los numeros ordenados de mayor a menor en el rango dado es: ",lista)

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO mayor(numero1, numero2, ordenado) VALUES( %s,%s,%s);",(numero_1, numero_2, lista))
        conexion.commit()
        cursor.close()
        conexion.close()  

        file = open("rango ordenado2.txt", "w")
        file.write(str(numero_1) +os.linesep)
        file.write(str(numero_2) +os.linesep)
        file.write(str(lista) +os.linesep)

    if(opcion == "2"):

        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM mayor;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)

    if(opcion == "3"):
        exit()





