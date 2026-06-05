import re
with open("day11.txt", "rt") as Advent11:
    Advent = Advent11.read()
    Advent = Advent.strip().split('\n\n')

def read_the_textfile(text):
    Monkeys,values,equation,divided,divisible_true,divisible_false,temparary=[],[],[],[],[],[],[]#see how we can read text as spliting in internet (https://www.youtube.com/watch?v=W9vVJ8gDxj4&ab_channel=JonathanPaulson)
    for line in text:
        Name, starting, op, tests, true, false = line.split('\n') #each line save values in list
        Name=Name.replace(":"," ")
        Monkeys.append(int(Name.split()[-1])) # to save the number of monkey (to know how many monkey do we have )
        starting=starting.split(":")#split the strating line to satrting: and values
        starting=starting[1].split(",")#take values and split by " , "
        for i in starting:
            temparary.append(int(i)) #temparay list to save the values of starting
        values.append(temparary) #to have only the value without list of list
        temparary=[]
        op=op.split("=")
        equation.append(op[1]) #save the equation of each monkey
        divided.append(int(tests.split()[-1])) #save the divided value
        divisible_true.append(int(true.split()[-1])) #true value
        divisible_false.append(int(false.split()[-1])) #false value

    return Monkeys,values,equation,divided,divisible_true,divisible_false

def calculate_inspect(text,cutof):
    round = 0
    Monkeys, values, equation, divided, divisible_true, divisible_false=read_the_textfile(text)

    full_inspection=[0 for _ in range(len(Monkeys))]#initial zeros inspection for all monkeys
    while round<cutof:
        for i in range(len(Monkeys)): #range the biggest list
            j=len(values[i]) #len of values in inner list of first monkey
            while j > 0: #while the list is not empty
                full_inspection[i] += 1 #count the inspection for each monkey
                k=0
                old=values[i][k]
                ans=eval(equation[i])//3
                if ans % divided[i] ==0:# check if the value are divisible or not
                    values[divisible_true[i]].append(ans) #append the value after calculation in target list
                    values[i].remove(old) #remove the value from current list

                else:
                    values[divisible_false[i]].append(ans)
                    values[i].remove(old)
                j=j-1 #update j be reduced one because the list will pop value to true or false


        round+=1
    full_inspection=sorted(full_inspection)
    return full_inspection[-1]*full_inspection[-2]

def calculate_inspect_part2(text, cutof):
    round = 0
    Monkeys, values, equation, divided, divisible_true, divisible_false = read_the_textfile(text)

    Total_divisible = 1
    for divi in divided:#this idea from internet (by take multiplication all value of divisible in test line  and during calculation take output of eval mudulo this total)
        Total_divisible *= divi

    full_inspection = [0 for _ in range(len(Monkeys))]
    while round < cutof:
        for i in range(len(Monkeys)):  # range the biggest list
            j = len(values[i])  # len of inner list
            while j > 0:  # while the list is not empty
                full_inspection[i] += 1  # count the inspection for each monkey
                k = 0
                old = values[i][k]
                ans = eval(equation[i]) % Total_divisible
                if ans % divided[i] == 0:  # check if the value are divisible or not
                    values[divisible_true[i]].append(ans)  # append the value after calculation in target list
                    values[i].remove(old)  # remove the value from current list

                else:
                    values[divisible_false[i]].append(ans)
                    values[i].remove(old)
                j = j - 1  # update j be reduced one because the list will pop value to true or false

        round += 1
    full_inspection = sorted(full_inspection)
    return full_inspection[-1] * full_inspection[-2]

def test_part1():
    assert calculate_inspect(Test,20)==10605

def test_part2():
    assert calculate_inspect_part2(Test,10000)==2713310158

Test = """Monkey 0:
          Starting items: 79, 98
          Operation: new = old * 19
          Test: divisible by 23
            If true: throw to monkey 2
            If false: throw to monkey 3

        Monkey 1:
          Starting items: 54, 65, 75, 74
          Operation: new = old + 6
          Test: divisible by 19
            If true: throw to monkey 2
            If false: throw to monkey 0

        Monkey 2:
          Starting items: 79, 60, 97
          Operation: new = old * old
          Test: divisible by 13
            If true: throw to monkey 1
            If false: throw to monkey 3

        Monkey 3:
          Starting items: 74
          Operation: new = old + 3
          Test: divisible by 17
            If true: throw to monkey 0
            If false: throw to monkey 1
        """
Test = Test.strip().split('\n\n')

print("Part 1 number of item inspect=",calculate_inspect(Advent,20))
print("Part 2 number of item inspect=",calculate_inspect_part2(Advent,10000))
