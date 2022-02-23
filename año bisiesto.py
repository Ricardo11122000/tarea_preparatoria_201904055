#MOSTRAR SI UN ANO ES BISIESTO O NO

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


    print("Aplicacion para mostrar si un año es bisiesto o no")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar un numero ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion_escogida = input("Ingrese una opcion: ")
    if(opcion_escogida == "1"):

        año = int(input("Ingrese el año: "))

        if not año % 4:
            if not año % 100:     
                if not año % 400:  
                    print("Es bisiesto")
                    afirmacion = "si es bisiesto"
                else:              
                    print("No es bisiesto")
                    afirmacion = "no es bisiesto"
            else:                 
                print("Es bisiesto")
                afirmacion = "si es bisiesto"
        else:                    
            print("No es bisiesto")
            afirmacion = "no es bisiesto"

        cursor = conexion.cursor()
        cursor.execute("INSERT INTO anobisiesto(año, bisiesto) VALUES( %s,%s);",(año,afirmacion))
        conexion.commit()
        cursor.close()
        conexion.close() 

        file = open("anobisiesto.txt", "w")
        file.write(str(año) +os.linesep) 
        file.write(afirmacion +os.linesep) 

    elif(opcion_escogida == "2"):
        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM anobisiesto;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)
    else:
        exit() 
