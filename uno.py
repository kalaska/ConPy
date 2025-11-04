#!/usr/bin/env python3
import argparse
from pathlib import Path
import sys

from arrays import ArrayList


def pintaArray(arr):
    for i in range(arr.size):
        print(f"{i+1:4}: {arr.get(i)}") 

def leer_lineas(path):
    with open(path, 'r', encoding='utf-8') as f:
        lineas = ArrayList()
        for i, linea in enumerate(f, 1):
            lineas.add(linea.rstrip())
        return lineas

def sumaArray(lineas):
    suma=0
    for i in range(lineas.size):
        s = lineas.get(i)
        try:
            if s.lstrip("+-").isdigit():
                suma+= int(s)
        except ValueError:
            print("La cadena no es un entero válido")
    return suma

def main():
    parser = argparse.ArgumentParser(description="Ejemplo: leer un fichero y mostrarlo por líneas")
    parser.add_argument('file', type=str, help='Ruta al fichero a leer')
    args = parser.parse_args()

    path = Path(args.file)
    if not path.exists():
        print(f"Error: no existe {path}", file=sys.stderr)
        sys.exit(2)
    if not path.is_file():
        print(f"Error: {path} no es un fichero regular", file=sys.stderr)
        sys.exit(3)

    lineas = ArrayList()
    try:
        lineas = leer_lineas(path)
    except Exception as e:
        print(f"Error al leer {path}: {e}", file=sys.stderr)
        sys.exit(1)
    suma = sumaArray(lineas)
    print(f"Suma de líneas: {suma}")
    pintaArray(lineas)
if __name__ == '__main__':
    main()
