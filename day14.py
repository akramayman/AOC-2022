with open("day14.txt", "rt") as Advent:
    Advent = Advent.read()
    text=Advent.split("\n")
def retreive_positions(text):
    direction=[]
    temparary=[]#to can work on original range of list
    poistion=1#to increment the position
    for i in text:
        inner=i.replace("->","\n").split("\n")#to split range one of ranges like(498,4 -> 498,6 -> 496,6) to ['498,4','498,6',....]
        for j in inner:
            x,y=j.split(",")
            x,y=int(x),int(y)#convert text to inetger
            temparary.append((x,y))
            direction.append((x,y))
        for i in range(len(temparary)-1):#whole length -1 to can take pairs of two
            x1,y1=temparary[i]#current
            x2,y2=temparary[i+1]#next one
            if x1==x2 and y1!=y2:#thats mean the y position need to change
                for k in range(min(y2,y1)+1,max(y2,y1)):#the value between min+1 and max
                    direction.append((x1,min(y1,y2)+poistion))#to add all values between the y axis in direction list (save all position of # rocks)
                    poistion+=1
            if x1 != x2 and y1 == y2:#thats mean the x position need to change
                for k in range(min(x1,x2)+1,max(x1,x2)):
                    direction.append((min(x1,x2)+poistion,y1))#to add all values between the x axis in direction list
                    poistion += 1
            poistion=1
        temparary=[]
    end_of_rock = []
    for j in direction:
        end_of_rock.append(j[1])
    end_of_rock=max(end_of_rock)#to save the end (maximum before abyss الهاوية)
    return direction,end_of_rock

def fall(text):
    listpos,max_rock=retreive_positions(text)
    x,y = 500, 0#start position of sand
    counter_fall=0
    while y<=max_rock:#to check before goes to abyss (هاوية)
        if (x,y+1) not in listpos:#check the down one step if it is in the list or not
            New=(x,y+1)
            y += 1
            continue
        if (x-1,y+1) not in listpos:#check the down one step left if it is in the list or not
            New=(x-1,y+1)
            y += 1
            x -=1
            continue
        if (x+1,y+1) not in listpos:#check the down one step right if it is in the list or not
            New=(x+1,y+1)
            y += 1
            x +=1
            continue
        listpos.append(New)
        x,y = 500, 0#reset the start of sand because its start entering from same start position
        counter_fall+=1#count how many time we insert sand

    return counter_fall

def test_part1():
    assert fall(test_text)==24

def fall2(text):
    x,y = 500, 0#strat position of sand
    lists, values = retreive_positions(text)
    lists=set(lists)#modified the original to set to reduce the number of element in the list by take the unique value (because it take too long time using list like first part so I see on internet and change this part to set)
    count_infinite=0
    while True:#this loop to continue looping inner loop until find the 500,0
        while y<=values:#to check before goes to abyss (هاوية)
            if (x,y+1) not in lists:#check the down one step if it is in the list or not
                y += 1
                continue
            if (x-1,y+1) not in lists:#check the down one step left if it is in the list or not
                y += 1
                x -=1
                continue
            if (x+1,y+1) not in lists:#check the down one step right if it is in the list or not
                y += 1
                x +=1
                continue
            break
        count_infinite+=1
        lists.add((x,y))
        if (x,y) ==(500,0):
            return count_infinite
        x, y = 500, 0

def test_part2():
    assert fall2(test_text)==93

test_text="""498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
test_text=test_text.split("\n")

print("Number units of sand come to rest before sand starts flowing into the abyss below part1=",fall(text))
print("Number units of sand come to rest part2=",fall2(text))
