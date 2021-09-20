def maxArea(h):
    ans = 0
    n = len(h)
    maxA = 0
    for i in range(n):
        for j in range(i, n):
            l = j - i
            b = min(h[i], h[j])
            maxA = max(maxA, (l * b))
            # print(i,j)
            # print(maxA)
            
    return maxA
    
def calMaxA(maxA, i, j, h):
    l = j - i
    b = min(h[i], h[j])
    return max(maxA, (l * b))
    
def maxAreaTwoPointer(h):
    n = len(h)
    l = 0
    r = n - 1
    maxA = 0
    while l < r:
        # print (l,r)
        print(h[l], h[r])
        print()
        maxA = calMaxA(maxA, l, r, h)
        
        if h[l] < h[r]:
            l += 1
        else:
            r -= 1
    return maxA
        
    
h = [1 ,8 ,6 ,2 ,5 ,4 ,8 ,3 ,7]
b = [3, 1,  1, 38, 4, 1, 3, 5]
m = maxArea(b)
print(maxAreaTwoPointer(b))
print(m)