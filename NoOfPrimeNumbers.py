def ifPrime(n):
    if(n ==1):
        return True
    i = 2
    while i ** 2 <= n:
        if(n % i == 0):
            return False
        i += 1
    return True
def primeN(n):
    res = []

    for i in range(1, n+1):
        print('hi')
        print("hi",ifPrime(i))
        if ifPrime(i):
            print (ifPrime(i))
            res.append(i)
    print (res)
primeN(5)
print (ifPrime(0))