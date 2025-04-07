import os
import datetime

if __name__ == "__main__":
    print("Este es el archivo Principal ")

# Nombrede ruta de script de python
# print(type(os.getcwd()))
# C:\Users\landomos\Documents\Pasw_Generador

# Listar directorios en el directorio actual
# print(os.listdir(".venv"))
# ['.gitignore', 'Include', 'Lib', 'pyvenv.cfg', 'Scripts']

# Unir direciones
# print(os.path.join(os.getcwd(), "Nuevas contraseñas"))
# C:\Users\landomos\Documents\Pasw_Generador\Nuevas contraseñas

# Crear carpeta
# try:
#   os.mkdir("Nuevas contraseñas ")
# except FileExistsError:
#   print("Ya existe esa carpeta ")
# else:
#   print("Carpeta Creada ")

# Crear una carpeta dentro de otra carpeta
# try:
# os.makedirs(os.path.join("Nuevas contraseñas", "contras"))
# except FileExistsError:
# print("Ya existe esa carpeta ")
# else:
# print("Carpetas Creadas ")

# Renombrar carpeta
# os.rename("Nuevas contraseñas", "Nuevas")

# Renombra varios archivos a la vez
# for file in os.listdir():
#  if file.endswith(".txt"):
#      os.rename(file, f"nuevo_{file}")
# print(file)


# Comprobar si existe
# if os.path.exists("Nuevas") == True:
#   for file in os.listdir():
#      print(file)
# else:
#   print("No existe ")


def crear_Archivotxt():
    os.chdir(os.getcwd())
    if os.path.exists(f"{datetime.date.today()} Nuevas_Contraseñas.txt") == True:
        print(
            f"Ya existe este archivo {datetime.date.today()} Nuevas_Contraseñas.txt")
    else:
        with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", "w", encoding="utf-8"):
            with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", "a", encoding="utf-8") as fichero:
                fichero.writelines(
                    f" Tabla de Contraseñas Generadas {datetime.date.today()}     \n ")


def ya_existe():
    while True:
        try:
            seleccion = input("Ingrese la contraseña a comprobar: ")
            with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", "r", encoding="utf-8") as fichero:
                contenido = fichero.read()  # Almacenamos el contenido del archivo
                if seleccion in contenido:
                    print(f"Ya existe la contraseña {seleccion}")
                    break
                else:
                    print(f"No se a encontrado la contraseña {seleccion} ")
                    break  # Si la contraseña ya existe, salimos del ciclo
        except FileNotFoundError:
            print("El archivo no existe o no se ha creado.")
            break  # Si no se encuentra el archivo, salimos del ciclo
        except Exception as e:
            print(f"Se ha producido un error: {e}")


def historial_contras():
    try:
        with open(f"{datetime.date.today()} Nuevas_Contraseñas.txt", "r", encoding="utf-8") as fichero:
            contenido = fichero.readlines()  # Almacenamos el contenido del archivo
            for con in contenido:
                print(con)
    except FileNotFoundError:
        print("El archivo no existe o no se ha creado.")
