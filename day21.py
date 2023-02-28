import re
test="""root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""
with open("day21.txt", "rt") as Advent:
    Advent = Advent.read()

def read_file(Advent):
    test=Advent.split("\n")
    dictionary_variable={}
    special_characters = "%^*-+/"
    for i in test:#to fill the dictionary with all values and keys from text file
        value, equation = i.split(":")
        if any(c in special_characters for c in i)==False:#if the text not contain any thing of + - * / so int's integer and save it as integer
            dictionary_variable[value]=int(equation)       #(https://docs.python.org/3/library/functions.html?highlight=any#any)
        else:
            dictionary_variable[value] = equation #save the equation
    value_ss('root',dictionary_variable)
    return dictionary_variable['root']

def value_ss(x,dictionary_variable):
    d=dictionary_variable[x] #retreive the value of key x
    if type(d)== int:#if the value of key its integer so return this integer
        return d
    else:
        new = [t.strip() for t in re.split(r'[%/:/+/*/-]', d)] #using re.split to move over d and check if it contain one calculation symbol so split by it and strip to remove any space in key
        value1= value_ss(new[0],dictionary_variable)#check first variable and retrive the value of it
        value2= value_ss(new[1], dictionary_variable)#check second variable and retrive the value of it
        dictionary_variable[x]=int(eval(d,dictionary_variable)) #applied the equation


def test_part1():
    assert read_file(test)==152
print("Output of root value part1=",read_file(Advent))




