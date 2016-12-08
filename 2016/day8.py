# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis

input = open('day8.txt', 'r').read().split('\n')
width = 50
height = 6
screen = [ [ 0  for __ in range(width) ] for _ in range (height)] 
import sys

def rect(a,b):
    global screen
    for row in range (int(b)): #total height
        for col in range (int(a)): # across our row
            screen[row][col] = 1

def rotate(row, n):
    return (row[-int(n):] + row[:-int(n)])

def rotate_row(a,b):
    global screen
    screen[int(a)] = rotate(screen[int(a)], int(b))

def rotate_col(a, b):
    global screen
    col = [screen[i][int(a)] for i in range(height)] # turn our col into a row
    col = rotate(col, int(b))
    for i in range(height):
        screen[i][int(a)] = col[i]
    
for line in input:
    line = line.split()
    if 'rect' in line: #we have a rect op
        (a,b) = line[1].split('x')
        rect(a, b)
        print ("RECT A: {0}, B:{1}".format(a, b))
    if 'row' in line: #we have a row op
        a = line[2][line[2].find('=') + 1:]
        b = line[4]
        rotate_row(a,b)
        print ("ROW A: {0}, B:{1}".format(a, b))
    if 'column' in line:
        a = line[2][line[2].find('=') + 1:]
        b = line[4]
        rotate_col(a,b)
        print ("COL A: {0}, B:{1}".format(a, b))
def lit (): # it is not lit.. IT'S NOT lit. its lit again
    global screen
    return sum(sum(line) for line in screen)
def display():
    for y in range(height):
        for x in range(width):
            if screen[y][x]:
                sys.stdout.write('@')
            else:
                sys.stdout.write(' ')
        sys.stdout.write('\n')
print ('Part 1: {0} lit.'.format(lit()))
print ('Part 2:')
display()