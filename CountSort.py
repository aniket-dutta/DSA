def countSort(n, s):
    res = [''] * n
    cArr = [0] * 256
    
    for x in s:
        cArr[ord(x)] += 1
        
    for i in range (256):
        cArr[i] += cArr[i - 1]
    print (cArr[ord('a'):ord('k')])
    
    for i in range(n):
        res[cArr[ord(s[i])] - 1] = s[i]
        cArr[ord(s[i])] -= 1
        print(res)
    return ''.join(res)
    
    
# arr = [6 , -10, 3, 2, 0 ,1, 7 ]
# arr.sort(reverse=True)
# print(arr)
arr =  list('aabbccddee')
a = [6 ,-10, 3, 2, -32]
n = len(arr)
res = countSort(n, arr)

print(res)