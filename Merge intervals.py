inter = [[6, 10], [1, 2], [2, 4], [9, 10], [10, 200]]
inter.sort()
print(inter)
n = len(inter)

# for i in range(n):
#     for j in range(n):
#         if i == j:
#             continue
#         if inter[i][0] < inter[j][1] and inter[i][1]>= inter[j][0]:
#             print ("merged array")
#             if inter[j][0] > inter[i][0]:
#                 inter[j][0] = inter[i][0]
#             if inter[j][1] < inter[i][1]:
#                 inter[j][1] = inter[i][1]
           
#             # res.append([inter[i][0], inter[j][1]])
#             print(inter)
            
        
        
i = 0
j = 1
res = []
res.append(inter[0])
print(res)



def checkMerge(first, second):
    if first[1] >= second[0]:
        i = min(first[0], second[0])
        j = max(first[1], second[1])
        return ([i, j])
    else:
        return None
        
for i in range(1, n):
    stackTop = res[len(res) - 1]
    check = checkMerge(stackTop, inter[i])
    if check is not None:
        res.pop()
        res.append(check)
    else: 
        res.append(inter[i])
        
print(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
      


