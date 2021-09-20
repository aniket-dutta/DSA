def firstMissingPositive(nums):
    nums = list(set(nums))
    N = len(nums)    
    if N == 0:
        return 1
    if N == 1:
        return 2 if nums[0] == 1 else 1
    #if all values in arr are negative
    flag = False
    m = max(nums)
    mi = min(nums)
    if m < 1:
        return 1 
    # if mi > N:
    #     return 1
    #iterate through the arr for each index

        #now for each index element >0 and <n find its matching index and place 
        #there, this is done by replacing elements at each individual index 
        #keeping the index constant and swapping with a[n] - 1 element 
    for i in range(N):
        while(nums[i] in range(1, N+1) and (nums[i] != nums[nums[i] - 1])):
            temp = nums[i]
            nums[i], nums[temp - 1] = nums[temp - 1], nums[i]
            # print (nums)
    #find which index value mismatches with the index element
    
    for i in range(N):
        #print (nums)
        if nums[i] <= N:
            #print(N, nums[i])
            flag = True
            if nums[i] != nums[nums[i] - 1]:
                return i + 1
    
    #if all indexs matches means no 1 - n are present in the arr with index 1-n
    #meaning now the least minimum positive integer left is n+1
    if flag:
        return N + 1
    else:
        return 1

if __name__ == '__main__':
    n = int(input())
    nums = []
    if n > 0:
        nums = input().split()
        nums = [int(i) for i in nums]

    result = firstMissingPositive(nums)
    print(result)

