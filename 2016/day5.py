
# Advent of Code - 2016
# http://adventofcode.com/
# author: Jose M. Luis

#note: commented out useless slow cool terminal effects


from hashlib import md5
import time
#from sys import stdout

start = time.time()
def part1():
    global start
    word = 'ffykfhsq'
    intdex = 0
    password = ""

    # While we have not found our 8 length password
    while len(password) is not 8:
        # Encode our word plus our index and output hexadecimal representation
        md = md5(str(word + str(intdex)).encode('utf-8')).hexdigest()
        #password = md[:8] # completely unnecessary
        if md.startswith('00000'): # if the first five digits are zeroes
            print (time.time() - start)
            password +=  md[5] # add the 6th digit to our found password array

        # display our password
        #for i in range(len(found)):
            #password[i] = found[i]

        #stdout.write("\r" + password)
        #stdout.flush()
        intdex += 1
    return password

def part2():
    global start
    word = 'ffykfhsq'
    intdex = 0
    found = 0
    password = [ None ] * 8

    # While we have not found our 8 length password
    while True:
        # Encode our word plus our index and output hexadecimal representation
        md = md5(str(word + str(intdex)).encode('utf-8')).hexdigest()
        # if the first five digits are zeroes and from 0 to 7
        if md.startswith('00000') and (ord(md[5]) >= ord('0') and ord(md[5]) <= ord('7')):
            slot = int(md[5])
            if password[slot] is None:
                slot = int(md[5])
                password[slot] =  md[6] # add the 6th digit to our found password array
                found += 1
                print ("Found # {0} t={1:.3f} PASSWORD IS NOW: {2} added {3}".format(found, (time.time()-start), password, md[6]))
            if not None in password: # if we don't have any [None] in our array
                break
        intdex += 1
    return password