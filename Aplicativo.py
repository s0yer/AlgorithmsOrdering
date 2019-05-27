#Libraries imported
#Bibliotecas importadas
from Funcoes import *
from Listas import *



def main():

    #interface com o usuário
    esperando_entrada = True

    while esperando_entrada:
        print('Escolha a opção: ')

        print('d: Define o tamanho da lista')
        print('l: Cria lista de tamanho n random')
        print('f: Cria lista fibonacci de tamanho n embaralhada')
        print('p: Imprime lista')
        print('r: Embaralha lista')
        print('i: Tempo de execução InsertionSort')
        print('b: Tempo de execução BubbleSort')
        print('s: Tempo de execução SelectionSort')
        print('c: Compara tempos de execução do BubbleSort com InsertionSort')
        print('t: Compara TODOS tempos de execução')
        print('e: Exit / Sair ')

        escolha = escolhaUsuario()

        if escolha == 'd':
            valorLista = int(obtemValorLista())

        elif escolha == 'l':
            lista = listaRandom(valorLista)

        elif escolha == 'f':
            lista = listaFibonacci(valorLista)

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

        elif escolha == 'c':
            comparaAlgoritimos(tempoExeBubbleSort(lista),tempoExeInsertionSort(lista))

        elif escolha == 't':
            print(comparaTodosAlgoritimos(tempoExeBubbleSort(lista), tempoExeInsertionSort(lista), tempoExeSelectionSort(lista), tempoExeShellSort(lista)))

        elif escolha == 'e':
            esperando_entrada = False

        else:
            print('Entrada inválida, pegue um valor das opções! ')


main()