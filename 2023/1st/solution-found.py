import re
import time


### THIS SOLUTION WAS FOUND AT:
### https://github.com/fuglede/adventofcode/blob/master/2023/day01/solutions.py


def calibration(data):
    ls = data.split("\n")
    ns = [re.findall("\d", x) for x in ls]
    return sum(int(n[0] + n[-1]) for n in ns)



def part1():
    with open("in.txt") as f:
        data1 = f.read().strip()

    p1_start = time.time()

    p1_end = time.time()
    # Part 1
    print(calibration(data1))
    print(p1_end-p1_start)

# Part 2
def part2():
    p2_start = time.time()
    with open("in.txt") as f:
        data2 = f.read().strip()
    data2 = (
        data2.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    p2_end = time.time()
    print(calibration(data2))
    print(p2_end-p2_start)

