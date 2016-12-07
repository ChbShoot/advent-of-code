
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis


from hashlib import md5
from sys import stdout

def part1():
    word = 'ffykfhsq'
    intdex = 0
    foundDex = 0
    found = []
    password = ""

    # While we have not found our 8 length password
    while len(found) is not 8:

        # Encode our word plus our index and output hexadecimal representation
        md = md5(str(word + str(intdex)).encode('utf-8')).hexdigest()
        password = md[:8] # completely unnecessary

        if str(md[:5]) is '00000': # if the first five digits are zeroes
            found[foundDex] = md[5] # add the 6th digit to our found password array
            foundDex += 1

        # display our password
        for i in range(len(found)):
            password[i] = found[i]

        stdout.write("\r" + password)
        stdout.flush()
        intdex += 1

part1()