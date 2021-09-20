def firstUniqueInteger(lis):
    index = dict.fromkeys(lis, 0)
    for x in lis:
        index[x] += 1
    for x in index:
        if index[x] == 1:
            return x
    return -1
    
s = [7, 6, 1, 6, 1]

s = firstUniqueInteger(s)
print(s)