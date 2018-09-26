from Listas import *
from random import *


def main():
    novalista = criaLista1()
    print(sorted(novalista))

    listaFib = listaFibonacci(10)
    shuffle(listaFib)
    print(listaFib)
    print(sorted(listaFib))

main()
