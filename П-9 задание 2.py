def is_prime_recursive(n, divisor=None):
    if n <= 1:           
        return False
    if divisor is None:  
        divisor = min(n // 2, 2)
    if divisor == 1:     
        return True
    if n % divisor == 0: 
        return False
    return is_prime_recursive(n, divisor - 1)  



n = int(input())

if is_prime_recursive(n):
    print('YES')
else:
    print('NO')
