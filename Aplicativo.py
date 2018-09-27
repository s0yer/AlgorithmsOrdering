#Bibliotecas importadas
from Listas import *
from random import *
from Algoritmos import *
from time import *

def main():

    #Cria nova lista estabelecida e ordena
    novalista = criaLista1()
    print(sorted(novalista))

    #Cria uma Sequencia de Fibonacci com 'n' posições
    listaFib = listaFibonacci(10**3)

    #Verifica se a lista está desordenada
    shuffle(listaFib)
    print(listaFib)

    #Ordena e verifica tempo de Execução Insertion Sort
    inicio = time()
    print(insertionSort(listaFib))
    fim=time()
    print('Tempo de execução InsertionSort: %f'  %(fim-inicio))

    #Verifica se a lista está desordenada
    shuffle(listaFib)
    print(listaFib)

    #Ordena e verifica tempo de Execução Bubble Sort
    inicio = time()
    print(bubbleSort(listaFib))
    fim = time()
    print('Tempo de execução BubbleSort: %f' %(fim - inicio))

main()
