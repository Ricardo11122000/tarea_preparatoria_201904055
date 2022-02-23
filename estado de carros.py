# APLICACION PARA MOSTRAR EL ESTADO ACTUAL DE UN AUTO


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


    print("Aplicacion para mostrar el estado actual de un auto")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    if(opcion_escogida == "1"):
        modelo = int(input("Ingrese el modelo del automovil: "))
        km_recorridos = int(input("Ingrese el numero de kilometros recorridos por el auto: "))

        if(modelo <= 2007 and km_recorridos >= 20000):
            estado = "debe renovarse"
            print(estado)
        elif(modelo >2007 and modelo < 2013 and km_recorridos >= 20000):
            estado = "debe recibir mantenimiento"
            print(estado)
        elif(modelo > 2013 and km_recorridos < 10000):
            estado = "esta en optimas condiciones"
            print(estado)
        else:
            print("mecanico")
       
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO modelocarros(modelo, kilometraje, estado) VALUES( %s,%s,%s);",(modelo,km_recorridos,estado))
        conexion.commit()
        cursor.close()
        conexion.close() 

        file = open("Estado de carros.txt", "w")
        file.write(str(modelo) +os.linesep) 
        file.write(str(km_recorridos) +os.linesep)
        file.write(estado +os.linesep) 

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM modelocarros;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 



