nums = [9,6,4,2,3,5,7,0,1]
miss = len(nums)
for i in range(0, len(nums)):
    if i not in nums:
        miss = i
        break

print(miss)