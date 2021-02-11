try:
    def calPrime(n):
        primes = [2]
        for i in range(3, n+1):
            flag = 0
            for j in primes[::-1]:
                if i%j == 0:
                    flag = 1
                    break
            if flag == 0:
                primes.append(i)
        return primes
    
    test = int(input())
    for i in range(test):
        x, y = map(int, input().split())
        count = 0
        if x < y:
            print('Chef')
            continue
        xprime = calPrime(x)
        if len(xprime) > y:
            print('Divyam')
            continue
        print('Chef')
        

except:
    pass
