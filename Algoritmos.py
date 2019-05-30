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


def mergeSort(array):
    if len(array) > 1:
        mid = len(array) // 2  # Finding the mid of the array
        L = array[:mid]  # Dividing the array elements
        R = array[mid:]  # into 2 halves

        mergeSort(L)  # Sorting the first half
        mergeSort(R)  # Sorting the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

    return array

def QuickSort(lista, inicio, fim):
    if inicio < fim:
        divide = partition(lista, inicio, fim)
        QuickSort(lista, inicio, divide -1)
        QuickSort(lista, divide+1, fim)
        return lista
    else:
        return lista

def partition(list, start, end):
    pivot = list[end]
    bottom = start-1
    top = end

    done = 0
    while not done:

        while not done:
            bottom = bottom + 1

            if bottom == top:
                done = 1
                break

            if list[bottom] > pivot:
                list[top] = list[bottom]
                break

        while not done:
            top = top - 1

            if top == bottom:
                done = 1
                break

            if list[top] < pivot:
                list[bottom] = list[top]
                break

    list[top] = pivot
    return top



