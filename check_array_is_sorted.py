def array_sorted(nums):
    for i in range(len(nums)):
        if nums[i+1]<nums[i]:
            return False
    return True
nums = [1,2,3,4,2]
print(array_sorted(nums))