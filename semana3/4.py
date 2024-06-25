def s(n, d):
    if d > 50:
        return 0
    else:
        return (2*d - 1) / d + s(n + 1, d + 1)

resultado = s(1, 1)
print(resultado)  
