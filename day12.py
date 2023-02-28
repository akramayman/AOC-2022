from collections import deque

with open("day12.txt", "rt") as Advent12:
    Advent12 = Advent12.read()
Advent12 = Advent12.strip().split('\n')
full_list = []
for items in Advent12:
    full_list.append(list(items))  # create list of list as matrix for all text character


def position_of_start_end(full_list,Start):
    hight = len(full_list)
    width = len(full_list[0])
    neighbore = deque()

    for i in range(hight):
        for j in range(width):
            if full_list[i][j] == Start:  #retrieve the position of start
                start_position = (i, j, 0)# x y and weight
                neighbore.append(start_position) #add it directlly to Qeue

    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = set() #to save the unique value of visited node

    while neighbore:
        x, y, weg = neighbore.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        if full_list[x][y] == "E":
            return weg

        for i, j in direction:
            new_x, new_y = x + i, y + j
            if 0 <=new_x<hight and 0 <=new_y<width and 1-mapping_charachter(x,y,hight,width)<= mapping_charachter(new_x,new_y,hight,width) <=1+mapping_charachter(x,y,hight,width): #check if the ord of value
                neighbore.append((new_x, new_y, weg + 1))                                                                                     #inside the domain of previous charchter and inside the range if mazze (two lists)

def mapping_charachter(x, y, hight, width):# to reterive the ord of charachter
    for i in range(hight):
        for j in range(width):
            if x == i and y == j:
                if ord(full_list[x][y]) == ord("S"):
                    return ord("a")
                if ord(full_list[x][y]) == ord("E"):
                    return ord("z")
                return ord(full_list[x][y])




print("Shortest path weight from start at S =",position_of_start_end(full_list,"S"))
print("Shortest path weight from start at a =",position_of_start_end(full_list,"a"))
