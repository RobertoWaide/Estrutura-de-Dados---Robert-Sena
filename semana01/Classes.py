class lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None
    
   
def cria_lista():
    return lista()

def insere_lista(lst, valor):
    novo = lista(valor)
    novo.prox = lst
    return novo

def imprime_lista(lst):
    atual = lst
    while atual is not None:
        print(atual.info)
        atual = atual.prox

def busca_lista(lst, valor):
    atual = lst
    while atual is not None:
        if atual.info == valor:
            return True 
        atual = atual.prox
    return False

def lista_retira(lst, valor):
    if lst is None:
        return lst
    
    if lst.info == valor:
        lst = lst.prox
        return lst
    
    atual = lst
    while atual.prox is not None:
        if atual.prox.info == valor:
            atual.prox = atual.prox.prox
            return lst
        atual = atual.prox
    return lst

lst = None
lst = insere_lista(lst, 50)
lst = insere_lista(lst, 60)
lst = insere_lista(lst, 70)

valorblabla = int(input(f"Digite um número para verificar se está na lista: "))

busca = busca_lista(lst, valorblabla)
print("Lista antes da retirada:")
imprime_lista(lst)
print("Elemento encontrado:", busca)

lst = lista_retira(lst, valorblabla)

print("Lista após a retirada:")
imprime_lista(lst)

