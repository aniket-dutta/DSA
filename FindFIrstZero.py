def bSearchZeroOne(arr, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    
    if arr[mid] == 1 and arr[mid - 1] == 0:
        return mid
    elif arr[mid] == 0:
        return bSearchZeroOne(arr, mid + 1, end)
    else:
        return bSearchZeroOne(arr, start, mid - 1)
    

def zeroOnes(n, arr):
    if arr[0] == 1:
        return 0
    return bSearchZeroOne(arr, 0, n - 1)


nums = []    
# nums = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
n = len(nums)
a = zeroOnes(n, nums)
print(a)

# a = 8
# b = 1
# print( int((a + b) / 2))
# print((a + b) // 2)


