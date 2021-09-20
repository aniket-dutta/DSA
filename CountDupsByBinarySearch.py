def countLeftRight(arr, index):
    count = 1
    i = index
    while i > 0 and arr[i - 1] is arr[i]:
        count += 1
        i -= 1
    i = index
    while i < len(arr) - 1 and arr[i + 1] is arr[i]:
        count += 1
        i += 1
    # print(count)
    return count
# arr = [1,2,3,4,5,5,5,5,5,5,7,6]
# countLeftRight(arr, 9)

def bSearch(arr, start, end, k):
    if start > end:
        return -1
    mid = (start + end) // 2
    
    if arr[mid] == k:
        return mid
    elif arr[mid] < k:
        return bSearch(arr, mid + 1, end, k)
    else:
        return bSearch(arr, start, mid - 1, k)
        
def countFirstOccurence(arr, start, end, k):
    if start > end:
        return -1
    mid = (start + end) // 2
    
    if (arr[mid] == k and mid == 0) or (arr[mid] == k and arr[mid - 1] != k):
        return mid
    elif arr[mid] < k:
        return countFirstOccurence(arr, mid + 1, end, k)
    else:
        return countFirstOccurence(arr, start, mid - 1, k)
    
def countLastOccurence(arr, start, end, k):
    if start > end:
        return -1
    mid = (start + end) // 2
    
    if (arr[mid] == k and mid == end) or (arr[mid] == k and arr[mid + 1] != k):
        return mid
    elif arr[mid] <= k:
        return countLastOccurence(arr, mid + 1, end, k)
    else:
        return countLastOccurence(arr, start, mid - 1, k)
    
def countOccurrences(n, arr, k):
    index = -1
    i,j = 0,0
    if n == 1 and arr[0] == k: 
        return 1 
    else:
        # index = bSearch(arr, 0, n - 1, k)
        i = countFirstOccurence(arr, 0, n - 1, k)
        j = countLastOccurence(arr, 0, n - 1, k)
        if i <0 or j < 0:
            return 0
        print(i,j)
        return j - i + 1

nums = [1 ,2, 2] #,3,4,5,5,5,5,5,5,6,6]
# nums = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1]
n = len(nums)
a = countOccurrences(n, nums, 3)
print(a)

# a = 8
# b = 1
# print( int((a + b) / 2))
# print((a + b) // 2)


