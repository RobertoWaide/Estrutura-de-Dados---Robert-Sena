def potencia(x, n):
    if n == 0:
        return 1
    elif n > 0:
        return x * potencia(x, n - 1)
    else:
        return 1 / potencia(x, -n)


print(potencia(2, -3))  
print(potencia(5, 0))   
print(potencia(3, 4))  
