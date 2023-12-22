import re
import numpy as np
from math import ceil


def part1():
    with open("in.txt") as file_in:
        arr = file_in.read().splitlines()
    races = list(zip(map(int, re.findall("\d+", arr[0].strip("Time:   "))), map(int, re.findall("\d+", arr[1].strip("Distance: ")))))

    total = 1
    for race in races:
        t, d = race
        roots = np.roots([-1, t, -d])
        ways2win = ceil(roots[0])-(ceil(roots[1]) if not roots[1].is_integer() else int(roots[1])+1)
        total *= ways2win
    print(total)





def part2():
    with open("in.txt") as file_in:
        arr = file_in.read().splitlines()
    race = (int(re.sub(" ", "", arr[0].strip("Time:   "))), int(re.sub(" ", "", arr[1].strip("Distance: "))))

    t, d = race
    roots = np.roots([-1, t, -d])
    ways2win = ceil(roots[0])-(ceil(roots[1]) if not roots[1].is_integer() else int(roots[1])+1)

    print(ways2win)

# part1()
part2()
    