from random import randint

def my_map (y, x):
    field = []
    for j in range (y):
        my_row = []
        for i  in range (x):
            my_row.append('[ ]')
        field.append(my_row)
    return field
    
def show_map(map1):
    for row in map1:
        print (*row, sep="")

def my_path(length, my_map, start= [0,0]):
    y,x = start
    my_map[y][x] = "[S]"
    #last_direction = 2
    #direction = 0
    tracker = []
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

                if (y+j)in range(len(my_map)) and (x+i) in range(len(my_map[0])) and my_map[y+j][x+i] == '[ ]' :
                    if [j,i] in cross_mvt_list: # this limits the direction to cross direcrtion
                        if tiles >= 2:
                            if [j,i] != tracker[tiles-2]:
                                direction_list.append([j, i]) #direction 
                    
                                position_list.append([y+j,x+i])

                        else:
                            direction_list.append([j, i]) #direction 
                    
                            position_list.append([y+j,x+i]) # this is the position available
                    

        if len(position_list) == 0:# there are no direction possible => dead end
            my_map[y][x] = '[D]' 
            break    

        #print(direction_list)
        index = randint(0,len(position_list)-1)
        position = position_list[index]
        tracker.append([ -x for x in direction_list[index] ])
        #print(tracker) #tracking the position use the previous 2
        y,x = position
        #path position list
        #print('position y,x is', direction)

        if x == len(my_map[0])-1 and y == len(my_map)-1:
            my_map[y][x] = '[W]'
            print('You reached the end')
            print(f"Using {tiles+1} tiles")

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
            my_map[y][x] = '[+]'

    return my_map

def spot_finder(map):
    
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '[+]': #check adjacent case
                
                for j in range (-1, 2): #this is a 3 by 3 range
            
                    for i in range (-1, 2):

                        if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                            if map[y+j][x+i] not in '[+], [D], [S], [W]':
                                counter = map[y+j][x+i].strip("[]")
          
                      
                                if counter == ' ':
                                    counter = 0 
                 
                                counter = int(counter)
                                counter+=1
                                map[y+j][x+i] = f'[{counter}]' #higher value means greater priority
                    
    return map

def spot_finder2(map):
    
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] not in '[+], [D], [S], [W]' : #check adjacent case
                counter = map[y][x].strip("[]")
                if counter == ' ':
                    counter = 0
                counter = int(counter)
                
                j = -2
                while j <3:
                    
                    

                #for j in range (-2, 3): #this is a 5*5 radius effect
                
                    i = -2
                    while i<3:
                    #for i in range (-2, 3):

                        if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                            if map[y+j][x+i] == "[+]":#or "[D]" or '[S]' or '[W]'):
                                #counter = map[y+j][x+i].strip("[]")
          
                                #counter = counter
                                #if counter == ' ':
                                 #   counter = 0 
                                
                                
                                counter += 1
                            else: 
                                counter = counter
                        i+=1
                    j+=1
                map[y][x] = f'[{counter}]'
                counter = 0 #higher value means greater priority
                    
    return map       
#def position_finder(map):-
#list of path, for element not in path, if next to a path or if 
# movement in staight line: cross_mvt_list = [[0,1],[0,-1],[1,0], [-1,0]] 
# if cross then 
    """coner, best location
    create no loop back"""

#chess game
    #diagonal
    
#pathfinding

         
c = (my_map(7,7))

d = (my_path(30,c))
show_map(d)

print('Corners:3x3')

e = spot_finder(d)
show_map(e)

print('5x5')
show_map(spot_finder2(d))