import re
import time

def part1():
    start = time.time()
    with open("in.txt") as file_in:
        arr = file_in.read().splitlines()

    proc = [re.findall("\d", x) for x in arr]

    total = sum(int(n[0] + n[-1]) for n in proc)  

    end = time.time()

    print(total)
    print(end-start)



def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    new_text, count = regex.subn(lambda mo: replacements[mo.group()], text)
    while count:
        new_text, count = regex.subn(lambda mo: replacements[mo.group()], new_text)
    return new_text



def part2():
    start = time.time()
    digits = {'one' : 'o1e',
              'two' : 't2o',
              'three' : 't3e',
              'four' : 'f4r',
              'five' : 'f5e',
              'six' : 's6x',
              'seven' : 's7n',
              'eight' : 'e8t',
              'nine' : 'n9e'}
    with open("in.txt") as file_in:
        arr = [multiple_replace(digits, x) for x in file_in.read().splitlines()]

    proc = [re.findall("\d", x) for x in arr]
    total = sum(int(n[0] + n[-1]) for n in proc)  

    end = time.time()

    print(total)
    print(end-start)

part1()
part2()
    