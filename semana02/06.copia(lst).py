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

def copia(lst):
    copia_lst = lst
    return copia_lst


lst = None

for i in range(6):
    n = int(input("Digite um número: "))
    lst = insere_lista(lst, n)

print("Lista original:")
imprime_lista(lst)
copia_lst = copia(lst)
print("Lista copia:")
imprime_lista(copia_lst)
