# Hello World program in Python
    
def removeAdjacentDuplicates(s):
    stack = []
    for i in range (len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        elif stack[-1] == s[i]:
            stack.pop()
        else: stack.append(s[i])
        
    res = "".join(stack)
    print(res)
    return res
        
    
    
s = "abbaca"
res = removeAdjacentDuplicates(s)
print(res)