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
    my_map[y][x] = "On"
    #last_direction = 2
    #direction = 0
    for tiles in range(length): #0123 =>nwse or can used while not at the end
       
            
            
        """while x not in range(0, len(my_map[0])-1) and abs(xdirection-last_xdirection) == 2:
            xdirection = randint(0,3)
            last_xdirection = xdirection"""
        #check surronfing
        position_list = []
        direction_list = []
        cross_mvt_list = [[0,1],[0,-1],[1,0], [-1,0]] 
        for j in range (-1, 2):
            
            for i in range (-1, 2):

                if (y+j)in range(len(my_map)) and (x+i) in range(len(my_map[0])) and my_map[y+j][x+i] == "o" :
                    if [j,i] in cross_mvt_list:
                        direction_list.append([j, i])
                    
                        position_list.append([y+j,x+i]) # diago mvt included
                    # use filter to get in 

        if len(position_list) == 0:
            my_map[y][x] = 'Death'
            break    

        #print(direction_list)
        position = position_list[randint(0,len(position_list)-1)]
        y,x = position
        #path position list
        #print('position y,x is', direction)

        if x == len(my_map[0])-1 and y == len(my_map)-1:
            my_map[y][x] = 'End'
            print('You reached the end')
            print(f"Using {tiles} tiles")

            return my_map
        #elif direction == 0 and y!= 0:
            y -= 1
            #if surronded by x then over
            #if map[]
            #check surrond, while not ded => make list of options, random index of list
        #elif direction == 2 and y!= len(my_map)-1:
            y += 1
        #elif direction == 1 and x!= 0:
            x -= 1
        #elif direction == 3 and x!= len(my_map[0])-1:
            x += 1
        
        #if my_map[y][x] == "x" or my_map[y][x] == "db" :
            my_map[y][x] = "db"
        else:
            my_map[y][x] = tiles

    return my_map

                
#def position_finder(map):-
#list of path, for element not in path, if next to a path or if 
# movement in staight line: cross_mvt_list = [[0,1],[0,-1],[1,0], [-1,0]] 
# if cross then 
    """coner, best location
    create no loop back"""

#chess game
    #diagonal
    




         
c = (my_map(7,7))

show_map(my_path(14,c))