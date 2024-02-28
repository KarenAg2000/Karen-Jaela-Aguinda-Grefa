def ordenar_fila(matriz, fila):
    n = len(matriz[0])
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if matriz[fila][j] < matriz[fila][min_index]:
                min_index = j
        if min_index != i:
            matriz[fila][i], matriz[fila][min_index] = matriz[fila][min_index], matriz[fila][i]



matriz = [
    [19, 75, 27],
    [34, 52, 66],
    [78, 81, 93]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 19


ordenar_fila(matriz, fila_a_ordenar)

print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
