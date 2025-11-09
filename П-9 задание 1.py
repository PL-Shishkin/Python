def remainder(a, b):
    if a < b:
        return a
    else:
        return remainder(a - b, b)

a = 10
b = 3
print(remainder(a, b))  
