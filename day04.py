import re

with open("day04.txt", "rt") as Advent:
    Advent = Advent.read()

def intersectio(text):
    text= re.split(r'[-,\n]', text)
    text=list(map(int,text)) #list of values as integers
    i,j,count_paris,overlapping=0,0,0,0
    range1=[]
    range2=[]
    while i<len(text):
        while j in range(i,i+4):
                range1.extend(range(text[j],text[j+1]))#extend the list with all values between this range
                range1.append(text[j+1])

                range2.extend(range(text[j+2],text[j+3]))#extend the list with all values between this range
                range2.append(text[j + 3])

                if (range1[0]<=range2[0] and range1[-1]>=range2[-1]) or (range2[0]<=range1[0] and range2[-1]>=range1[-1]):#check if full
                    count_paris+=1

                #part two to find all Overlappint
                if len((set(range2) & set(range1)))!=0:
                    overlapping+=1

                range1 = []
                range2 = []
                break
        j=i+4 #to start at the end of i because i take 4 value as first pairs 
        i+=4 #jump four digit each time

    return count_paris,overlapping


def test_intersectio():
    assert intersectio(text)== (2,4)

text="""2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""


print("First value is fully contain and second one is overlapping=",intersectio(Advent))