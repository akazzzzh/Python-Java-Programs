# ptimal soln
def ssmallest(nums):
    smallest = nums[0]
    ssmallest1 = 10*9
    for i in range(1,len(nums)):
        if nums[i]<smallest:
            ssmallest1 = smallest
            smallest = nums[i]
    return ssmallest1
nums = [3,2,1,5,2]
print(ssmallest(nums))