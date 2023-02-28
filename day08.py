with open("day08.txt", "rt") as Advent:
    Advent = Advent.read()

Advent=Advent.strip().split('\n')
full_list=[]
for items in Advent:
    full_list.append(list(map(int,items))) #create list of list and save the values as integer

def calculate_the_visible(full):
    up,down,right,left,counter=[],[],[],[],0
    for i in range(len(full)):#loop over all list
        for j in range(len(full[i])):#loop over len of inner list
            value=full[i][j] #save the value you need to check it
            for k in range(i + 1, len(full)):
                down.append(full[k][j])
            for w in reversed(range(i)):
                up.append(full[w][j])
            for item in range(j + 1, len(full[i])):
                right.append(full[i][item])
            for lef in reversed(range(j)):
                left.append(full[i][lef])
            #check in four direction and increment if onle are visible from one side
            if i==len(full)-1 or value>max(down):
                counter+=1
            elif i==0 or value>max(up):
                counter+=1
            elif j==len(full[i])-1 or value>max(right):
                counter+=1
            elif j==0 or value>max(left):
                    counter+=1
            up,down,right,left=[],[],[],[]
    return counter

def calculate_part_2(list):
    up, down, right, left, multi = [], [], [], [], []
    dir1,dir2,dir3,dir4=0,0,0,0
    for i in range(len(list)):  # loop over all list
        for j in range(len(list[i])):  # loop over len of inter list
            value = list[i][j]
            for k in range(i + 1, len(list)):
                down.append(list[k][j])
            for w in reversed(range(i)):
                up.append(list[w][j])
            for item in range(j + 1, len(list[i])):
                right.append(list[i][item])
            for lef in reversed(range(j)):
                left.append(list[i][lef])
            #loop over four direction and check the count of cheachter are less or equal in each direction and in the end multplie these count's
            if len(down)!=0:
                for dir1 in range(len(down)):
                    if value<=down[dir1]:
                        break
            if len(up)!=0:
                for dir2 in range(len(up)):
                    if value<=up[dir2]:
                        break
            if len(right)!=0:
                for dir3 in range(len(right)):
                    if value<=right[dir3]:
                        break
            if len(left)!=0:
                for dir4 in range(len(left)):
                    if value<=left[dir4]:
                        break
            multi.append((dir1+1)*(dir2+1)*(dir3+1)*(dir4+1))
            up, down, right, left = [], [], [], []
            dir1,dir2,dir3,dir4=0,0,0,0

    return max(multi)

test="""30373
25512
65332
33549
35390"""
def split_text_for_test(test):
    test=test.strip().split('\n')
    list_test = []
    for items in test:
        list_test.append(list(map(int, items)))
    return list_test
def test_part1():
    assert calculate_the_visible(split_text_for_test(test)) == 21


print("Problem1 = ",calculate_the_visible(Advent))
print("Problem2= ",calculate_part_2(Advent))


