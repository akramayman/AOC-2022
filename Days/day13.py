from functools import cmp_to_key

with open("day13.txt", "rt") as Advent:
    Advent = Advent.read()
    part_1 = Advent.strip().split('\n\n')#save two pairs as an elemnt in the list
    part_2 = Advent.strip().replace('\n\n','\n').split("\n")#to save each list as one element in the list

def compare_two(left,right):
    if type(right)==int and type(left)==list:
        right=[right]
    if type(right)==list and type(left)==int:
        left=[left]
    if type(right)==int and type(left)==int:
        if left<right: #if the in the right order return 100 else -1
            return 100
        if left>right:
            return -1
    if type(right)==list and type(left)==list:
        length=0
        while length<len(right) and length<len(left):#if both of them are list and check at the same time the length should be less of length of both list
            output=compare_two(left[length],right[length])
            if output==100:
                return 100
            if output==-1:
                return -1
            length += 1
        if length == len(left):#if the left paris are complated
            if len(right) == len(left):# equal right paris thats mean still looping over pairs
                return None
            return 100 #that's mean left pair are finish and it in the right order
        return -1 #thats mean the right paris are finish and it in the left order

def get_the_result_part1(Advent):
    Number_pairs = []
    counter = 0
    for item in Advent:
        left, right = item.split("\n")#split the pair for right and left list
        right = eval(right)
        left = eval(left)
        counter += 1
        if compare_two(left, right) == 100:
            Number_pairs.append(counter)#save the Id of pair
    return (sum(Number_pairs))

def get_the_result_part2(Advent):
    Integer_list=[]
    for i in range(len(Advent)):
        Integer_list.append(eval(Advent[i]))
    Integer_list.append([[2]]) # add the divider packets by equations
    Integer_list.append([[6]])
    Ordering=sorted(Integer_list,key=cmp_to_key(compare_two),reverse=True) #I take this function cmp_to_key from internet and it doing by take each value (https://docs.python.org/3/library/functools.html)
    #and compare it with all other values and returns a negative number for less-than, zero for equality, or a positive number for greater-than
    counter,position1,position2=1,0,0 #counter equal 1 that mean first list in ordere (because the normal thing is zero)
    for j in Ordering:
        if j==[[2]]:
            position1=counter
        if j==[[6]]:
            position2=counter
        counter+=1
    return position1*position2

def test_part1():
    assert get_the_result_part1(text1)==13

def test_part2():
    assert get_the_result_part2(text2)==140

text="""[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""
text1=text.strip().split("\n\n")
text2=text.strip().replace('\n\n','\n').split("\n")

print("The output of part two=",get_the_result_part1(part_1))
print("The output of part one=",get_the_result_part2(part_2))





