
def criaLista1():
    lista1 = [10,20,4,30,40,33,88,122]
    return lista1

def listaFibonacci(numero):
    if numero < 2:
        return numero
    return listaFibonacci(numero - 2) + listaFibonacci(numero - 1)

