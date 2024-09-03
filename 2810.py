
output = []
for i in s:
    if i == 'i':
        output.reverse()
    else:
        output.append(i)
output = "".join(output)
print(output)