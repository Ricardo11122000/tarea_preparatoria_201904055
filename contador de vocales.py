#INGRESAR UNA PALABRA Y CONTAREL NUMERO DE VOCALES EN ELLA
# BASE DE DATOS = vocales2

import math
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


    print("Aplicacion para contar el numero de vocales en una palabra")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar una palabra ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion = input("Ingrese una opcion: ")

    if(opcion == "1"):

        palabra = input("Ingrese una palabra: ")
        Numero_de_vocales = 0
        for letra in palabra:
            if(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U" ):
                Numero_de_vocales = Numero_de_vocales + 1
            else:
                Numero_de_vocales = Numero_de_vocales
        print("El numero de vocales en "+palabra+" es: "+str(Numero_de_vocales))

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO vocales2(palabra, vocales) VALUES( %s,%s);",(palabra,Numero_de_vocales))
        conexion.commit()
        cursor.close()
        conexion.close()  

        file = open("vocales2.txt", "w")
        file.write(palabra +os.linesep)
        file.write(str(Numero_de_vocales) +os.linesep)

    elif(opcion == "2"):

        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM vocales2;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)

    elif(opcion == "3"):

        exit()