def bSearch(arr, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    
    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        return bSearch(arr, mid + 1, end)
    else:
        return bSearch(arr, start, mid - 1)
        
    
def fixedPoint(n, A):
    if n == 1 and A[0] == 0:
        return 0
    else:
        return bSearch(A, 0, n - 1)


nums = [-3 ,-1, 2, 4, 5, 6, 7, 8, 9]    
# nums = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
n = len(nums)
a = fixedPoint(n, nums)
print(a)

# a = 8
# b = 1
# print( int((a + b) / 2))
# print((a + b) // 2)


