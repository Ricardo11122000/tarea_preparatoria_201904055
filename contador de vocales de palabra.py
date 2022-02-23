#PROGRAMA PARA CONTAR EL NUMERO DE CADA VOCAL PRESENTE EN UNA PALABRA
# BASE DE DATOS = VOCALES



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


    print("Aplicacion para contar vocales en una palabra")
    print(" ")
    print("menu principal: ")
    print(" ")
    print("1. Ingresar una palabra ")
    print("2. Mostrar el historial ")
    print("3. Finalizar la aplicacion ")
    opcion = input("Ingrese una opcion: ")

    if (opcion == "1"):
            palabra = input("Ingrese una palabra para contar el numero de cada vocal presente: ")

            contador_As = 0
            contador_Es = 0
            contador_Is = 0
            contador_Os = 0
            contador_Us = 0


            for letra in palabra:
                if(letra == "a" or letra == "A"):
                    contador_As = contador_As + 1
                elif(letra == "e" or letra == "E"):
                    contador_Es = contador_Es + 1
                elif(letra == "i" or letra == "I"):
                    contador_Is = contador_Is + 1
                elif(letra == "o" or letra == "O"):
                    contador_Os = contador_Os + 1
                elif(letra == "u" or letra == "U"): 
                    contador_Us = contador_Us + 1

            print("El numero de la vocal a en la palabra es: ", contador_As)
            print("El numero de la vocal e en la palabra es: ", contador_Es)
            print("El numero de la vocal i en la palabra es: ", contador_Is)
            print("El numero de la vocal o en la palabra es: ", contador_Os)
            print("El numero de la vocal u en la palabra es: ", contador_Us)

            cursor = conexion.cursor()
            cursor.execute("INSERT INTO vocales(palabra, a,e,i,o,u) VALUES( %s,%s,%s,%s,%s,%s);",(palabra,contador_As,contador_Es,contador_Is,contador_Os,contador_Us))
            conexion.commit()
            cursor.close()
            conexion.close()  

            file = open("vocales.txt", "w")
            file.write(str(contador_As) +os.linesep)
            file.write(str(contador_Es) +os.linesep)
            file.write(str(contador_Is) +os.linesep)
            file.write(str(contador_Os) +os.linesep)
            file.write(str(contador_Us) +os.linesep)
            file.write(palabra +os.linesep)

    elif(opcion == "2"):

        print("Historial")
        cursor = conexion.cursor()
        SQL = 'SELECT*FROM vocales;'
        cursor.execute(SQL)
        valores = cursor.fetchall()
        print(valores)

    elif(opcion == "3"):

        exit()

