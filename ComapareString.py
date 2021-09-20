def backspaceStringCompare(s1, s2):
    stack1 = []
    stack2 = []
    
    for x in s1:
        if x is '#':
            if len(stack1) > 0:
                stack1.pop()
        else:
            stack1.append(x)
            
    
    for x in s2:
        if x is '#':
            if len(stack2) > 0:
                stack2.pop()
        else:
            stack2.append(x)
            
    finals1 = "".join(stack1)
    finals2 = "".join(stack2)
    # print(finals1, finals2)
    return finals1 == finals2
    
    
    
    
s1 = "a###as#sddff#"
s2 = "aa#sddf"

res = backspaceStringCompare(s1, s2)
print(res)