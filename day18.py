from collections import deque
with open("day18.txt", "rt") as Advent:
    Advent = Advent.read()

def sides(text):
    text=text.split("\n")
    origin=set()
    Total=0
    part2=0
    Coor_x, Coor_y, Coor_z = [], [], []#To save and retrieve the full atmosphere of all cubes for part 2
    for j in text:
        x,y,z=map(int,j.split(","))
        origin.add((x,y,z))#to save all value from advent text
        Coor_x.append(x), Coor_y.append(y), Coor_z.append(z)
    min_x, max_x = min(Coor_x), max(Coor_x)
    min_y, max_y = min(Coor_y), max(Coor_y)
    min_z, max_z = min(Coor_z), max(Coor_z)
    for i in text:
        x,y,z=map(int,i.split(","))
        children = function_find_child(x, y, z)
        for cube in children:
            if cube in origin:#if the one of children is in the original data so it adjacent to him and don't count it
                continue
            if cube not in origin:
                Total+=1
            if part_2(cube,min_x,max_x,min_y, max_y,min_z, max_z,origin)==True:
                part2+=1
    return Total,part2

def function_find_child(x,y,z):
    child=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    children=[]
    for i,j,k in child:
        children.append((x+i,y+j,z+k))
    return children


def part_2(cube,min_x,max_x,min_y,max_y,min_z,max_z,origin):
    cube_faces=deque()
    cube_faces.append(cube)
    visited = set()
    while cube_faces:
        x,y,z=cube_faces.popleft()
        if (x,y,z) in origin:#check if this face in the origin list (stock)
            continue
        if (x,y,z) in visited:#if we already reach this point before
            continue
        visited.add((x,y,z))
        if x< min_x or x > max_x or y<min_y or y>max_y or z<min_z or z>max_z: #if we are out side the range of minimum or maximum that mean its air
            return True                                                       #so return True
        children = function_find_child(x, y, z)#retrieve all children or faces for this child to can be save whole path and keep adding these value to
        for x,y,z in children:                  #queue until reach out of the edge (air) or stuck in inner
            cube_faces.append((x,y,z))
    return False

def test_part1():
    assert sides(example)== (64,58)



example="""2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5"""

print("Approximate the surface area and the exterior area =",sides(Advent))