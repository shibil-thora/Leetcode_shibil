s = "abab"
point = False
for i in range(len(s)):
    if s[i] == 'b':
        point = i
        break

print( 'a' not in s[point:] )
