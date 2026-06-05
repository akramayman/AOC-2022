with open("day09.txt", "rt") as Advent:
    Advent = Advent.read()
    Advent = Advent.splitlines()

def calculate_the_tail_visited(text):
    head = [0,0]#initial position for head
    tail = [0,0]#initial position for tail
    fullpath = [(0, 0)]#to save whole path of tail as tuple
    for line in text:
        dir,val = line.split()#split the text to direction charachter and the value of movement
        for i in range(int(val)):
            if dir=="R":
                head[0]+=1#update the x moving right
                if abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1:#check if the difference grater that 1 that mean its out of 8 ragion around so need to change the position of tail
                    tail[1]=head[1]
                    tail[0]=head[0]-1#to give the previous location of head to tail
                    fullpath.append(tuple(tail))#append the position as tuple to can't modife it (it's immutable)
            elif dir=="L":
                head[0] -=1#update the x moving left
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:#check if the difference grater that 1 that mean its out of 8 ragion around so need to change the position of tail
                    tail[1] = head[1]
                    tail[0] = head[0]+1
                    fullpath.append(tuple(tail))
            elif dir=="U":
                head[1] +=1#update the y moving up
                if abs(head[0]-tail[0])>1 or abs(head[1]-tail[1])>1 :#check if the difference grater that 1 that mean its out of 8 ragion around so need to change the position of tail
                    tail[1] = head[1]-1
                    tail[0] = head[0]
                    fullpath.append(tuple(tail))
            elif dir=="D":
                head[1] -=1#update the y moving down
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:#check if the difference grater that 1 that mean its out of 8 ragion around so need to change the position of tail
                    tail[1] = head[1]+1
                    tail[0] = head[0]
                    fullpath.append(tuple(tail))
    return len(set(fullpath))#to retrieve the total number of movement with at least one visited

def test_path_problem1():
    assert calculate_the_tail_visited(text1)==13

def calculate_9tail_part2(text):
    tail_robe = [[0, 0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]#initial position for tail
    path_tail9 = [(0, 0)]#to save whole path of tail as tuple
    for line in text:
        dir,val = line.split()#split the text to direction charachter and the value of movement
        for i in range(int(val)):
            if dir=="R":
                tail_robe[0][1] += 1
            elif dir=="L":
                tail_robe[0][1] -= 1
            elif dir=="U":
                tail_robe[0][0] += 1
            elif dir=="D":
                tail_robe[0][0] -= 1
            for j in range(9):
                newx=tail_robe[j][0]-tail_robe[j+1][0]
                newy=tail_robe[j][1]-tail_robe[j+1][1]
                if newx==0 and newy>1:#move right in the same row
                    tail_robe[j+1][1] += 1
                elif newx==0 and newy<-1:#move left in the same row
                    tail_robe[j+1][1] -= 1
                elif newx>1 and newy==0:#move up same column
                    tail_robe[j+1][0] += 1
                elif newx<-1 and newy==0:#move down same column
                    tail_robe[j+1][0]-=1

                elif newx>1 and newy>0:#move right corner R first squre of coordinate [2,5][0,4]
                    tail_robe[j+1][0] +=1
                    tail_robe[j+1][1] +=1
                elif newx>0 and newy>1:#second move right corner R [1,5][0,3] should be now [1,4]
                    tail_robe[j + 1][0]+=1
                    tail_robe[j + 1][1]+=1

                elif newx>0 and newy<-1:#move left corner L to third sequre of coordinate
                    tail_robe[j + 1][0] += 1
                    tail_robe[j + 1][1] -= 1
                elif newx > 1 and newy < 0:##second move L to third squre of coordinate
                    tail_robe[j + 1][0] += 1
                    tail_robe[j + 1][1] -= 1


                elif newx<0 and newy>1:#first move to the second coordinate
                    tail_robe[j + 1][0] -= 1
                    tail_robe[j + 1][1] += 1
                elif newx<-1 and newy>0:#second move to the second coordinate
                    tail_robe[j + 1][0] -= 1
                    tail_robe[j + 1][1] += 1

                elif newx<-1 and newy<0:#first move to the fourth coordinate
                    tail_robe[j + 1][0] -= 1
                    tail_robe[j + 1][1] -= 1
                elif newx<0 and newy<-1:#second move to the fouth coordinate
                    tail_robe[j + 1][0] -= 1
                    tail_robe[j + 1][1] -= 1

            path_tail9.append(tuple(tail_robe[9]))

    return len(set(path_tail9))

def test_path_problem2():
    assert calculate_9tail_part2(text2)==36

text1="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""
text2="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""
text1=text1.splitlines()
text2=text2.splitlines()

print("The Output path length of tail for part one=",calculate_the_tail_visited(Advent))
print("The Output path length of tail 9 for part two=",calculate_9tail_part2(Advent))
