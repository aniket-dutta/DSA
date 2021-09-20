def nextLargerElement(arr):
    stack = [] #stack to find nge
    n = len(arr)
    stack.append(0) #push first ele in array
    ans = [0] * n #final result
    for i in range (1,n):
        #assume nge as next element 
        nextGE = arr[i]  
        # find top of stack, ie previous element/s
        top = arr[stack[-1]]
        # if the current nge is greater than prevouis elements
        # then its nge for all elements in stack that are less 
        # than the current nge element, so pop out all those 
        # elements present in stack
        if nextGE > top:
            while len(stack) > 0 and arr[stack[-1]] < nextGE :
                ans[stack[-1]] = nextGE
                print(arr[stack[-1]] , nextGE, i, ans)
                stack.pop()
                print(stack)
                
            stack.append(i)
            
        # if the current nge is not greater than the top of
        # stack, add it to the stack and move to next element
        else:
            stack.append(i)
            # print(stack[-1], nextGE, i, res)
        print(stack)
    for i in range(len(ans)):
        if ans[i] == 0:
            ans[i] = -1
    
    return ans
s = [1, 3, 2, 4]
res = nextLargerElement(s)
print(res)