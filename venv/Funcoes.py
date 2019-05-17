from time import *

def tempoExeInsertionSort():

    # Order and check execution time Insertion Sort
    # Ordena e verifica tempo de Execução Insertion Sort
    inicio = time()
    print(insertionSort(listaFib))
    fim = time()
    return print('Tempo de execução InsertionSort: %f' % (fim - inicio))

def tempoExeBubbleSort():

    # Order and check runtime Bubble Sort
    # Ordena e verifica tempo de Execução Bubble Sort
    inicio = time()
    print(bubbleSort(listaFib))
    fim = time()
    return print('Tempo de execução BubbleSort: %f' % (fim - inicio))

def escolhaUsuario():
    escolha = input('Sua escolha: ')
    return escolha