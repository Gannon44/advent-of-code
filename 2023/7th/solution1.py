import re


def multiple_replace(replacements, text):
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, replacements.keys())))
    # For each match, look-up corresponding value in dictionary
    new_text = regex.sub(lambda mo: replacements[mo.group()], text)
    return new_text


def findRank1(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    char_counts = sorted(char_counts.values(), reverse=True)
    if len(char_counts) == 1:
        return 1
    elif len(char_counts) == 2 and char_counts[0] == 4:
        return 2
    elif len(char_counts) == 2 and char_counts[0] == 3:
        return 3
    elif len(char_counts) == 3 and char_counts[0] == 3:
        return 4
    elif len(char_counts) == 3 and char_counts[0] == 2:
        return 5
    elif len(char_counts) == 4:
        return 6
    else:
        return 7

def part1():

    new_order = {'A':'m', 'K':'l', 'Q':'k', 'J':'j', 
                 'T':'i', '9':'h', '8':'g', '7':'f', 
                 '6':'e', '5':'d', '4':'c', '3':'b', '2':'a'}    

    with open("in.txt") as file_in:
        arr = [x.split(" ") for x in file_in.read().splitlines()]
    
    for idx in range(len(arr)):
        arr[idx] = (multiple_replace(new_order, arr[idx][0]), int(arr[idx][1]), arr[idx][0])

    in_rank = sorted(arr, key=lambda x: (-findRank1(x[0]), x[0]), reverse=False)
    # print(*in_rank, sep="\n")

    total = 0
    for idx, hand in enumerate(in_rank):
        total += hand[1]*(idx+1)

    print(total)







def findRank2(string):
    char_counts = {}
    for char in string:
        if char == 'a':
            continue
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    char_counts = sorted(char_counts.values(), reverse=True)
    if len(char_counts) == 0:
        char_counts.append(5)
    else:
        char_counts[0] += 5-sum(char_counts)    
    if len(char_counts) == 1:
        return 1
    elif len(char_counts) == 2 and char_counts[0] == 4:
        return 2
    elif len(char_counts) == 2 and char_counts[0] == 3:
        return 3
    elif len(char_counts) == 3 and char_counts[0] == 3:
        return 4
    elif len(char_counts) == 3 and char_counts[0] == 2:
        return 5
    elif len(char_counts) == 4:
        return 6
    else:
        return 7

def part2():
    
    new_order = {'A':'m', 'K':'l', 'Q':'k', 'J':'a', 
                 'T':'j', '9':'i', '8':'h', '7':'g', 
                 '6':'f', '5':'e', '4':'d', '3':'c', '2':'b'}

    with open("in.txt") as file_in:
        arr = [x.split(" ") for x in file_in.read().splitlines()]
    
    for idx in range(len(arr)):
        arr[idx] = (multiple_replace(new_order, arr[idx][0]), int(arr[idx][1]), arr[idx][0])

    in_rank = sorted(arr, key=lambda x: (-findRank2(x[0]), x[0]), reverse=False)
    # print(*in_rank, sep="\n")

    total = 0
    for idx, hand in enumerate(in_rank):
        total += hand[1]*(idx+1)

    print(total)





# part1()
part2()
    