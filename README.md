Script para organizar archivos en carpetas segun su mimetype.

El mimetype de un archivo puede ser: text, video, image, audio o application.

# ¿Como hacerlo funcionar?

## Instalación

Descarga e enstala [Python](https://www.python.org/downloads/)

Abre el shell del sistema y ejecuta el siguiente comando:

    pip install git+https://github.com/CalumRakk/sort_files

## Ejecutar el script usando shell

El siguiente comando organiza los archivos de la carpeta en la ruta `"D:\Usuarios\User\Descargas"`:

    sort_files "D:\Usuarios\User\Descargas"

## Ejecutar el script usando un archivo .bat

Crea un archivo de texto en la carpeta que desea organizar y copia el siguiente código dentro:

```text
sort_files "%CD%"
pause
```

Ahora, cambiale la extesión del archivo a `.bat` y listo.

El siguiente video es un ejemplo usando un archivo `.bat`

https://github.com/CalumRakk/sort_files/assets/31534753/e8d89d9c-a9d8-42c8-b82f-0ebb914b67ea
