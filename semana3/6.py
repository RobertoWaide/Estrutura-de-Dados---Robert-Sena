def busca_binaria(vet, v, inf, sup):
    if inf > sup:
        return False
    else:
        meio = (inf + sup) // 2
        if vet[meio] == v:
            return meio
        elif vet[meio] > v:
            return busca_binaria(vet, v, inf, meio - 1)
        else:
            return busca_binaria(vet, v, meio + 1, sup)

vet = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
v = 7
resultado = busca_binaria(vet, v, 0, len(vet) - 1)
print(resultado) 

v = 4
resultado = busca_binaria(vet, v, 0, len(vet) - 1)
print(resultado)  
