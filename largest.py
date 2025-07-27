# Brute Force - Sorting then finding out the largest element


# Optimal soln
def largest(nums):
    largest = nums[0]
    for i in range(1,len(nums)):
        if nums[i]>largest:
            largest = nums[i]
    return largest
nums = [3,2,1,5,2]
print(largest(nums))

