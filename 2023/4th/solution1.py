import re


def part1():
    with open("in.txt") as file_in:
        arr = [x.split(': ')[1].strip() for x in file_in.read().splitlines()]

    winners = [re.findall('\d+', x.split(' | ')[0]) for x in arr]
    numbers = [re.findall('\d+', x.split(' | ')[1]) for x in arr]

    total = 0
    for idx, win in enumerate(winners):
        playble = set(numbers[idx])
        count = 0
        for num in win:
            if num in playble:
                if count == 0:
                    count += 1
                else:
                    count *= 2
        total += count

    print(total)






def part2():
    with open("in.txt") as file_in:
        arr = [x.split(': ')[1].strip() for x in file_in.read().splitlines()]

    winners = [re.findall('\d+', x.split(' | ')[0]) for x in arr]
    numbers = [re.findall('\d+', x.split(' | ')[1]) for x in arr]
    card_counts = [1 for _ in arr]

    total = 0
    for idx, win in enumerate(winners):
        for counter in range(card_counts[idx]):
            playble = set(numbers[idx])
            count = 0
            for num in win:
                if num in playble:
                    count += 1
            for i in range(count):
                if i+idx+1 < len(card_counts):
                    card_counts[i+idx+1] += 1
                else:
                    break

    # print(card_counts)
    print(sum(card_counts))



# part1()
part2()
    