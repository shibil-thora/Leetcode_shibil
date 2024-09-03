def getLucky(s, k): 
    alph = {
        'a': 1, 
        'b': 2, 
        'c': 3, 
        'd': 4, 
        'e': 5, 
        'f': 6, 
        'g': 7, 
        'h': 8, 
        'i': 9, 
        'j': 10, 
        'k': 11, 
        'l': 12, 
        'm': 13, 
        'n': 14, 
        'o': 15, 
        'p': 16, 
        'q': 17, 
        'r': 18, 
        's': 19, 
        't': 20, 
        'u': 21, 
        'v': 22, 
        'w': 23, 
        'x': 24, 
        'y': 25, 
        'z': 26
    } 
    conversion = [str(alph[i]) for i in s] 
    num = ''.join(conversion)

    while k > 0: 
        sum_of_num = 0 
        for n in num: 
            sum_of_num += int(n) 
        num = str(sum_of_num)  
        k -= 1
    
    return int(num)

s = "iiii" 
k = 1

print(getLucky(s, k), '----------------output---------------')