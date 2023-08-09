
from typing import List
from pathlib import Path
import os
import mimetypes

import filetype

def get_mimetype(file):
    kind = filetype.guess(file)
    if kind:
         mime= kind.mime 
    else:
        mime, _ = mimetypes.guess_type(file)
    
    if mime is None:
        print("No mimetype", file)
        return None
    return mime


def obtener_todos_los_archivos(ruta)->List[Path]:
    archivos = []
    for raiz, directorios, archivos_en_dir in os.walk(ruta):
        for archivo in archivos_en_dir:
            archivos.append(Path(os.path.join(raiz, archivo)))
    return archivos