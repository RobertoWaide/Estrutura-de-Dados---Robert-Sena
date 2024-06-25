def imprimir(min, max):
    if min > max:
        return
    else:
        print(min)
        imprimir(min + 1, max)

imprimir(1, 5)
