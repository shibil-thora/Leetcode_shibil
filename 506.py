score_dict = {
    1: "Gold Medal",
    2: "Silver Medal",
    3: "Bronze Medal",
}

score = [5,4,3,2,1]
b = score.copy()
b.sort()
b.reverse()
print(b)
full_dict = {b[i]:i+1 for i in range(len(b))}

for i in range(len(score)):
    score[i] = full_dict.get(score[i])

for i in range(len(score)):
    score[i] = score_dict.get(score[i], str(score[i]))

print(score)