stack = []
minStack = []

def push(x):
    stack.append(x)
    if len(minStack) == 0:
        minStack.append(x)
    elif len(minStack) > 0:
        if x < minStack[-1]:
            minStack.append(x)
        else:
            minStack.append(minStack[-1])
        

def pop():
    if len(stack) >  0 and len(minStack) > 0:
        stack.pop()
        minStack.pop()

def findMin():
    if len(minStack) > 0:
        return minStack[-1]
    else:
        return -1
    
queries = int(input())

for query in range(queries):
    _type = input().strip().split()
    x = 0
    if len(_type) == 2:
        _type, x = map(int, _type)
    else:
        _type = int(_type[0])
    if _type == 1:
        push(x)
    elif _type == 2:
        pop()
    else:
        minElement = findMin()
        print(minElement)
