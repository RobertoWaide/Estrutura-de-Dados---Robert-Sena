def binario(x):
    if x > 1:
        binario(x // 2)
    print(x % 2, end='')

binario(12) 
print()     
binario(5)   
print()      

binario(31) 
print()    
