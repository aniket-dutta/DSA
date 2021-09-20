arr = [ 1,-2,-4,5,-2 ,0,  0, -1, 4, -8, 1]
arr = [4 -3 1 2 1]
k = 4
n = len(arr)


def minimumPrefix(n, nums):
    prefixSum = [0] * n 
    minSum = 0
    for i in range(n):
        prefixSum[i] = prefixSum[i - 1] + nums[i]
        minSum = min(minSum, prefixSum[i])
    print(prefixSum)
    print (abs(minSum))
    return abs(minSum)
        
        
        
        
minimumPrefix(n, arr)
        
    