# Hello World program in Python
    
def longestValidParentheses(s):
    stack = []
    stack.append(-1)
    
    res = 0
    for i in range(len(s)):
        if s[i] == "(":
            print(s[i])
            stack.append(i)
            print(stack)
        else:
            print(s[i])
            if len(stack) != 0:
                stack.pop()
            if len(stack) != 0:
                print(res, i, stack[-1])
                res = max(res, i - stack[-1])
            else:
                stack.append(i)
            print(stack)
    return res
        
    
    
# s = ")))))))()"
# s = "())((()()))"
res = longestValidParentheses(s)
print(res)