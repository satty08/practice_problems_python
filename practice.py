def countPrimes(n):
    if n == 0 or n == 1:
        return 0
    count = 0
    for i in range(2, n):
        if isPrime(i):
            count += 1
                
    return count
    
def isPrime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

print(countPrimes(12))