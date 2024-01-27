s = "ab"
t = "baab"
out_arr = []
for i in t:
    if i in s:
        out_arr.append(i)

out_str = "".join(out_arr)
print(out_arr)
print( s in out_str)
