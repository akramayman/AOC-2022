import copy #to use it in take a copy of the tuples of list (position and value)

with open("day20.txt", "rt") as Advent:
    Advent = Advent.read()

def _Calulate_coordinate(Advent,key,part):
    Advent = Advent.strip().split("\n") #remove the white space lines
    original_list = []
    for i in Advent:
        if part=="part1":#to check we applied which part
            original_list.append(int(i))#insert the values as integer in the list
        else:
            original_list.append(int(i) * key)
    value_original_inde=[]
    for original_index, value in enumerate(original_list):
        value_original_inde.append((value,original_index))#to save in this list each value with current original position

    update_list=copy.deepcopy(value_original_inde)

    round=0
    while round!=10:
        for val,ind in value_original_inde:#lop over the original value and read value and position for it
            new_value=update_list.index((val,ind))#retrive the current position for this tuple in the modified list
            new=update_list.pop(new_value) #pop the value from the list
            new_index = (new_value + val) % (len(original_list) - 1) #calculate the new position of the value and keep it in range of list by take modulo
            update_list.insert(new_index,new)#insert the value with the new position in the new location
        if part=="part1":#to check we applied which part
            break
        else:
            round+=1


    for zero in range(len(update_list)):# find the finial position of 0 in updated list
        if update_list[zero][0]==0:
            position_zero=zero

    #to retrive the value after 0 in coordinates
    coordinates=[1000,2000,3000]
    answer=[] #to save the value of answer after coordinates
    for val in coordinates:
        ans=(position_zero+val)%len(update_list)#calculate the position of coordinate by sum the position of zero with values of coordinate
        answer.append(update_list[ans][0])#retrieve the value in that position

    return sum(answer)

def test_coordinate():
    assert _Calulate_coordinate(test,decryption_key,part="part1")==3

def test_part2():
    assert _Calulate_coordinate(test, decryption_key, part="part2") == 1623178306

decryption_key=811589153
test="""1
2
-3
3
-2
0
4
"""
print("The output of part 1= ",_Calulate_coordinate(Advent,decryption_key,part="part1"))
print("The output of part 1= ",_Calulate_coordinate(Advent,decryption_key,part="part2"))

