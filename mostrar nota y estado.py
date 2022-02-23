#MOSTRAR nota y esatdo

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


    print("Aplicacion para mostrar la mostrar el promedio de tres notas")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar notas ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    contador = 0
    historial_cantidad = ["Registro"] 
    if(opcion_escogida == "1"):
        Nota1 = int(input("Ingrese la primera nota: "))
        Nota2 = int(input("Ingrese la segunda nota: "))
        Nota3 = int(input("Ingrese la tercera nota: "))

        promedio = (Nota1 + Nota2 + Nota3)/3
        if(promedio >= 60):
            final = "aprobado"
            print("Usted esta aprobado y su promedio final es: ",promedio)
        else:
            final = "reprobado"
            print("Ustde esta reprobado y su promedio final es: ", promedio)


        cursor = conexion.cursor()
        cursor.execute("INSERT INTO notas(nota, estado) VALUES( %s,%s);",(promedio,final))
        conexion.commit()
        cursor.close()
        conexion.close() 

        file = open("Notas.txt", "w")
        file.write(str(promedio) +os.linesep) 
        file.write(final +os.linesep)

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM notas;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 