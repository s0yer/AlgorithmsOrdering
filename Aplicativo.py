#Libraries imported
#Bibliotecas importadas
from Listas import *
from random import *
from Algoritmos import *
from time import *

def main():

    #Create new established list and sort
    #Cria nova lista estabelecida e ordena
    novalista = listaRandom(10)
    print(sorted(novalista))

    #Create a Fibonacci Sequence with 'n' positions
    #Cria uma Sequencia de Fibonacci com 'n' posições
    listaFib = listaFibonacci(10**3)

    
    #Shuffles the list -> listaFib
    #Embaralha a lista -> listaFib
    shuffle(listaFib)
    print(listaFib)
    
    #Order and check execution time Insertion Sort
    #Ordena e verifica tempo de Execução Insertion Sort
    inicio = time()
    print(insertionSort(listaFib))
    fim=time()
    print('Tempo de execução InsertionSort: %f'  %(fim-inicio))
    
    #Shuffles the list -> listaFib
    #Embaralha a lista -> listaFib
    shuffle(listaFib)
    print(listaFib)
    
    #Order and check runtime Bubble Sort
    #Ordena e verifica tempo de Execução Bubble Sort
    inicio = time()
    print(bubbleSort(listaFib))
    fim = time()
    print('Tempo de execução BubbleSort: %f' %(fim - inicio))

main()
