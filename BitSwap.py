def swap_all_odd_and_even_bits(n):
    res = ''
    for i in range(32, 0, -2):
        #calculate each bit from left to right
        # n & 1000...(32-1) times, if and is > 0 means 
        # both bits were 1, ie bit is 1
        a = 1 if n & (1 << i - 1) else 0
        b = 1 if n & (1 << i - 2) else 0
        # print (a,b)
        # if a and b are different, swap them
        if a ^ b is not 0: 
            res +=  str(b) + str(a)
        else:
            res += str(a) + str(b)
            
    return int(res,2)
            
            
            
            
        
a = swap_all_odd_and_even_bits(22)
print(a)