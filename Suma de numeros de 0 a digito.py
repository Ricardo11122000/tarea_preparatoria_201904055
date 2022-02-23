#PROGRAMA PARA MOSTRAR LA SUMA DE 0 HASTA EL DIGITO INGRESADO POR EL USUARIO
# BASE DE DATOS = SUMA

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


    print("Aplicacion para realizar la suma de 0 hasta el numero ingresado")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion = input("Ingrese una opcion: ")
    Suma = 0

    if (opcion == "1"):
        Numero = int(input("Ingrese un numero: "))

        for n in range(0, Numero+1, 1):
            Suma = Suma + n
        print("El valor de la suma de todos los digitos es: ",Suma)

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO suma(numero, suma) VALUES( %s,%s);",(Numero,Suma))
        conexion.commit()
        cursor.close()
        conexion.close()  

        file = open("suma.txt", "w")
        file.write(str(Numero) +os.linesep)

    elif(opcion == "2"):

        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM suma;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)

    elif(opcion == "3"):

        exit()
