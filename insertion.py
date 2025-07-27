def sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j>=0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums
nums = [5,7,2,4,1]
sort(nums)
print(nums)
