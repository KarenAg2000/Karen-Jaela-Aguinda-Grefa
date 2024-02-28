def buscar_valor(matriz, valor):
    for k in range(len(matriz)):
        for j in range(len(matriz[k])):
            if matriz[k][j] == valor:
                return True, (k, j)
    return False, None

matriz = [
    [21, 22, 23],
    [24, 25, 26],
    [27, 28, 29]
]

valor_buscar = 25

encontrado, posicion = buscar_valor(matriz, valor_buscar)

if encontrado:
    print(f"El valor {valor_buscar} se encontró en la posición {posicion}")
else:
    print(f"El valor {valor_buscar} no se encontró en la matriz.")
