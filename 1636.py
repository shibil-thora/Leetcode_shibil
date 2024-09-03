def countPairs(nums, target):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,(len(nums))):
            if 0 < i and i < j and j < len(nums) and (nums[i] + nums[j] <= target):
                print(nums[i], nums[j])
                count += 1
    return count

    
print(countPairs([-1,1,2,3,1], 2))