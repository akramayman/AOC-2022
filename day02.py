#column 1 A for Rock, B for Paper, and C for Scissors
#column 2 X for Rock, Y for Paper, and Z for Scissors
#-----part1-----
with open("day02.txt", "rt") as Advent02:
    Advent = Advent02.read()

def play (text):
    text=text.splitlines()
    list_strategy=[]
    for line in text:
        w, o = line.split()
        choose={'X':1,'Y':2,'Z':3}[o]
        opponent={('A','X'):3,('A','Y'):6,('A','Z'):0,
                  ('B', 'X'): 0, ('B', 'Y'): 3, ('B', 'Z'): 6,
                  ('C', 'X'): 6, ('C', 'Y'): 0, ('C', 'Z'): 3,
                  }[w,o]
        list_strategy.append(choose+opponent)
    return list_strategy

def test_play_part1():
    assert sum(play(test))==15

#X means you need to lose =0 , Y means you need to end the round in a draw = 3, and Z means you need to win = 6
#-----Part_two-----

def play_part_two (text):
    text=text.splitlines()
    strategy_part02=[]
    for line in text:
        w, o = line.split()
        choose={'X':0,'Y':3,'Z':6}[o]
        opponent={('A','X'):3,('A','Y'):1,('A','Z'):2,
                  ('B','X'): 1, ('B', 'Y'): 2, ('B','Z'): 3,
                  ('C', 'X'): 2, ('C', 'Y'): 3, ('C', 'Z'): 1,
                  }[w,o]
        strategy_part02.append(choose+opponent)
    return strategy_part02

def test_play_part2():
    assert sum(play_part_two(test))==12

test="""A Y
B X
C Z"""

print("Output of Strategy guide part=",sum(play(Advent)))
print("Output of Lose,Draw,Win part=",sum(play_part_two(Advent)))