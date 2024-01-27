nums = [4,3,2,7,8,2,3,1]
n = len(nums)
output = []

nums.sort()
nums = set(nums)
full_set = set(range(1, n + 1))

print(list(full_set - nums))