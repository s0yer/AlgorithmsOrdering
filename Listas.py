
def criaLista1():
    lista1 = [10,20,4,30,40,33,88,122]
    return lista1

def listaFibonacci(n):
    a, b = 0, 1
    lista =[a,b]
    for i in range(0, n):
        a, b = b, a + b
        lista.append(b)
    return lista

