import re


def part1():
    with open("in.txt") as file_in:
        arr = file_in.read().splitlines()

    arr = list(map(lambda x: re.sub(r'[\D]', '', x), arr))

    total = 0
    for string in arr:
        total += int(string[0]+string[-1])     

    print(total)



def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    new_text, count = regex.subn(lambda mo: replacements[mo.group()], text)
    while count:
        new_text, count = regex.subn(lambda mo: replacements[mo.group()], new_text)
    return new_text



def part2():
    digits = {'one' : 'o1e',
              'two' : 't2o',
              'three' : 't3e',
              'four' : 'f4r',
              'five' : 'f5e',
              'six' : 's6x',
              'seven' : 's7n',
              'eight' : 'e8t',
              'nine' : 'n9e'}
    with open("in1.txt") as file_in:
        arr = [multiple_replace(digits, x) for x in file_in.read().splitlines()]

    print(arr)
    arr = list(map(lambda x: re.sub(r'[\D]', '', x), arr))

    total = 0
    for string in arr:
        total += int(string[0]+string[-1])     
    print(total)

part2()
    