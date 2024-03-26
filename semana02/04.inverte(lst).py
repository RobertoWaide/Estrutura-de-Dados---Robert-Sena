class lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def insere_lista(lst, valor):
    novo = lista(valor)
    novo.prox = lst
    return novo

def imprime_lista(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def inverte(lst):
    atual = lst
    lst = None
    temp = []
    while atual is not None:
        temp.append(atual.info)
        atual = atual.prox
    temp.reverse()
    for n in temp:
        lst = insere_lista(lst, n)
    return lst


lst = None

for i in range(6):
    n = int(input("Digite um número: "))
    lst = insere_lista(lst, n)

print("Lista antes da retirada:")
imprime_lista(lst)

lst = inverte(lst)

print("Lista inversa:")
imprime_lista(lst)
 
