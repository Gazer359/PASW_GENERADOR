import random
import string
import os
from rich.progress import Progress
import time
import datetime


with Progress() as progress:
    task2 = progress.add_task("[green]Processing...", total=100)

    while not progress.finished:
        progress.update(task2, advance=0.6)
        time.sleep(0.02)


def pasw_generator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits

    caracteres = lower + upper + num + string.punctuation

    try:
        longitud_contra = int(input("Longitud de la contraseña -> "))
        cantidad_contr = int(input("Numero de contraseñas a generar -> "))
        os.system("cls")
    except ValueError as e:
        print(f"Error {e} ")
    else:
        for pasword in range(cantidad_contr):
            try:
                N_contraseña = random.sample(caracteres, longitud_contra)

                if longitud_contra <= 10:
                    with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", 'a', encoding="utf-8") as fichero:
                        fichero.writelines(
                            f"\n | {pasword + 1} -> {"".join(N_contraseña)}| Moderada")
                else:
                    with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", 'a', encoding="utf-8") as fichero:
                        fichero.writelines(
                            f"\n | {pasword + 1} -> {"".join(N_contraseña)}| Buena ")
            except ValueError as e:
                print(f"Error {e}")
    print("\n")
    print(f"{cantidad_contr} contraseñas creadas satisfactoriamente ")
    print(os.path.abspath(
        f"{datetime.date.today()} Nuevas_Contraseñas.txt"))

    print("""
───────▄▀▀▄─
───────█──█────────────
───────█──█▄▄
───────█──█──█▀▀▄▄─────
───▄▄▄─█──█──█──█─▀▄───
───█──▀█────────▀──█───
────▀▄─█───────────█───
─────▀▄───────────█────
──────▀▄──────────█────
───────▀▄────────█─────
────────█▄▄▄▄▄▄▄▄█─────""")


def pasw_easy_read():
    try:
        cantidadcontra = int(input("Cantidad de contraseñas: "))
    except ValueError as e:
        print(f"Error {e}")
    else:
        separadores = [",", "!", "/", "-", "_", "?"]
        os.system("cls")
        for pasw in range(cantidadcontra):
            with open("words.txt", mode="r", encoding="utf-8") as archivo:
                palabras = archivo.read().splitlines()
                sep = random.choice(separadores)
                w1 = palabras[random.randint(2, 64000)]
                w2 = palabras[random.randint(1, 64000)]
                w3 = palabras[random.randint(3, 64000)]
                with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", 'a', encoding="utf-8") as fichero:
                    fichero.writelines(
                        f"\n{pasw+1} -> {w1}{sep}{w2}{sep}{w3} \n")
        print(f"{cantidadcontra} contraseñas creadas satisfactoriamente ")
        print(os.path.abspath(
            f"{datetime.date.today()} Nuevas_Contraseñas.txt"))

        print("""
───────▄▀▀▄─
───────█──█────────────
───────█──█▄▄
───────█──█──█▀▀▄▄─────
───▄▄▄─█──█──█──█─▀▄───
───█──▀█────────▀──█───
────▀▄─█───────────█───
─────▀▄───────────█────
──────▀▄──────────█────
───────▀▄────────█─────
────────█▄▄▄▄▄▄▄▄█─────""")


if __name__ == "__main__":
    print("Este es el archivo Principal ")
