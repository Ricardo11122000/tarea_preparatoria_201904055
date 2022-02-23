# APLICACION PARA MOSTRAR LOS NUMEROS PARES EN UN RANGO
# BASE DE DATOS: 

import math
import numpy
import os
import psycopg2

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


    print("Aplicacion para contar mostrar numeros pares en un rango")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un rango ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion = input("Ingrese una opcion: ")

    if(opcion == "1"):


          limite_superior = int(input("Ingrese el limite superior del rango de numeros: "))
          limite_inferior = int(input("Ingrese el limite inferior del rango de numeros: "))
          numeros_pares = []


          for n in range(limite_inferior,limite_superior+1,2):
               numeros_pares.append(n)
          print("Los numeros de dos en dos entre el rango"+str(limite_superior)+" y "+str(limite_inferior)+" es :",numeros_pares)

          cursor = conexion.cursor()
          cursor.execute("INSERT INTO pares(superior, inferior,pares) VALUES( %s,%s,%s);",(limite_superior,limite_inferior,numeros_pares))
          conexion.commit()
          cursor.close()
          conexion.close()  

          file = open("numeros pares.txt", "w")
          file.write(str(limite_inferior) +os.linesep)
          file.write(str(limite_superior) +os.linesep)
          file.write(str(numeros_pares) +os.linesep)

    elif(opcion == "2"):
          print("Historial")
          cursor = conexion.cursor()
          SQL = 'SELECT*FROM pares;'
          cursor.execute(SQL)
          valores = cursor.fetchall()
          print(valores)

    elif(opcion == "3"):
          exit()