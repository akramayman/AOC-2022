from collections import Counter
with open("day06.txt", "rt") as Advent:
    Advent = Advent.read()

def Problem_1(text):
    j=0
    list=[]
    list_of_index=[]
    while j <len(text)-3:#because you need four different charachter
        for i in range(j,j+4):
            list.append(text[i])#to save only four charachter each time
            if len(set(list))==4:#to check if it are uniqe charachter of not
                list_of_index.append(i+1)
        list=[]#reempty the list
        j+=1#move on
    return list_of_index[0]

def Problem_2(text):
    j=0
    list=[]
    list_of_index=[]
    while j <len(text)-13:#because you need 13 different charachter
        for i in range(j,j+14):#14 digit
            list.append(text[i])
            if len(set(list))==14:
                list_of_index.append(i+1)
        list=[]
        j+=1
    return list_of_index[0]

def testProblem1 ():
    assert Problem_1(w)==10
def testProblem2():
    assert Problem_2(w)==29


w='nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'
print("Output of part 1=",Problem_1(Advent),"\nOutput of Part 2=",Problem_2(Advent))