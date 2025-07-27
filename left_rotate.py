# Not Optimized
# def left_rotate(nums):
#     return nums[1:] + [nums[0]]
# nums = [1,2,3,4,5]
# print(left_rotate(nums))

#Optimized

# def left_rotate(nums):
#     first = nums[0]
#     for i in range(1,len(nums)):
#         nums[i-1] = nums[i]
#     nums[-1] = first 
#     return nums
# nums = [1,2,3,4,5]
# print(left_rotate(nums))

# Right rotate by 1
def right_rotate(nums):
    last = nums[-1]
    for i in range(len(nums)-2,-1,-1):
        nums[i+1] = nums[i]
    nums[0] = last
    return nums
nums = [1,2,3,4,5]
print(right_rotate(nums))