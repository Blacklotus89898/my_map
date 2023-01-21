from random import randint

def my_map (y, x):
    field = []
    for j in range (y):
        my_row = []
        for i  in range (x):
            my_row.append('o')
        field.append(my_row)
    return field
    
def show_map(map1):
    for row in map1:
        print(row)

def my_path(length, my_map, start= [0,0]):
    y,x = start
    my_map[y][x] = "Start"
    last_direction = 2
    direction = 0
    for tiles in range(length): #0123 =>nwse
        direction = randint(0,3)
        while abs(direction-last_direction) == 2: #make x and y 2 random thing check first, then go
            direction = randint(0,3)
            
            
        """while x not in range(0, len(my_map[0])-1) and abs(xdirection-last_xdirection) == 2:
            xdirection = randint(0,3)
            last_xdirection = xdirection"""
        #check surronfing
        direction_list = []
        for i in range (-1, 2, 2):
            for j in range (-1, 2, 2):
                if my_map[x+i][y+j] == "o":
                    direction_list.append(my_map[x+i][y+j])


        if x == len(my_map[0])-1 and y== len(my_map)-1:
            my_map[y][x] = 'End'
            print('You reached the end')

            return my_map
        elif direction == 0 and y!= 0:
            y -= 1
            #if surronded by x then over
            #if map[]
            #check surrond, while not ded => make list of options, random index of list
        elif direction == 2 and y!= len(my_map)-1:
            y += 1
        elif direction == 1 and x!= 0:
            x -= 1
        elif direction == 3 and x!= len(my_map[0])-1:
            x += 1
        
        if my_map[y][x] == "x" or my_map[y][x] == "db" :
            my_map[y][x] = "db"
        else:
            my_map[y][x] = "x"
    return my_map

                




         
c = (my_map(5,4))

show_map(my_path(4,c))