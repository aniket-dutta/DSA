# s = 'abcddddddadd'
# s = 'Xyyzya'
# s = 'aaaaaaaaabcd'

# s = 'crio.do'
s = 'abacd'
n = len(s)
k = 3
# k is greatest no of distinct characters allowed




def length_of_substring(s, k):
    n = len(s)
    res = 0
    ck = 0
    res = 0
    for i in range(n):
        #to store for all chars and symbols
        visited = [0] * 500 
        for j in range(i, n):
            if visited[ord(s[j])] == 0 and ck < k:
                visited[ord(s[j])] += 1
                ck += 1
                res = max(res, j - i + 1)
                print(s[j], i, j, ck, res)
            elif visited[ord(s[j])] > 0 and ck <= k:
                res = max(res, j - i + 1)
                print(s[j], i, j, ck, res)
            else:
                break
                
        print("c i j ck res")
        print('ck = 0 now')
        print()
        ck = 0
                
       
    return res
    
# def 
    
    
a = length_of_substring(s, k)
print(a)

--------------------------------------------BY 2 pointers---------------------------------------------------------------------------------------------------------

def length_of_substring(s, k):
    n = len(s)
    res = 0
    ck = 0
    j = 0
    i = 0
    visited = [0] * 500 
    print("x i j ck res")
    while i < n and j < n:
        # print(s[j])
        
        
        
        # print(s[j], visited[ord(s[j])], ck)
        
        
        if visited[ord(s[j])] == 0 and ck < k:
            visited[ord(s[j])] += 1
            ck += 1
            res = max(res, j - i + 1)
            print(s[j], i, j, ck, res)
            j += 1
           
        elif visited[ord(s[j])] > 0 and ck <= k:
            res = max(res, j - i + 1)
            print(s[j], i, j, ck, res)
            j += 1
        else:
            visited = [0] * 500 
            i += 1
            j = i 
            ck = 0
            print('ck = 0 now')
            print()
            # print(s[j], i, j, ck, res)
            break
            
        
        
                
       
    return res