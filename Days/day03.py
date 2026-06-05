with open("day03.txt", "rt") as Advent:
    Advent = Advent.read()
    Advent =Advent.splitlines()

def Compartments (Advent):
    list_of_findChr=[]
    Total_of_findChr=[]
    for i in Advent:
        part1=i[:(len(i) // 2)]
        part2=i[(len(i) // 2):]
        list_of_findChr.append(list(set(part2)&set(part1)))

    for j in list_of_findChr: #to get one list
        for item in j:
            Total_of_findChr.append(item)

    return Total_of_findChr

def Conver_toNumber (Charater_list):
    list_of_number=[]
    Dictionary_of_char = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11,
                         'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18,
                         's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26,
                         'A': 27, 'B': 28, 'C': 29, 'D': 30, 'E': 31, 'F': 32, 'G': 33, 'H': 34, 'I': 35, 'J': 36,'K': 37,
                         'L': 38, 'M': 39, 'N': 40, 'O': 41, 'P': 42, 'Q': 43, 'R': 44,
                         'S': 45, 'T': 46, 'U': 47, 'V': 48, 'W': 49, 'X': 50, 'Y': 51, 'Z': 52}
    for item in Charater_list:
        for i,j in Dictionary_of_char.items():
            if item ==i:
                list_of_number.append(j)

    return list_of_number

def test_Compartment_01():
    assert sum(Conver_toNumber(Compartments(text.splitlines())))==157 #the example of Advent of code

def test_Compartment_02():
    w="zzsSTtSTLzsspSdtTmHHmpmtFgqcgPlgFqWBqqqBMdWWvFlg".splitlines()
    assert sum(Conver_toNumber(Compartments(w))) == 4 #check one randome row from data

def test_Compartment_Issue_03():
    w=text2.splitlines()
    assert sum(Conver_toNumber(Compartments_Issue3(w))) == 70 #the example of Advent of code

def Compartments_Issue3(Advent):
    three_row=[]
    i=0
    while i<len(Advent):
        for w in Advent[i]:
            if w in Advent[i+1] and w in Advent[i+2]:
                three_row.append(w)
                break
        i=i+3 #jump three line in each round

    return three_row

text="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

text2="""vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""
print("The output of problem1=",sum(Conver_toNumber (Compartments(Advent))))
print("The output of problem2=",sum(Conver_toNumber (Compartments_Issue3(Advent))))

