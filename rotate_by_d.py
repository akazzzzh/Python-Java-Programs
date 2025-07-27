def roate(nums,d):
    d = d%len(nums)
    for i in range(d):
        nums.append(nums.pop(i))
    return nums
nums = [1,2,3,4,5]
print(roate(nums,2))


