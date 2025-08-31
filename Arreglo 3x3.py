matriz = [
    [4, 2, 13],
    [9, 6, 3],
    [1, 5, 15]
]


def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)  #  (fila, columna)
    return None


valor_b= int(input("Ingrese el valor a buscar en la matriz:"))


posicion = buscar_valor(matriz, valor_b)


if posicion:
    print(f"El valor {valor_b} se encontró en la posición fila {posicion[0] + 1}, columna {posicion[1] + 1}.")
else:
    print(f"El valor {valor_b} no se encontró en la matriz.")