from time import *
from Algoritmos import *
from Listas import *


#calcula e retorna o tempo de execução do algoritmo InsertionSort
def tempoExeInsertionSort(lista):

    # Order and check execution time Insertion Sort
    # Ordena e verifica tempo de Execução Insertion Sort
    embaralhaLista(lista)
    inicio = time()
    insertionSort(lista)
    fim = time()
    print(lista)
    tempoInsertion = fim - inicio
    print('Tempo de execução InsertionSort: %f' % (tempoInsertion))
    return tempoInsertion

#Calcula e retorna o tempo de execução do algoritmo BubleSort
def tempoExeBubbleSort(lista):

    # Order and check runtime Bubble Sort
    # Ordena e verifica tempo de Execução Bubble Sort
    embaralhaLista(lista)
    inicio = time()
    bubbleSort(lista)
    fim = time()
    print(lista)
    tempoBubble = fim - inicio
    print('Tempo de execução BubbleSort: %f' % (tempoBubble))
    return tempoBubble

#Calcula e retorna o tempo de execução do algoritmo SelectionSort
def tempoExeSelectionSort(lista):
    embaralhaLista(lista)
    inicio = time()
    selectionSort(lista)
    fim = time()
    print(lista)
    tempoSelection = fim - inicio
    print('Tempo de execução SelectionSort: %f' % (tempoSelection))
    return tempoSelection

#Calcula e retorna o tempo de execução do algoritmo ShellSort
def tempoExeShellSort(lista):
    embaralhaLista(lista)
    inicio = time()
    shellSort(lista)
    fim = time()
    print(lista)
    tempoShell = fim - inicio
    print('Tempo de execução ShellSort: %f' % (tempoShell))
    return tempoShell

#Calcula e retorna o tempo de execução do algoritmo MergeSort
def tempoExeMergeSort(lista):
    embaralhaLista(lista)
    inicio = time()
    mergeSort(lista)
    fim = time()
    print(lista)
    tempoMerge = fim - inicio
    print('Tempo de execução MergeSort: %f' % (tempoMerge))
    return tempoMerge

    # Calcula e retorna o tempo de execução do algoritmo MergeSort
def tempoExeQuickSort(lista, tamanhoLista):
    embaralhaLista(lista)
    inicio = time()
    QuickSort(lista, lista[0], lista[tamanhoLista])
    fim = time()
    print(lista)
    tempoQuick = fim - inicio
    print('Tempo de execução QuickSort: %f' % (tempoQuick))
    return tempoQuick

    #Obtem a escolhado usuário
def escolhaUsuario():
    escolha = input('Sua escolha: ')
    return escolha

    #Obtem o valor do tamanho do vetor que será escolhido pelo usuário
def obtemValorLista():
    valor = input('digite um valor: ')
    return valor

    #Embaralha a lista q foi passada
def embaralhaLista(lista):
    lista = shuffle(lista)
    return lista

    #Executa a ordenação InsertionSort para a lista passada como parâmetro
def executaInsertionSort(lista):
    print(insertionSort(lista))
    return lista

    #Executa a ordenação BubbleSort para a lista passada como parâmetro
def executaBubbleSort(lista):
    print(bubbleSort(lista))
    return lista

    #Função que compara tempo de execução de 2 algorítmos
def comparaAlgoritimos(tempoBubble, tempoSelection):
    difTempo = tempoBubble - tempoSelection
    return print('A diferença de tempo entre os dois algoritmos e de: %f' %difTempo)

    #Função que acha o menor valor e maior valor de tempo dos algorítmos
def comparaTodosAlgoritimos(tempoBubble, tempoInsertion, tempoSelection, tempoShell, tempoMerge, tempoQuick):

    #construção do array com os tempos de execução dos algoritimos
    arrayTempos = [tempoBubble]
    arrayTempos.append(tempoInsertion)
    arrayTempos.append(tempoSelection)
    arrayTempos.append(tempoShell)
    arrayTempos.append(tempoMerge)
    arrayTempos.append(tempoQuick)

    menorTempo = min(arrayTempos)
    maiorTempo = max(arrayTempos)

    print('O menor tempo é igual a : %f' %menorTempo)
    print('O maior tempo é igual a : %f' %maiorTempo)

    return (menorTempo,maiorTempo)