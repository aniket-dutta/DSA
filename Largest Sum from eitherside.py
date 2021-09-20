def pickLargestSum(n,K, arr):
    curr_points = 0
    max_points = 0

    for i in range(K):
        curr_points += arr[i]
 
    max_points = curr_points
    j = n - 1
 
    for i in range(K - 1, -1, -1):
        curr_points = (curr_points +
                       arr[j] - arr[i])
        max_points = max(curr_points,
                         max_points)
        j -= 1
    return max_points

 
   
# def pickLargestSum(n, k, arr):
#     if n is 1:
#         return arr[0]
#     if n is k:
#         return sum(arr)
#     if k is 0:
#         return 0
#     i = 0
#     windowSum = sum(arr[i:k])
#     maxSum = windowSum
    
#     # print(maxSum)
#     while i > (-k) :
#         i -= 1
#         lastWindowElement = arr[k + i]
#         windowSum = windowSum - lastWindowElement + arr[i]
#         maxSum = max(maxSum, windowSum)
#         # print ( maxSum, windowSum,lastWindowElement, arr[i])
#     return maxSum


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    result = pickLargestSum(n, k, arr)
    print(result)


if __name__ == "__main__":
    main()
