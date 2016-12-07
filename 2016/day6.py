
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis

import collections

input = open('day6.txt', 'r').read().split('\n')

def part(which):
    # length of our message, usually 8(?)
    message_length = len(input[0])
    message = ""
    # 2d array for each letter
    letters = [ ('') ] * message_length
    for i in range(len(input)):
        for j in range(message_length):
            try:
                letters[j]+= input[i][j]
            except IndexError: #debug
                print ("i = {0} j = {1} input = {2}".format(i, j, input[i]))
    for check in letters:
        c = collections.Counter()
        c.update(check)
        # Part 1, we take the most common letter
        if which is 1:
            message += str(c.most_common(1)[0][0])
        # Part 2, we take the least common letters
        elif which is 2:
            message += str(c.most_common()[-1:][0][0])
    return message