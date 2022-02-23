#MOSTRAR LA CANTIDAD DE NUMEROS IMPARES DE 0 HASTA DGITO INTRODUCIDO Y MOSTRAR HISTORIAL

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


    print("Aplicacion para mostrar la cantidad de numeros impares desde 0 hasta el digito introducido")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    contador = 0
    historial_cantidad = ["Registro"] 
    if(opcion_escogida == "1"):
        Numero = int(input("Ingrese el numero deseado: "))
        for n in range(0, Numero, 1):
            residuo = n%2
            if(residuo!= 0):
                contador = contador + 1
        resultado = contador
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO numerosimpares(numero, cantidad) VALUES( %s,%s);",(Numero,resultado))
        conexion.commit()
        cursor.close()
        conexion.close() 

        file = open("Cantidad de numeros impares.txt", "w")
        file.write(str(Numero) +os.linesep) 
        file.write(str(resultado) +os.linesep)

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM numerosimpares;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 

    

               