def firstMissingPositive(nums):
    m = max(nums)
    N = len(nums)
    # print (N)
    #if all values in arr are negative
    if m < 1:
        return 1 
    if N == 1:
        return 2 if nums[0] == 1 else 1
    l = [0] * m

    for i in range (N):
        if nums[i] > 0 and l[nums[i] - 1] != 1:
            l[nums[i] - 1] = 1
    
    for i in range (N):
        if l[i] == 0:
            return i + 1

    return i + 2

if __name__ == '__main__':
    n = int(input())
    nums = []
    if n > 0:
        nums = input().split()
        nums = [int(i) for i in nums]

    result = firstMissingPositive(nums)
    print(result)

