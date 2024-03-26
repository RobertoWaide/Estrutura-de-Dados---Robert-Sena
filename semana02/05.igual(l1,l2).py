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


def igual(lst,lst2):
    while lst is not None:
        if lst.info == lst2.info:
            lst = lst.prox
            lst2 = lst2.prox
        else:
            return False
    return True


lst = None
lst2 = None


for i in range(3):
    n = int(input("Digite um número: "))
    lst = insere_lista(lst, n)
    n = int(input("Digite um número: "))
    lst2 = insere_lista(lst2, n)

ingual = igual(lst,lst2)

print(f"As lista sendo iguais corresponde como {ingual}")
