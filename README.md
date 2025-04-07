# PASW_GENERADOR

# Manual de Uso: Generador de Contraseñas

Este programa permite generar contraseñas de forma aleatoria, generar contraseñas fáciles de leer, consultar si una contraseña ya existe en el historial y ver el historial de contraseñas generadas.

## Requisitos

- Python 3.x
- Librerías: `os`, `time`
- Módulos adicionales: `Pasw_Generador` (para generar contraseñas) y `OS_manager` (para gestionar archivos y el historial de contraseñas)

## Funcionalidades

El programa ofrece un menú con las siguientes opciones:

1. **Generador de contraseñas aleatorias**: Crea una contraseña aleatoria y la guarda en un archivo de texto.
2. **Generador de contraseñas fáciles de leer**: Crea una contraseña fácil de recordar y la guarda en un archivo de texto.
3. **Consultar si ya existe una contraseña**: Verifica si la contraseña ya ha sido creada anteriormente.
4. **Consultar historial de contraseñas**: Muestra todas las contraseñas generadas en sesiones anteriores.
5. **Salir**: Termina la ejecución del programa.

## Instrucciones de Uso

### 1. Generar una Contraseña Aleatoria

Selecciona la opción `1` para generar una contraseña aleatoria. El programa la creará y la guardará en un archivo de texto.

### 2. Generar una Contraseña Fácil de Leer

Selecciona la opción `2` para generar una contraseña fácil de recordar. Esta también será guardada en un archivo de texto.

### 3. Consultar si la Contraseña Ya Existe

Selecciona la opción `3` para verificar si una contraseña ya ha sido generada previamente.

### 4. Ver el Historial de Contraseñas

Selecciona la opción `4` para ver todas las contraseñas generadas en sesiones anteriores.

### 5. Salir del Programa

Selecciona la opción `5` para salir del programa.

## Código Explicado

El programa consiste en un ciclo `while True` que presenta un menú y espera la selección del usuario. Dependiendo de la opción seleccionada, el programa ejecutará diferentes funciones importadas de otros módulos.

### Librerías Importadas

- **Pasw_Generador**: Contiene las funciones `pasw_generator` y `pasw_easy_read`, que se encargan de generar contraseñas aleatorias y fáciles de leer respectivamente.
- **OS_manager**: Contiene las funciones `crear_Archivotxt`, `ya_existe`, y `historial_contras`, que gestionan los archivos de contraseñas y permiten consultar el historial o verificar si una contraseña ya existe.

### Funciones Principales

- `crear_Archivotxt()`: Crea un archivo de texto donde se almacenan las contraseñas generadas.
- `pasw_generator()`: Genera una contraseña aleatoria.
- `pasw_easy_read()`: Genera una contraseña fácil de recordar.
- `ya_existe()`: Verifica si una contraseña ya existe en el historial.
- `historial_contras()`: Muestra el historial de contraseñas generadas.

## Ejemplo de Ejecución

```bash
──────██████.
──▄▀▀▀▄───────────────
──█───█───────────────
─███████─────────▄▀▀▄─
░██───██░░█▀█▀▀▀▀█░░█░
░███▄███░░▀░▀░░░░░▀▀░░

 BIENVENIDO GENERADOR DE CONTRASEÑAS.

1.Generador de contraseñas aleatorias
2.Generador de contraseñas fáciles de leer
3.Consultar si ya existe una contraseña
4.Consultar el historial de contraseñas creadas
5.Salir del Programa

Ingresar una de las opciones: 1
