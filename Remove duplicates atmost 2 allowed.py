def removeDuplicatesFromSortedArrayII(n, a):
    n = len(a)
    uniquePointer = 0
    counter = 0
    i = 0
    while (i < n):
        # print ("i,n,up,c")
        # print(i, n, uniquePointer,counter)
        # print(a)
        # print()
        if counter is 2 and i < n:
            uniquePointer = i
            if a[i] is a[i - 1]:
                while a[i] is a[i - 1] and i < n - 1:
                    i += 1
                if( i == n-1):
                    i += 1
                a[uniquePointer: i] = []
                
            # print(uniquePointer, i)
            
            n = n - ( i - uniquePointer )
            counter = 0
            i = uniquePointer  

        elif i < n - 1 and a[i] is a[i + 1] and counter < 2:
            counter += 1
            i += 1
        elif i < n - 1 and a[i] is not a[i + 1]:
            counter = 0
            i += 1
        else: 
            i += 1    
    return [n, a]


def main():
    n = int(input().strip())
    nums = list(map(int, input().strip().split(' ')))

    length, newNums = removeDuplicatesFromSortedArrayII(n, nums)
    print(length)
    print(*newNums)

if __name__=="__main__":
    main()
