from random import *

#cria lista de tamanho n embaralhada
def listaRandom(n):
    lista2 = [0]
    for i in range(0, n):
        a = randrange(0, 100)
        lista2.append(a)
    return lista2

#cria lista de fibonacci em ordem
def listaFibonacci(n):
    a, b = 0, 1
    lista =[a,b]
    for i in range(0, n):
        a, b = b, a + b
        lista.append(b)
    return lista

