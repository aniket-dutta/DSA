# Hello World program in Python
nums = [1,0,4,2,0,7,0,3,4,0,9,5]

def countZero(n):
    if n is not 0:
        return True
    else:
        return False
def moveZeroes(nums):
    ans = list(filter(countZero, nums))
    ans += [0] * (len(nums) - len(ans))
    return ans
    
def moveZ(nums):
    i = 0
    j = 0
    
    while i < len(nums):
        if nums[i] is not 0:
            nums[j] = nums[i]
            print(j,i, nums)
            j += 1
        i += 1
            
            

# ans = moveZeroes(nums)
ans = moveZ(nums)
print(ans)