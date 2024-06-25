def sucessor(n):
    return n + 1

def predecessor(n):
    return n - 1

def calcula_soma(x, y):
    if y == 0:
        return x
    else:
        return calcula_soma(sucessor(x), predecessor(y))

print(calcula_soma(5, 3))  
print(calcula_soma(10, 7)) 
