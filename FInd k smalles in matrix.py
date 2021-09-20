mat = [
        [1, 5, 9],
        [10, 11, 14],
        [12, 13, 15]
    ]

def getPositionInSortedArray2(guess, mat):
    pos = 0 
    n = len(mat)
    # starting pos = 0
    for i in range(n):
        if guess < mat[i][0]:
            return pos
        #if number is less than first ele of each row
        if guess > mat[i][n - 1]:
            pos += n
            continue
        j = 0
        while j < n:
            if mat[i][j] <= guess:
                pos += 1
                print(mat[i][j], pos, i)
            j += 1
    return pos 


def getPositionInSortedArray(guess, mat):
    pos = 0 
    n = len(mat)
    # starting pos = 0
    for i in range(n):
        if guess < mat[i][0]:
            return pos
        #if number is less than first ele of each row
        if guess > mat[i][n - 1]:
            pos += n
            # print("pos update")
            # print(pos, i)
            continue
        #if num > lat ele of the row, add the row's count
        sortedElements = 0
        j = n // 2
        while j >= 1:
            # print(j, n, i, mat[i][sortedElements + j], guess)
            while sortedElements + j < n and mat[i][sortedElements + j] <= guess:
                sortedElements += j
            j /= 2

        pos += sortedElements + 1
    
    return pos
p = getPositionInSortedArray2(12, mat)
print(p)            
# p = getPositionInSortedArray(12, mat)
# print(p)        

def kthSmallestElementInMatrix(matrix, k):
    n = len(matrix)
    start = matrix[0][0]
    end = matrix[n - 1][n - 1]
    while start <= end:
        mid = (start + end) // 2
        print(start, end, mid)
        sortedPosition = getPositionInSortedArray2(mid, matrix)
        print(sortedPosition)
        if sortedPosition >= k:
            end = mid - 1
        else:
            start = mid + 1
        print(start, end)
    return start
    
    
    
# ans = kthSmallestElementInMatrix(mat, 8)
# print(ans)





