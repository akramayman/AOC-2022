from math import pow
with open("day25.txt", "rt") as Advent:
    Advent = Advent.read()

def read_text(Advent):
    Advent=Advent.split("\n")#split the text file by newline space
    data_Inlist=[]#the whole list for all data
    temparay=[]#use it to create list of list for each row
    for line in Advent:#read the line
        for item in line:#split each item in the line
            temparay.append(item)#append first list and intering in the big one
        data_Inlist.append(temparay)
        temparay=[]#to empty the inner list are used to create list of list
    return data_Inlist

def calculate_decimal(Advent):
    data=read_text(Advent)#retrieve the whole list
    answer=[]
    result=0
    for list in data:
        for index in range(len(list)):                    #len(list)-index-1 to read the list from right to left
            result+=decimal(list[index],len(list)-index-1)#convert the value to decimal by applied the decimal function in take the value and the value of power of 5
        answer.append(result)#append the output line by line
        result=0
    return sum(answer)

def decimal(value,power):#to retrieve the decimal coding value
    if value=="=":
        value=-2*pow(5,power)
    elif value=="-":
        value=-1*pow(5,power)
    else:
        value=int(value)*pow(5,power)
    return value

def SNAF(value,target,round,output):#take the changing value each time and the constant target and the round it represent the power of 5 and constant list
    answer_val=0
    while True:#untile reach the equivalent values between value and target
        new=int(value % pow(5,round)) #retrieve decoding for value by take the value and % the power of position
        if new not in [3,4,0,1,2]:#if it not in the range of -2 to 2 ,where -2 equal same moudulo output of three and 4 to -1 (-2 mod 5)=3 & (-1 mod 5)=4
            new=int(new/pow(5,round-1))#we take the value and do the divide by power of 5 with previous position
            if new==4:
                new=-1#change value if 4 to equal -1
                output.append(new)
            elif new==3:
                new=-2#change value if 3 to equal -2
                output.append(new)
            else:
                output.append(new)
        else:
            output.append(new)
        for i in range(len(output)):#to calculate the decimal coding for current list to use it to check the equivalent
            if output[i]==-2:
                output[i]="="
                answer_val += decimal(output[i], i)#take i here becaue it will be allready redable from right to left correct direction
            if output[i]==-1:
                 output[i]="-"
                 answer_val += decimal(output[i],i)
            else:
                answer_val+=decimal(output[i],i)
        if answer_val==target:
            return output
            break
        else:
            new_value=(value-(new*pow(5,round-1)))#update the value by take previous one - current one multiply 5 to power position -1
            round += 1
            return SNAF(new_value,target,round,output)#recursive

def test_decimal():
    assert calculate_decimal(test_example)==4890


test_example="""1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122"""
output=[]
print("Output of decimal value= ",calculate_decimal(Advent))#the output of file in decimal way
answer=SNAF(calculate_decimal(Advent),calculate_decimal(Advent),1,output)#to retrive the list of SNAF
answer.reverse()#revirese the list to take the correct order of value
answer=''.join(map(str, answer))#covert the output list to string to by easy to use the join
print("The SNAF coding for decimal value=",answer)
