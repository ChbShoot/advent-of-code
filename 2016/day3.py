# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis

input = open("day3.txt", 'r').readlines()

# Quick-o triangle check
def is_triangle(trig):
    trig.sort()
    return ((trig[0] + trig[1]) > trig[2])

def part1():
    trigs = 0
    for sides in input:
        line = sides.split()
        trig = [int(line[0]), int(line[1]), int(line[2])]
        if is_triangle(trig):
            trigs += 1
    print (trigs)

def part2():
    trigs = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    dimension = 0
    count = 0
    for sides in input:
        line = sides.split()
        for i in range(0, 3):
            trigs[i][dimension] = int(line[i])
        if dimension is not 2:
            dimension += 1
            continue
        else: # We've reached the third line, time to start the next 3 triangles
            dimension = 0
            for i in range(0, 3):
                if is_triangle(trigs[i]):
                    count += 1
            trigs = [ [0, 0, 0], [0, 0, 0], [0, 0, 0] ]
    print (count)