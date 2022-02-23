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

    print("Aplicacion para calcular areas geometricas")
    print(" ")

    print("MENU PRINCIPAL: ")

    print("1. Ir a la calculadora")
    print("2. Ver historial")
    print("3. Salir de la aplicacion")
    opcion_escogida = input("Escoga una opcion: ")
    if(opcion_escogida == "1"):
        print("1. Calcular area de un triangulo")
        print("2. Calcular area de un circulo")
        print("3. Calcular area de un cuadrado")
        print("4. Calcular area de un rectangulo")
        opcion_escogida2 = input("Escoga una opcion: ")

        if(opcion_escogida2 == "1"):
            base = float(input("Ingrese la longitud de la base: "))
            altura = float(input("Ingrese la longitud de la altura: "))
            area = (base*altura)/2
            figura = "triangulo"

        elif(opcion_escogida2 == "2"):
            radio = float(input("Ingrese el radio del circulo: "))
            area = 3.1416*radio**2
            figura = "circulo"
        elif(opcion_escogida2 == "3"):
            lado = float(input("Ingrese la longitud de los lados del cuadrado: "))
            area = lado**2
            figura = "cuadrado"
        elif(opcion_escogida2 == "4"):
            baser = float(input("Ingrese la longitud de la base del rectangulo: "))
            alturar = float(input("Ingrese la longitud de la altura del rectangulo: "))
            area = baser*alturar
            figura = "rectangulo"

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO areas(figura, area) VALUES( %s,%s);",(figura, area))
        conexion.commit()
        cursor.close()
        conexion.close() 

        file = open("areas.txt", "w")
        file.write(figura +os.linesep) 
        file.write(str(area) +os.linesep) 

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM areas;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 

