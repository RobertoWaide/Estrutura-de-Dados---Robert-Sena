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


def separa(lst, valor):
    atual = lst
    lst = None
    lst2 = None
    freeza = False
    while atual is not None:
        if atual.info == valor:
            freeza = True
            lst = insere_lista(lst, atual.info)
        elif freeza:
            lst2 = insere_lista(lst2, atual.info)
        else:
            lst = insere_lista(lst, atual.info)
        atual = atual.prox

    return lst, lst2
 
lst = None
for i in range(5):
    n = int(input("Digite um número: "))
    lst = insere_lista(lst, n)



valorblabla = int(input(f"Digite um número para separar a lista: "))
print("Lista antes da retirada:")
imprime_lista(lst)

lst, lst2 = separa(lst, valorblabla)

print("Lista 1:")
imprime_lista(lst)
print("Lista 2:")
imprime_lista(lst2)
