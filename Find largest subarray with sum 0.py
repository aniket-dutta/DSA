# arr = [ 1,-2,-4,5,-2 ,0,  0, -1, 4, -8, 1]
# arr = [4 ,-3, 1, 2, 1]
# arr = [-3 ,-3 ,-3 ,-2 ,-3 ,-3 ,-3]
# arr = [2, 3, 1, -4, 0, 6]
# arr = [2 ,3 ,1 ,-4 ,0 ,6 ,-1 ,-2 ,24 ,2]
arr = [2]
n = len(arr)
#pick k elements from start or end of array to have  largest sum possible
#we can do by storing psum and ssum
# we can do by storing sum of first k elemnts and then 
# moving the window back arr[-1] and substracting the arr[k] and adding arr[-1]
# we can do by calculating the minimum contigous sum of n - k elemnts and return total sum - minsum
def largestSubarraySumZero(n, arr):
    pSum = 0
    subIndex = [0, 0]
    maxLength = 0
    index = {}
    for i in range(n):
        pSum += arr[i]
        if pSum is 0:
            if maxLength < (i - 0):
                maxLength = i
                subIndex[1] = i
        elif index.get(pSum) is not None:
                # print(index.get(pSum))
                if maxLength < i - index[pSum]:
                    maxLength = i - index[pSum]
                    subIndex[0], subIndex[1] = index[pSum] + 1, i
                    # print("Sub index Update")
                    # print(subIndex)
        else:
            index.update({pSum: i})
    if subIndex[0] is subIndex[1]:
        return [-1]        
    res = arr[subIndex[0]:subIndex[1] + 1]
    if res is None:
        return [-1]
    else:
        return res
        # print(i, arr[i], pSum, index)
                
    print(subIndex)

    

r = largestSubarraySumZero(n, arr)
print (r)
