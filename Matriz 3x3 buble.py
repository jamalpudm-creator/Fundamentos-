#  QuickSort
def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[len(lista) // 2]
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)


def ordenar_fila_matriz(matriz, fila):
    print("\nMatriz original:")
    for fila_m in matriz:
        print(fila_m)


    matriz[fila] = quicksort(matriz[fila])

    print(f"\nMatriz con la fila {fila} ordenada:")
    for fila_m in matriz:
        print(fila_m)


if __name__ == "__main__":

    matriz = [
        [12, 22, 2],
        [6, 3, 14],
        [32, 9, 24]
    ]

    print("Matriz inicial:")
    for f in matriz:
        print(f)

    fila = int(input("\nElige la fila que deseas ordenar (1, 2 o 3): "))

    if 1 <= fila <= len(matriz):
        ordenar_fila_matriz(matriz, fila - 1)
    else:
        print("❌ Número inválido.")
