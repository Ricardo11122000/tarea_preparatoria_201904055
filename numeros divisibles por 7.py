#FACTORIAL DE NUMEROS DIVISIBLES POR 7

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


    print("Aplicacion para mostrar el factorial de numeros divisibles por 7")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    factorial = 1
    if(opcion_escogida == "1"):
        try:
                 Numero = int(input("Ingrese el numero deseado: "))    
                 residuo = Numero%7
                 if(residuo != 0):
                     error = float("a")
        except ValueError:
            print ("El numero no es divisible por 7")
        else:
            for i in range(0,Numero,1):
                factorial = factorial*i + factorial
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO factorial(numero, factorial) VALUES( %s,%s);",(Numero,factorial))
        conexion.commit()
        cursor.close()
        conexion.close() 
        file = open("divisibles por 7.txt", "w")
        file.write(str(Numero) +os.linesep)
        file.write(str(factorial) +os.linesep)
                     
    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM factorial;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 

         