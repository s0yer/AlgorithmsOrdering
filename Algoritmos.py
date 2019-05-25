
# Algorithms Functions

# Algoritmo InsertionSort implementado
def insertionSort(k):
    for i in range(1,len(k)):
        j = i
        temp = k[j]
        while j > 0 and temp < k[j-1]:
            k[j] = k[j-1]
            j = j-1
        k[j] = temp
    return k

# Algoritmo BubleSort implementado
def bubbleSort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
          if lista[i] > lista[i+1]:
               lista[i], lista[i+1] = lista[i+1],lista[i]
               ordenado = False
    return lista

# Algorítmo SelectionSort implementado
def selectionSort(A):
    for i in range(len(A)):

        # Encontra o elemento mínimo no vetor não classificado
        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        # Troca o elemento mínimo encontrado com o primeiro elemento
        A[i], A[min_idx] = A[min_idx], A[i]

    return A


def shellSort(array):
    # Classificação do shell usando o seq de gap: n/2, n/4, ..., 1.
    gap = len(array) // 2

    # Loop sobre os gaps
    while gap > 0:

        # Faz o insertionSort
        for i in range(gap, len(array)):
            val = array[i]
            j = i
            while j >= gap and array[j - gap] > val:
                array[j] = array[j - gap]
                j -= gap
            array[j] = val

        gap //= 2
    return array