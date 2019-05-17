#Libraries imported
#Bibliotecas importadas
from Listas import *
from random import *
from Funcoes import *
from Algoritmos import *


def main():
    esperando_entrada = True

    while esperando_entrada:
        print('Escolha a opção: ')
        print('l: cria lista de tamanho n random')
        print('f: cria lista fibonacci de tamanho n embaralhada')
        print('p: Mostrar os participantes:')
        print('m: Minerar um novo bloco')
        print('h: Manipular o blockchain')
        print('o: Obtem saldo do participante')
        print('s: Sair. ')

    escolha = escolhaUsuario()

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
    

    
    #Shuffles the list -> listaFib
    #Embaralha a lista -> listaFib
    shuffle(listaFib)
    print(listaFib)
    


main()
