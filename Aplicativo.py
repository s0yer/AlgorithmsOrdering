#Libraries imported
#Bibliotecas importadas
from Funcoes import *
from Listas import *



def main():

    lista = 0
    tamanhoLista = 0

    #interface com o usuário
    esperando_entrada = True

    while esperando_entrada:
        print('Escolha a opção: ')

        print('d: Define o tamanho da lista | l: Cria lista de tamanho n random')
        print('f: Cria lista fibonacci de tamanho n embaralhada | p: Imprime Lista')
        print('r: Embaralha lista ')
        print('i: Tempo de execução InsertionSort | b: Tempo de execução BubbleSort')
        print('s: Tempo de execução SelectionSort | m: Tempo de execução MergeSort')
        print('q: Tempo de execução QuickSort')
        print('c: Compara tempos de execução do BubbleSort com InsertionSort')
        print('t: Compara TODOS tempos de execução')
        print('e: Exit / Sair ')

        escolha = escolhaUsuario()

        if escolha == 'd':
            tamanhoLista = int(obtemValorLista())

        elif escolha == 'l':
            lista = listaRandom(tamanhoLista)

        elif escolha == 'f':
            lista = listaFibonacci(tamanhoLista)

        elif escolha == 'p':
            print(lista)

        elif escolha == 'r':
            embaralhaLista(lista)

        elif escolha == 'i':
            tempoExeInsertionSort(lista)

        elif escolha == 'b':
            tempoExeBubbleSort(lista)

        elif escolha == 's':
            tempoExeSelectionSort(lista)

        elif escolha == 'h':
            tempoExeShellSort(lista)

        elif escolha == 'm':
            tempoExeMergeSort(lista)

        elif escolha == 'q':
            tempoExeQuickSort(lista, tamanhoLista)

        elif escolha == 'c':
            comparaAlgoritimos(tempoExeBubbleSort(lista),tempoExeInsertionSort(lista))

        elif escolha == 't':
            print(comparaTodosAlgoritimos(tempoExeBubbleSort(lista), tempoExeInsertionSort(lista), tempoExeSelectionSort(lista), tempoExeShellSort(lista), tempoExeMergeSort(lista), tempoExeQuickSort(lista, tamanhoLista)))

        elif escolha == 'e':
            esperando_entrada = False

        else:
            print('Entrada inválida, pegue um valor das opções! ')


main()