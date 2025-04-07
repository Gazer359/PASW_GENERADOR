from Pasw_Generador import pasw_generator, pasw_easy_read
import time
import os
from OS_manager import crear_Archivotxt, ya_existe, historial_contras


while True:
    print("""
──────██████.
──▄▀▀▀▄───────────────
──█───█───────────────
─███████─────────▄▀▀▄─
░██───██░░█▀█▀▀▀▀█░░█░
░███▄███░░▀░▀░░░░░▀▀░░
\n BIENVENIDO GENERADOR DE CONTRASEÑAS. \n""")
    time.sleep(2)
    print("""1.Generador de contraseñas aleatorias \n2.Generador de contraseñas faciles de leer \n3.Consular si ya existe una contraeña  \n4.Consultar el historial de contraseñas creadas \n5.Salir del Programa""")

    try:
        seleccion = int(input("Ingresar una de las opciones: "))
        os.system("cls")
    except ValueError as e:
        print(f"Error {e}")
        continue
    else:
        if seleccion == 1:
            os.system("cls")
            crear_Archivotxt()
            pasw_generator()
            os.system("pause")
            os.system("cls")
        elif seleccion == 2:
            os.system("cls")
            crear_Archivotxt()
            pasw_easy_read()
            os.system("pause")
            os.system("cls")
        elif seleccion == 3:
            os.system("cls")
            ya_existe()
            os.system("pause")
            os.system("cls")
        elif seleccion == 4:
            os.system("cls")
            historial_contras()
            os.system("pause")
            os.system("cls")
        elif seleccion == 5:
            os.system("cls")
            print("Saliendo del programa")
            break
        else:
            print("Introduce un opcion valida XD")
