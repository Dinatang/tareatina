
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

no_fila = 0
busqueda = 9

for fila in matriz:
    no_columna = 0
    for columna in fila:
        if (columna ==busqueda):
            print(f"No.{busqueda},posicion es: [{no_fila}][{no_columna}]")
        no_columna += 1
    no_fila += 1



