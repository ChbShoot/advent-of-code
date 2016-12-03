
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis

input = open("day2.txt", 'r').read()

# Store our keypads
keypad = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
keypad2 = [ [0, 0, 1, 0, 0], [0, 2, 3, 4, 0], [5, 6, 7, 8, 9], [0, "A", "B", "C", 0], [0, 0, "D", 0, 0]]

# Position on keypad
x = 0
y = 0

code = ""
lines = input.split('\n')

# Tweaked move function from day 1
def move(keyp, direction):
    global x, y
    oldX = x
    oldY = y
    # North U
    if direction == 0:
        if x == 0:
            return
        else:
            x -= 1
    # East R
    elif direction == 1:
        if y == (len(keyp[x]) - 1):
            return
        else:
            y += 1
    # South D
    elif direction == 2:
        if x == (len(keyp) - 1):
            return
        else:
            x += 1
    # West L
    elif direction == 3:
        if y == 0:
            return
        else:
            y -= 1
    # Off key
    if keyp[x][y] == 0:
        x = oldX
        y = oldY

# Part 1 on first keypad
def part1():
    global x, y, code
    x = 1
    y = 1
    for instruction in lines:
        for dir in instruction:
            if dir == 'U':
                move(keypad, 0)
            elif dir == 'R':
                move(keypad, 1)
            elif dir == 'D':
                move(keypad, 2)
            elif dir == 'L':
                move(keypad, 3)
        code += str(keypad[x][y])
# Part 2 on second keypad
def part2():
    global x, y, code
    x = 2
    y = 0
    for instruction in lines:
        for dir in instruction:
            if dir == 'U':
                move(keypad2, 0)
            elif dir == 'R':
                move(keypad2, 1)
            elif dir == 'D':
                move(keypad2, 2)
            elif dir == 'L':
                move(keypad2, 3)
        code += str(keypad2[x][y])
part1()
print ("Part 1: " + code)
code = ""
part2()
print ("Part 2: " + code)