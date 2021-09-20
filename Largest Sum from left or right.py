# arr = [ 1,-2,-4,5,-2 ,0,  0, -1, 4, -8, 1]
# arr = [4 ,-3, 1, 2, 1]
arr = [-3 ,-3 ,-3 ,-2 ,-3 ,-3 ,-3]
k = 3
n = len(arr)
#pick k elements from start or end of array to have  largest sum possible
#we can do by storing psum and ssum
# we can do by storing sum of first k elemnts and then 
# moving the window back arr[-1] and substracting the arr[k] and adding arr[-1]
# we can do by calculating the minimum contigous sum of n - k elemnts and return total sum - minsum

def pickLargestSum(n, k, arr):
    if n is 1:
        return arr[0]
    if n is k:
        return sum(arr)
    i = 0
    windowSum = sum(arr[i:k])
    maxSum = windowSum
    
    # print(maxSum)
    while i > (-k) :
        i -= 1
        lastWindowElement = arr[k + i]
        windowSum = windowSum - lastWindowElement + arr[i]
        maxSum = max(maxSum, windowSum)
        print ( maxSum, windowSum,lastWindowElement, arr[i], i)
    return maxSum
        
    
    
    
    
    
    
    
    
r = pickLargestSum(n, k, arr)
print (r)
