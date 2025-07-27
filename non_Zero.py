def non_zero(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            j+=1

    return nums
nums = [0,0,1]
print(non_zero(nums))