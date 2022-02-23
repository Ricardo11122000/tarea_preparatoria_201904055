#Pedir un numero y mostrar sus divisores


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

    print("Aplicacion para determinar los divisores exactos de un numero")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    num = []
    


    if(opcion_escogida == "1"):

        Numero = float(input("Ingrese el numero: "))

        for n in range(1, 100, 1):
            residuo = Numero%n
            if(residuo == 0):
                print("El numero "+str(n)+" es divisor de",Numero)
                num.append(n)
       
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO div(numero, divisores) VALUES( %s,%s);",(Numero,num))
        conexion.commit()
        cursor.close()
        conexion.close()  

        file = open("num.txt", "w")
        file.write(str(Numero) +os.linesep)
        file.write(str(num) +os.linesep)

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM div;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 

