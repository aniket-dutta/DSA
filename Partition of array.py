arr = [1,2,4,5,2 ,0,  0, 1, 4, 8, 1]
n = len(arr)
def equalPartition(n, arr):
    prefixSum = [0] * n
    suffixSum = [0] * n
    suffixSum[n - 1] = arr[n - 1]
    prefixSum[0] = arr[0]
    i = 0
    
    for i in range(1, n):
        prefixSum[i] = prefixSum[i - 1] + arr[i]
    print(prefixSum)
    
    for i in range(n - 2, -1, -1):
        suffixSum[i] = suffixSum[i + 1] + arr[i]
        
    print(suffixSum)
    
    for i in range(1, n-1):
        if prefixSum[i] == suffixSum[i]:
            print(arr[i])
            return arr[i]
            
    return -1
    
def equalPartition2(size, arr):

	right_sum, left_sum = 0, 0

	# Computing right_sum
	for i in range(1, size) :
		right_sum += arr[i]

	i, j = 0, 1

	# Checking the point of partition
	# i.e. left_Sum == right_sum
	while j < size :
	    print(right_sum , arr[j], left_sum)
		right_sum -= arr[j] 
		
		left_sum += arr[i]
		print(right_sum , arr[j], left_sum)
		print()

		if left_sum == right_sum :
			return arr[i + 1]

		j += 1
		i += 1

     
     
     
equalPartition2(n, arr)   
        
    