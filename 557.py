s = "Let's take LeetCode contest"
s.strip()
s_arr = s.split(' ')

for i in range(len(s_arr)):
    s_arr[i] = s_arr[i][::-1]

s_str = ""

for i in s_arr:
    s_str += i + " "

print(s_str)