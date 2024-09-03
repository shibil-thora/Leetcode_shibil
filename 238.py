nums = [1, 2, 3, 4]
output = []
for i in nums:
    temp = []
    mul = 1
    for j in temp:
        if not i == j: 
            mul = mul * i
    output.append(mul)

print(output)