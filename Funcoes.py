from time import *
from Algoritmos import *
from Listas import *

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

    #Obtem a escolhado usuário
def escolhaUsuario():
    escolha = input('Sua escolha: ')
    return escolha

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

def comparaAlgoritimos(tempoB, tempoA):
    difTempo = tempoB - tempoA
    return print('A diferença de tempo entre os dois algoritmos e de: %f' %difTempo)