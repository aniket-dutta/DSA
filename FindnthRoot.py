import math
def powX(x, n):
    # print(x, n)
    
    if (n == 0): return 1
    if (n == 1): return x
    a = powX(x, n // 2); 
    #recursive function to calclate great powers
    # print(x, n, a)
    if a > int(1e10):
    # to handle out of memory cases we return high power of x as 1e10
        return int(1e10)
    if (int(n) & 1) == 1.0:
        return x * a * a;
    else:
        return a * a;
    

def findRoot(start, end, x, n):
    i = 0
    # print("g", "s", "e", "gp")
    while start <= end:
        guess = (start + end) // 2
        gp = powX(guess, n)
        # print(guess, start, end, gp)
        if gp == x:
            return guess
        elif gp > x:
            #if ans is going beyond x reduce to left subarray
            end = guess - 1
        else:
            #else search in right sub array
            start = guess + 1
        i += 1
    # res = round(guess, 6)
    return end
    # return math.floor(res)
    
def nthRoot(x, n):
    start = 1
    end = x 

    return findRoot(start, end, x, n)
    
a = nthRoot(16, 4)
# a = powX(5000, 9502)
print(a)