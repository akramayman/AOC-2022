from collections import defaultdict # subclass of the built-in dict class
with open("day07.txt", "rt") as Advent:
    Advent = Advent.read()


def problem_1(text):
    command=text.strip().split('\n') #split all text with \n
    list_path=[] #to folow where we are currently
    list_score=defaultdict(int)
    for line in command:
        words = line.strip().split() #split element in the line
        if words[1]=="cd":#access the directory
            if words[2]=="..":#thats mean I back to previous dir so i pop the dic
                list_path.pop()
            else:
                list_path.append((words[2]))
        elif words[1]=="ls":#that's mean we just read what in the file
            continue
        elif words[0]=="dir":
            continue
        else:
            for i in range(1, len(list_path) + 1):
                list_score['/'.join(list_path[:i])] += int(words[0]) #to update value for the same directory if it exict in the dic
    return  list_score

def calculate_the_part1(text):
    size = 0
    score=problem_1(text)
    for tuple,value in score.items():
        if value <=100000:#check if the path in the dir have value less we add id to size
            size += value
    return size

def calculate_the_part2(text):
    avalible=70000000
    empty=[]
    all_path=problem_1(text)
    total = all_path['/']#retrieve the size of root
    remain=avalible-total #total disk - total current size
    for i, j in all_path.items():
        if j >= (30000000-remain):#retrieve the value the grater the whole size - remiain to find the space to do the update
            empty.append(j)
    return min(empty)#minmum file need to delete to do the update

def test_part1():
    assert calculate_the_part1(te555xt)==95437

def test_part2():
    assert calculate_the_part2(te555xt)==24933642


te555xt ="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""
print("The output of first part =",calculate_the_part1(Advent))
print("The output of second part =",calculate_the_part2(Advent))





