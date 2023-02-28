with open("day10.txt", "rt") as Advent:
    Advent = Advent.read()
    Advent = Advent.splitlines()

def strength_during_problem1(Advent):
    strength_during = [20, 60, 100, 140, 180, 220]
    value,cycle=1,0#initial equation said the value start from 1
    full_string=[]
    for line in Advent:
        dir = line.split()
        if dir[0]=="noop":
            cycle +=1#increase one iteration if text equal noop
            if cycle in strength_during:
                full_string.append(value * cycle)#return output if we are in one of iteration strength_during[20,60,...]
        else:
            cycle +=1
            if cycle in strength_during:#check if first  cycle in strength_during
                full_string.append(value*cycle)
            cycle += 1
            if cycle in strength_during:#check if second cycle in strength_during
                full_string.append(value*cycle)
            value += int(dir[1])
    return sum(full_string) #sum for all these strength

def Day10_part2(Advent):
    cycle,value = 0,0
    Output_indexs = []#I save the position of peam in each iteration
    charch=["."]*240#empty list with length 240 of screen
    for line in Advent:
        dir = line.split()
        if dir[0]=="noop":
            Output_indexs.append(cycle)# append the value one because its one iteraton when text =noop
        else:
            value += int(dir[1])
            Output_indexs.append(cycle)
            Output_indexs.append(cycle)#add twise because its two iteration when find the addx
            cycle=value

    position=0
    for k in range(len(Output_indexs)):
        if position%40!=0 or position==0:#check if the position it is out of multiple 40 and not essintial as zero (and with moudulo we stay in range 40 of beam)
            if position ==Output_indexs[k] or position==Output_indexs[k]+1 or position==Output_indexs[k]+2:#check three position because there are 3 # in the beam
                charch[k]="#"
            else:
                charch[k]=" "
        else:
            position=0#if the count or position multiple of 40 then reset the beam checking
            if position ==Output_indexs[k] or position==Output_indexs[k]+1 or position==Output_indexs[k]+2:
                charch[k]="#"
            else:
                charch[k]=" "
        position+=1
    for w in range(0,len(charch),40):
        print("".join(charch[w:w+40]))#to print whole list as 6 line each one of them length 40

def test_part1():
    assert strength_during_problem1(exapmle)==13140


exapmle="""addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
"""
exapmle = exapmle.splitlines()
print("Output of part 1=",strength_during_problem1(Advent),"\nChrachters of part two =")
print(Day10_part2(Advent))




