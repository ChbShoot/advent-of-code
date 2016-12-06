
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis
# shouts out to /u/taliriktug for the guidance

input = open("day4.txt", 'r').read().split('\n')


def part1():
    sum = 0
    for line in input:
        if line is "":
            continue
        encrypted_name = line[0:(line.rfind("-"))].replace("-", "")
        sector_id = line[(line.rfind("-")+1):(line.find('['))]
        checksum = line[(line.find("[")+1):(line.find(']'))]

        encrypted_name = list(set([(encrypted_name.count(n), n) for n in encrypted_name]))
        encrypted_name.sort(key=lambda x: (x[0], -ord(x[1])), reverse=True)
        realname = ''.join(n[1] for n in encrypted_name[:5])
        if realname == checksum:
            sum += int(sector_id)
    print (sum)
key = 'abcdefghijklmnopqrstuvwxyz'
def part2():
    for line in input:
        if line is "":
            continue
        encrypted_name = line[0:(line.rfind("-"))]
        sector_id = int(line[(line.rfind("-")+1):(line.find('['))])
        checksum = line[(line.find("[")+1):(line.find(']'))]
        word = ""
        for letter in encrypted_name:
         
part2()