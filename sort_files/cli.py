#
import argparse
from .script import organizar
from pathlib import Path

def run_script():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type=str, help="ruta de la carpeta")

    args = parser.parse_args()
    organizar(Path(args.path))