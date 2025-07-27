# Brute force - Sorting

# Better soln - Two passes
# def second_largest(nums):
#     largest = nums[0]
#     for i in range(1,len(nums)):
#         if nums[i]>largest:
#             largest = nums[i]
#     second_largest1 = -1
#     for i in range(len(nums)):
#         if nums[i] > second_largest1 and nums[i]!=largest:
#             second_largest1 = nums[i]
#     return second_largest1
# nums = [3,2,1,5,2]
# print(second_largest(nums))

# Optimal
def second_largest(nums):
    largest = nums[0]
    ssecondlargest = -1
    for i in range(1,len(nums)):
        if nums[i]>largest:
            ssecondlargest = largest
            largest = nums[i]
    return ssecondlargest
nums = [3,2,1,5,2]
print(second_largest(nums))
    


