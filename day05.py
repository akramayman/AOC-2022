import re
import copy

with open("day05.txt", "rt") as Advent:
    Advent = Advent.read()

def Stacks(Advent,list_P1,list_P2):
    l = []
    p,m = "",""
    for i in Advent.splitlines():
        if i.startswith('move'):# to jump to first line with start with move
            q = re.findall(r'\d+', i)#retrive only number from each line of text
            for j in q:
                #for k in j:
                l.append(int(j))
            value=l[0]#save the movement value to use it in problem part 2
            for t in range(len(list_P1)):#to find the list it will be poped
                if t == l[1] :
                    for u in range(len(list_P1)):#to find list it will be append
                        if u == l[2]:
                            for x in range(0, l[0]):#to pop all value in range the movement in text
                                element = list_P1[t].pop()
                                list_P1[u].append(element)

                            for f in range(0,value):# create value variable to save the movement and its solution of problem part 2
                                q = list_P2[t].pop(len(list_P2[t]) - value)
                                list_P2[u].append(q)
                                value = value - 1 #we need to reduce value each time to take the next position of pop
            l = []
    for items in list_P1:#to retrive the last value in each list problem part 1
        if len(items) != 0:
            p = p + items[-1]

    for item in list_P2:#problem part 2
        if len(item) != 0:
            m = m + item[-1]
    return p,m

def test_Stacks():
    assert Stacks(Advent,list_P1,list_P2)==('QPJPLMNNR', 'BQDNWJPVJ')


list_P1=[[],['R','N','F','V','L','J','S','M'],['P','N','D','Z','F','J','W','H'],['W','R','C','D','G'],
       ['N','B','S'],['M','Z','W','P','C','B','F','N'],['P','R','M','W'],
       ['R','T','N','G','L','S','W'],['Q','T','H','F','N','B','V'],['L','M','H','Z','N','F']]
list_P2=copy.deepcopy(list_P1)

text_test5=[[],['Z','N'],['M','C','D'],['P']]
text_test5_copy=copy.deepcopy(text_test5)
text="""
move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


#print(Stacks(Advent,list_P1,list_P2))


