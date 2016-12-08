
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis
# we got a little crazy here


input = open('day7.txt', 'r').read().split('\n')

def palindrome(checking):
    if len(checking) is not 4:
        return None
    return (checking[0] is checking[3] and checking[0] is not checking[1] and checking[1] is checking[2])

def check_aba(checking):
    if len(checking) is not 3:
        return None
    return (checking[0] is checking[2] and checking[0] is not checking[1])

def get_sequences(line):
    regular = [ ("") ] * 6
    hyper = [("")] * 6
    hypernet = False
    hyper_index = 0
    regular_index = 0
    for letter in line:
        if not hypernet and letter is '[':
            hypernet = True
            regular_index += 1
            continue
        elif hypernet and letter is ']':
            hypernet = False
            hyper_index += 1
            continue
        if hypernet:
            hyper[hyper_index] += letter
        else:
            regular[regular_index] += letter
    return (regular, hyper)

def part1():
    goods = 0
    for line in input:
        (regular, hyper) = get_sequences(line)
        still_good = True
        for sequence in hyper:
            if still_good is False:
                break
            for i in range(len(sequence) - 3): # stop 3 before because ever i we check the folloing 3
                still_good = (palindrome(sequence[i:i+4]) is False)
                if still_good is False:
                    break
        if still_good is not False:
            still_good = False
            for sequence in regular:
                if still_good is True:
                    break
                for i in range(len(sequence) - 3):
                    still_good = palindrome(sequence[i:i+4])
                    if still_good is True:
                        break

        if still_good:
            goods += 1
    return goods

def part2():
    goods = 0
    for line in input:
        (regular, hyper) = get_sequences(line)
        abas = []
        corr_babs = []
        still_good  = False
        for sequence in regular:
            for i in range(len(sequence) - 2):
                if check_aba(sequence[i:i+3]):
                    abas.append(sequence[i:i+3])
        if len(abas) > 0:
            for aba in abas:
                corr_babs.append((aba[1] + aba[0] + aba[1]))
        if len (corr_babs) > 0:
            for sequence in hyper:
                if still_good:
                    break
                for i in range(len(sequence) - 2):
                    if still_good:
                        break
                    if sequence[i:i+3] in corr_babs and not still_good:
                        goods += 1
                        still_good is True
    return goods


print ("Good IP Addresses: {0}".format(part1()))
print ("SSL IP Addresses: {0}".format(part2()))