# APLICACION PARA PEDIR 3 NUMEROS Y REALIZAR OPERACIONES DIFERENTES
# BASE DE DATOS = 3OPERACIONES

import math
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

    print("Aplicacion para realizar operaciones segun numeros ingresados")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Utilizar aplicacion ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion = input("Ingrese una opcion: ")


    if(opcion == "1"):

        numero_1 = input("Ingrese el primer numero: ")
        numero_2 = input("Ingrese el segundo numero: ")
        numero_3 = input("Ingrese el tercer numero: ")



        if(float(numero_1)>float(numero_2) and float(numero_1)>float(numero_3) and not(numero_1==numero_2 or numero_1==numero_3 or numero_2==numero_3)):
            Resultado =float(numero_1) + float(numero_2) + float(numero_3)
            print(Resultado)
        elif(float(numero_2)>float(numero_1) and float(numero_2)>float(numero_3) and not(numero_1==numero_2 or numero_1==numero_3 or numero_2==numero_3)):
            Resultado = float(numero_1)*float(numero_2)*float(numero_3)
            print(Resultado)
        elif(float(numero_3)>float(numero_1) and float(numero_3)>float(numero_2) and not(numero_1==numero_2 or numero_1==numero_3 or numero_2==numero_3)):
            Resultado = numero_1 + numero_2 + numero_3
            print(Resultado)
        elif(numero_1==numero_2 and numero_1==numero_3):
            print("Los numeros ingresados son iguales y son:",numero_1)
        elif(numero_1==numero_2):
            Resultado = numero_3
            print(Resultado)
        elif(numero_2==numero_3):
            Resultado = numero_1
            print(Resultado)
        elif(numero_1==numero_3):
            Resultado = numero_2
            print(Resultado)

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO operaciones(numero1, numero2, numero3, resultado) VALUES( %s,%s,%s,%s);",(numero_1,numero_2,numero_3,Resultado))
        conexion.commit()
        cursor.close()
        conexion.close()  

        file = open("operaciones.txt", "w")
        file.write(str(numero_1) +os.linesep)
        file.write(str(numero_2) +os.linesep)
        file.write(str(numero_3) +os.linesep)
        file.write(str(Resultado) +os.linesep)

    elif(opcion == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM operaciones;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    elif(opcion == "3"):
        exit() 
    
