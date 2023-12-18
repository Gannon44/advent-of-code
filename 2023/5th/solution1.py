import re


def part1():
    with open("test12.txt") as file_in:
        arr = file_in.read().splitlines()

    arr = list(map(lambda x: re.sub(r'[\D]', '', x), arr))

    total = 0
    for string in arr:
        total += int(string[0]+string[-1])     

    print(total)






def part2():
    with open("test2.txt") as file_in:
        arr = file_in.read().splitlines()

    print(arr)
    arr = list(map(lambda x: re.sub(r'[\D]', '', x), arr))

    total = 0
    for string in arr:
        total += int(string[0]+string[-1])     
    print(total)

part1()
#part2()
    