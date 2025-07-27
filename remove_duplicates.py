# Bruteforce - You use a set

# Better - Creating a new array Time wise its optimal, Space wise its not

def remove_duplicates(nums):
    arr = [nums[0]]
    for i in range(1,len(nums)):
        if nums[i] != nums[i-1]:
            arr.append(nums[i])             
    return arr
nums = [1,2,2,3,4]
print(remove_duplicates(nums))



# Optimal - Two pointers 

def remove_duplicates_inplace(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return nums[:i+1]
nums = [1,2,2,3,4]
print(remove_duplicates(nums))
