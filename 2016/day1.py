
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis

input = open("day1.txt", 'r').read()

# Current position data
x = 0
y = 0
# Direction works increasingly clockwise where NESW is 0123
direction  = 0
#Cap our direction
def rectify():
    global direction
    if direction < 0:
        direction = 3
    elif direction > 3:
        direction = 0
#Perform our turn
def turn(clock):
    global direction
    direction += clock
    rectify()
#Move in current facing direction
def move(steps):
    global x, y
    if direction == 0:
        y += steps
    elif direction == 2:
        y -= steps
    elif direction == 1:
        x += steps
    elif direction == 3:
        x -= steps

#"Find" Easter Bunny HQ
def part1():
    for instruction in input.split(', '):
        if instruction[0] == 'R':
            turn(1)
        elif instruction[0] == 'L':
            turn (-1)
        move(int(instruction[1:]))

    print (abs(x) + abs(y))

def part2():
    history = set()
    found = False
    for instruction in input.split(', '):
            if instruction[0] == 'R':
                turn(1)
            elif instruction[0] == 'L':
                turn (-1)
            for i in range(0, int(instruction[1:])):
                move(1)
                pos = str(x) + ", " + str(y)
                if pos not in history and not found:
                    history.add(pos)
                elif pos in history and not found:
                    print("Found! " + pos)
                    print (abs(x) + abs(y))
                    found = True

def draw():
    been = list()
    for instruction in input.split(', '):
            if instruction[0] == 'R':
                turn(1)
            elif instruction[0] == 'L':
                turn (-1)
            for i in range(0, int(instruction[1:])):
                move(1)
                pos = [(x, y)]
                been += pos
    been.sort()
    temp = tuple(map(sorted, zip(*been)))
    min_x, max_x, min_y, max_y = temp[0][0], temp[0][-1], temp[1][0], temp[1][-1]
    width = abs (max_x - min_x) + 1
    height = abs (max_y - min_y) + 1

draw()