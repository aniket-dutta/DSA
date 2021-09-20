def subSort(arr):
    i = 0
    
    n = len(arr)
    j = n - 1
    s = -1
    e = -1
    
    while i < j:
        if arr[i + 1] < arr[i]:
            s = i
            
        if arr[j - 1] > arr[j]:
            e = j
    
        i += 1
        j -= 1
    if s < 0 and e < 0:
        #array is sorted
        return [s, e]
        
        
    minOfSub = min(arr[s:e + 1])
    maxOfSub = max(arr[s:e + 1])
    
    i = 0
    j = n - 1
    while i < s and j > e:
        if arr[i] >= minOfSub:
            s = i
        if arr[j] <= maxOfSub:
            e = j
        i += 1
        j -= 1

    
    print(s, e)
    
    return [s, e]
    
    
# a = [ 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
a = [1,2,3,4,5,6,7,8,9]
ans = subSort(a)
print(ans)