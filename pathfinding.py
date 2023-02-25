from map import my_map, my_path, show_map
import random


#show_map(my_path(20,m))

def pin(ma, name):
    y =random.randint(0, (len(ma))-1)
    x =random.randint(0,len(ma[y])-1)
    if ma[y][x] == '[ ]':
        ma[y][x] = f'[{name}]'
        return

    print('Same location')


def obstacle(map, size, x,y):
    for j in range(size):
        for i in range(size):
            map[y+j][x+i] = '[X]' 


    return map


def pathfinding1(map):

    """counter = 0
    
    for y in range(len(map)):
        for x in range(len(map[y])):

            if map[y][x] == counter:

                for j in range (-1, 2): #this is a 3 by 3 range
                    for i in range (-1, 2): # TODO: do not use sphere explosion, switch to snowflakes, radial expansion

                        if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                            
                            current = map[y+j][x+i]
                            if current != '[ ]' and current > counter:
                                current = counter
                            else:
                                map[y+j][x+i] = counter
"""

    #############################
    #TODO:nkdnv
    
    #from -counter, counter+1
    #   if in range => put counter if no obstacle, go back to atomic search 
    # // use both radial for no overlap and atomic for obstacle 
    # I^2 + j^2 >= counter^2
    
    x,y = 0,0
    map[y][x] = '[0]'
    counter = 0
    while counter < len(map):
        

        y = -counter
        while y < counter+1:
            x = -counter
            while x < counter+1:
                if x**2 + y**2 >= counter**2:
                    
                    for j in range (-1, 2): #this is a 3 by 3 range
                        for i in range (-1, 2):

                            if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                                
                                
                                current = map[y+j][x+i]
                                
                                if current == '[ ]':
                                    map[y+j][x+i] = f'[{counter+1}]'

                                if current != '[ ]':
                                    if current.strip('[]') == int:

                                        if int(current.strip('[]')) == counter-1:
                                            pass##correction
                                #else:
                                #    current = f'[{counter}]'

                x+=1
            y+=1

        counter +=1

    return map



def pathfinding2(map):
    x,y = 0,0
    map[y][x] = '[0]'
    counter = 0
    while counter < len(map):
        

        y = -counter
        while y < counter+1:
            x = -counter
            while x < counter+1:
                if x**2 + y**2 >= counter**2:
                    
                    for j in range (-1, 2): #this is a 3 by 3 range
                        for i in range (-1, 2):

                            if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                                if (abs(y+j))**2 + (abs(x+i))**2 >= (counter+1)**2:    
                                    current = map[y][x]
                                    
                                
                                
                                #if current == '[ ]':
                                   # value = current.strip('[]')
                                  #  map[x,y] = '[0]'
                                 #   map[y+j][x+i] = f'[{counter+1}]'

                                    if current != '[ ]' and current !='[X]':
                                        
                                        value = int(current.strip('[]'))
                                        
                                        if map[y+j][x+i] == '[ ]':
                                            map[y+j][x+i] = f'[{value+1}]'

                                        if map[y+j][x+i] != '[ ]' and map[y+j][x+i] !='[X]':
                                            if int(map[y+j][x+i].strip('[]')) >= value+1:
                                                map[y+j][x+i] = f'[{value+1}]'

                                            
                                            

                                        

                                        #if int(current.strip('[]')) == counter-1:
                                         #   pass##correction
                                #else:
                                #    current = f'[{counter}]'

                x+=1
            y+=1

        counter +=1

    return map
    


def pathfinding3(map):
    x,y = 0,0
    map[y][x] = '[0]'
    counter = 0
    cross_mvt_list = [[0,1],[0,-1],[1,0], [-1,0]] 
    while (counter < len(map) and counter <len(map[0])):
        

        y = -counter
        while y < counter+1:
            x = -counter
            while x < counter+1:
                if x**2 + y**2 >= counter**2:
                    
                    for j in range (-1, 2): #this is a 3 by 3 range
                        for i in range (-1, 2):
                            
                            if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                                if [j,i] in cross_mvt_list: # delete for diagonal mvt
                                   
                                    current = map[y][x]

                                    if current != '[ ]' and current !='[X]':
                                        
                                        value = int(current.strip('[]'))
                                        
                                        if map[y+j][x+i] == '[ ]':
                                            map[y+j][x+i] = f'[{value+1}]'

                                        if map[y+j][x+i] != '[ ]' and map[y+j][x+i] !='[X]':
                                            if int(map[y+j][x+i].strip('[]')) >= value+1:
                                                map[y+j][x+i] = f'[{value+1}]'

                x+=1
            y+=1

        counter +=1

    return map

def pathfinding4(map):
    x,y = 0,0
    map[y][x] = '[0]'
    counter = 0
    cross_mvt_list = [[0,1],[0,-1],[1,0], [-1,0]] 
    while (counter < len(map) and counter <len(map[0])):
        

        y = -counter
        while y < counter+1:
            x = -counter
            while x < counter+1:
                if x**2 + y**2 >= counter**2:
                    
                    for j in range (-1, 2): #this is a 3 by 3 range
                        for i in range (-1, 2):
                            
                            if (y+j)in range(len(map)) and (x+i) in range(len(map[0])): 
                                #if [j,i] in cross_mvt_list: # delete for diagonal mvt
                                
                                current = map[y][x]

                                if current != '[ ]' and current !='[X]':
                                    
                                    value = int(current.strip('[]'))
                                    
                                    if map[y+j][x+i] == '[ ]':
                                        map[y+j][x+i] = f'[{value+1}]'

                                    if map[y+j][x+i] != '[ ]' and map[y+j][x+i] !='[X]':
                                        if int(map[y+j][x+i].strip('[]')) >= value+1:
                                            map[y+j][x+i] = f'[{value+1}]'

                x+=1
            y+=1

        counter +=1

    return map




m = my_map(6,6)
m1 = my_map(6,6)
m2 = my_map(6,6)

mx = obstacle(m, 2, 1, 3 )
mx = obstacle(mx, 2, 2, 1 )

#mo = obstacle(m, 2, 2, 1)
mo1 = obstacle(m1, 2, 1, 3 )
mo1 = obstacle(mo1, 2, 2, 1 )

mo2= obstacle(m2, 2, 1, 3)
mo2= obstacle(mo2, 2, 2, 1)
#mo= obstacle(m, 1, 1, 2)
#m3= obstacle(m1, 1, 1, 2)
p1 = pathfinding3(mo1)
p2 = pathfinding4(mo2)

show_map(mx)
print('\n')
show_map(p1)
print('\n')
show_map(p2)