import re
import numpy



def lookup(key, unparsed_map):
    for item in unparsed_map:
        entry = item.split()
        source = int(entry[1])
        dest = int(entry[0])
        map_range = int(entry[2])
        if key >= source and key < (source + map_range):
            return key + (dest - source)
    return key




def part1():
    with open("in.txt") as file_in:
        arr = file_in.read().split('\n\n')
        arr = [x.split('\n') for x in arr]

    # u = unparsed
    seeds = arr[0][0].strip('seeds: ').split()
    u_seed2soil = arr[1][1:]
    u_soil2fert = arr[2][1:]
    u_fert2watr = arr[3][1:]
    u_watr2lite = arr[4][1:]
    u_lite2temp = arr[5][1:]
    u_temp2humd = arr[6][1:]
    u_humd2locn = arr[7][1:]

    min_locn = float("inf")
    for seed in seeds:
        soil = lookup(int(seed), u_seed2soil)
        fert = lookup(soil, u_soil2fert)
        watr = lookup(fert, u_fert2watr)
        lite = lookup(watr, u_watr2lite)
        temp = lookup(lite, u_lite2temp)
        humd = lookup(temp, u_temp2humd)
        locn = lookup(humd, u_humd2locn)
        min_locn = min(min_locn, locn)

    print(min_locn)




def lowest(a, n): 
    return numpy.partition(a, n-1)[:n]

def part2():
    with open("in.txt") as file_in:
        arr = file_in.read().split('\n\n')
        arr = [x.split('\n') for x in arr]

    # u = unparsed
    u_seeds = arr[0][0].strip('seeds: ').split()
    seeds = []
    for idx in range(0, len(u_seeds), 2):
        seeds.append((u_seeds[idx], u_seeds[idx+1]))

    u_seed2soil = arr[1][1:]
    u_soil2fert = arr[2][1:]
    u_fert2watr = arr[3][1:]
    u_watr2lite = arr[4][1:]
    u_lite2temp = arr[5][1:]
    u_temp2humd = arr[6][1:]
    u_humd2locn = arr[7][1:]
    
    locations = []
    for seed_range in seeds:
        min_locn = (0, float("inf"))
        for seed in range(int(seed_range[0]), int(seed_range[0]) + int(seed_range[1]), 100000):
            soil = lookup(seed, u_seed2soil)
            fert = lookup(soil, u_soil2fert)
            watr = lookup(fert, u_fert2watr)
            lite = lookup(watr, u_watr2lite)
            temp = lookup(lite, u_lite2temp)
            humd = lookup(temp, u_temp2humd)
            locn = lookup(humd, u_humd2locn)
            # locations.append((seed, locn))
            min_locn = min([min_locn, (seed, locn)], key = lambda t: t[1])
        locations.append(min_locn)
    # print(locations)

    new_list = []
    min_of_all = (0, float("inf"))
    for seed_loc in locations:
        old_min_seed = seed_loc[0]
        for i in range(5):
            base = int(100000 / pow(10, i))
            new_offset = int(base / 10)
            min_locn = (0, float("inf"))

            for offset in range(-base, base, new_offset):
                seed = old_min_seed + offset
                soil = lookup(seed, u_seed2soil)
                fert = lookup(soil, u_soil2fert)
                watr = lookup(fert, u_fert2watr)
                lite = lookup(watr, u_watr2lite)
                temp = lookup(lite, u_lite2temp)
                humd = lookup(temp, u_temp2humd)
                locn = lookup(humd, u_humd2locn)
                min_locn = min([min_locn, (seed, locn)], key = lambda t: t[1])
            old_min_seed = min_locn[0]
        new_list.append(min_locn)
    print(min(new_list, key = lambda t: t[1])[1])





# part1()
part2()
    





### ORIGINAL APPROACH
### PROCESS KILLED
# def make_map(unparsed_map):
#     new_map = {}
#     for item in unparsed_map:
#         entry = item.split()
#         source = int(entry[1])
#         dest = int(entry[0])
#         map_range = int(entry[2])
#         new_map.update(dict(zip(range(source, source+map_range), range(dest, dest+map_range))))
#     return new_map

# def lookup(item, map):
#     if item in map:
#         return map[item]
#     else:
#         return item

### GOES IN PART1()
    # seed2soil = make_map(u_seed2soil)
    # soil2fert = make_map(u_soil2fert)
    # fert2watr = make_map(u_fert2watr)
    # watr2lite = make_map(u_watr2lite)
    # lite2temp = make_map(u_lite2temp)
    # temp2humd = make_map(u_temp2humd)
    # humd2locn = make_map(u_humd2locn)

    # min_locn = float("inf")
    # for seed in seeds:
        # soil = lookup(int(seed), seed2soil)
        # fert = lookup(soil, soil2fert)
        # watr = lookup(fert, fert2watr)
        # lite = lookup(watr, watr2lite)
        # temp = lookup(lite, lite2temp)
        # humd = lookup(temp, temp2humd)
        # locn = lookup(humd, humd2locn)
        # min_locn = min(min_locn, soil)