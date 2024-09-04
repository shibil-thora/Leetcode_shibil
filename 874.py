commands = [-2,-1,8,9,6]
obstacles = [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]

direction_right = -1 
direction_left = -2  

starting_point = {'x': 0, 'y': 0} 

right_of = {
    'N': 'E', 
    'E': 'S',
    'W': 'N', 
    'S': 'W',
}  

left_of = {
    'N': 'W', 
    'E': 'N',
    'W': 'S', 
    'S': 'E',
}


direction = 'N'
max_distance = -1000

for i in commands:  
    obstacles_detected = [False, []]
    print(f'location is {(starting_point["x"], starting_point["y"])}, current direction is {direction} , i: {i}')
    if i == direction_right:
        print(f'direction changed from {direction} to {right_of[direction]}') 
        direction = right_of[direction]
        
    elif i == direction_left: 
        print(f'direction changed from {direction} to {left_of[direction]}')
        direction = left_of[direction] 
        
    else: 
        if direction == 'N':  
            for p in range(i): 
                starting_point['y'] += 1 
                if [starting_point['x'], starting_point['y']] in obstacles: 
                    obstacles_detected[0] = True
                    obstacles_detected[1] = [starting_point['x'], starting_point['y']]

        elif direction == 'E': 
            for p in range(i):
                starting_point['x'] += 1
                if [starting_point['x'], starting_point['y']] in obstacles: 
                    obstacles_detected[0] = True
                    obstacles_detected[1] = [starting_point['x'], starting_point['y']]

        elif direction == 'W': 
            for p in range(i):
                starting_point['x'] -= 1
                if [starting_point['x'], starting_point['y']] in obstacles: 
                    obstacles_detected[0] = True
                    obstacles_detected[1] = [starting_point['x'], starting_point['y']]
        else: 
            for p in range(i):
                starting_point['y'] -= 1 
                if [starting_point['x'], starting_point['y']] in obstacles: 
                    obstacles_detected[0] = True 
                    obstacles_detected[1] = [starting_point['x'], starting_point['y']]

        if obstacles_detected[0]: 
            print('###################### -Detected- ######################', obstacles_detected[1]) 
            if starting_point['x'] == obstacles_detected[1][0]: 
                print(starting_point, obstacles_detected[1], 'x equal')
                starting_point['y'] -= (obstacles_detected[1][1] + 1)
                 
        
            if starting_point['y'] == obstacles_detected[1][1]: 
                print(starting_point, obstacles_detected[1], 'y equal')
                starting_point['x'] -= (obstacles_detected[1][0] + 1)
                
                 
        
        print(f'location changed to {(starting_point["x"], starting_point["y"])}') 
        euclidian_distance = (starting_point['x'] * starting_point['x'] + 
                                starting_point['y'] * starting_point['y'])
        
        if euclidian_distance > max_distance: 
            max_distance = euclidian_distance 

print(max_distance, '<-- Output')
 
    