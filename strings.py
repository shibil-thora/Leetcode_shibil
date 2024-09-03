s = "anagram"
t = "nagaram" 

my_dict = {} 
for i in s: 
    my_dict[i] = True 

for i in t: 
    if i in my_dict: 
        del my_dict[i] 

print(my_dict)

     

