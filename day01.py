with open("day01.txt", "rt") as Advent:
    Advent = Advent.read()

def Calories (text):
    text=text.splitlines()
    value=0
    Elf_list=[]
    for line in text:
        if line!='':
            value+=int(line)
        else:
            Elf_list.append(value)
            value = 0
    Elf_list.append(value)
    return Elf_list

def Top_three (text):
    Elf=sorted(Calories(text),reverse=True)
    Max=0
    for i in Elf[:3]:
        Max+=i
    return Max

def test_Calories():
    assert max(Calories(text))==24000

def test_Top_three():
    assert Top_three(text)==45000

text="""1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


print("Output of Calories 1 =",max((Calories(Advent))))
print("Output of Top Three Calories 2 =",Top_three(Advent))