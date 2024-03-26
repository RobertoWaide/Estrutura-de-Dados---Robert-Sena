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

def retira_n(lst,valor):
    atual = lst 
    ant = None 
    while atual is not None:
        if atual.info == valor:
            if ant is not None:
                ant.prox = atual.prox
            else:
                lst = atual.prox
            atual = atual.prox
        else:
            ant = atual
            atual = atual.prox
    return lst
    

lst = None
for i in range(5):
    n = int(input("Digite um número: "))
    lst = insere_lista(lst, n)



valorblabla = int(input(f"Digite um número para verificar se está na lista: "))
print("Lista antes da retirada:")
imprime_lista(lst)

lst = retira_n(lst, valorblabla)

print("Lista após a retirada:")
imprime_lista(lst)
