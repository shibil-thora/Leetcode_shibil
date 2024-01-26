nums = [1,2,2,3,1,4]
frequency = {i:nums.count(i) for i in nums}
print(frequency)

max_fre = max(frequency.values())
sum_val = 0
for i in frequency.values():
    if i == max_fre:
        sum_val = sum_val + max_fre

print(sum_val)