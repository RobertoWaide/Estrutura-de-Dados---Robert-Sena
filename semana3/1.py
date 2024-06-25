def produto(n):
    if n == 1:
        return 1
    else:
        return n * produto(n - 1)
print(produto(5))  
print(produto(6))
