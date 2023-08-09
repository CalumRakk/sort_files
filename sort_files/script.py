#
from pathlib import Path
from .utils import obtener_todos_los_archivos, get_mimetype

def organizar(folder:Path):
    for file in folder.glob("*"):
        if file.is_dir(): continue            
        if file.name.endswith(".bat"): continue
            
        try: 
            mime= get_mimetype(file)
        except FileNotFoundError:
            continue
        if mime is None: continue

        dirname= mime.split("/")[0]  
        parent= file.parent.joinpath(dirname)
        parent.mkdir(exist_ok=True)
        newpath= parent.joinpath(file.name)
        file.rename(newpath)

    

    
