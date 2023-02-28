import re
with open("day15.txt", "rt") as Advent:
    Advent15 = Advent.read()

def raed_file(Advent):
    Sensors=[]
    Beacon=[]
    Manhattan=[]
    for line in Advent.splitlines():
        for i in line.split(":"):
            if i.startswith("Sensor")==True:
                x,y=re.findall(r'[+-]?\d+', i)#retrieve only the number for coordinate of sensor
                Sensors.append((int(x),int(y)))
            else:
                x2,y2 = re.findall(r'[+-]?\d+', i)#retrieve only the number for coordinate of beacon
                Beacon.append((int(x2), int(y2)))

    for coor in range(len(Sensors)):
        Manhattan.append(abs(Sensors[coor][0]-Beacon[coor][0])+ abs(Sensors[coor][1]-Beacon[coor][1])) #calculate the manhatten distance between sensor and beacon

    return Sensors,Beacon,Manhattan

def calculate_cannot_position(Advent,part):
    Sensors,Beacon,Manhattan=raed_file(Advent)
    Diamond=[]
    if part=="Advent":#just to can applied the test function for different target and example data
        target =2000000
    else:
        target = 10

    for ind, pos in enumerate(Sensors):
        new_x = Manhattan[ind] - abs(pos[1] - target)#find how many digit you need to increase and decrease from center using to find the coordinate
        if new_x<=0:#to keep value position and in the left or right
            continue
        Diamond.append((pos[0] - new_x, target))#append the list for edge of diamond in that location (negative) with target y axis
        Diamond.append((pos[0] + new_x, target))#append the list for edge of diamond in that location (positive) with target y axis

    temp=[]#temporary list to extract the minimum and maximum value (interval in target column)
    for k in Diamond:
        temp.append(k[0])

    Total_interval=[]#create list that save all x indexes in the target column
    for m in range(min(temp),max(temp)+1):
        Total_interval.append(m)

    output=len(Total_interval)#interval length
    for item in set(Beacon):#if the column contain a beacon reduce the total positions by one
        if item[1]==target:
            output-=1

    return output

def test_part1():
    assert calculate_cannot_position(example,"example")==26

example = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
"""
print("The out put of part one= ",calculate_cannot_position(Advent15,"Advent"))