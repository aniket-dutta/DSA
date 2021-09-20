def bitRep(n):
    count = 0
    for i in range(64, 0, -1):
        # print(n & (1 << i - 1))
        # print  ( (1 if (n & (1 << i - 1)) > 0 else 0), end = '')
        if (n & (1 << i - 1)) > 0:
            count += 1
            
            print('1',end = '')
        else:
            print('0',end = '')
    print ()
    print ( count )
    
# def countSetBits( n ):
    # count = 0
    # while n:
    #     count += 1
    #     n &= (n-1)
        
    #     print(n &= (n-1))
    # print(count)

a = 1000000000000000000
b = 0

c = a & b
d = a ^ b

# bitRep(a)
# bitRep(b)
print()
# bitRep(c)
bitRep(d)
# countSetBits(d)
