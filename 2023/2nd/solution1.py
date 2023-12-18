import re


def parse1(game):
    number, game = game.split(': ')
    subGames = game.split(';')
    for i in subGames:
        handful = i.split(',')
        vals = {'r' : 0,
                'g' : 0,
                'b' : 0}
        for j in handful:
            k = j.strip().split(' ', )
            vals[k[1][0]] += int(k[0])
            if vals['r'] > 12 or vals['g'] > 13 or vals['b'] > 14:
                return 0
    return int(number.split(' ')[1])


def part1():
    with open("in.txt") as file_in:
        arr = [parse1(x) for x in file_in.read().splitlines()]

    total = sum(arr)

    print(total)




def parse2(game):
    number, game = game.split(': ')
    subGames = game.split(';')
    power = {'r' : 1,
             'g' : 1,
             'b' : 1}
    for i in subGames:
        handful = i.split(',')
        vals = {'r' : 0,
                    'g' : 0,
                    'b' : 0}
        for j in handful:            
            k = j.strip().split(' ')
            vals[k[1][0]] += int(k[0])
        power['r'] = max(power['r'], vals['r'])
        power['g'] = max(power['g'], vals['g'])
        power['b'] = max(power['b'], vals['b'])
    print(power)
    return power['r'] * power['g'] * power['b']



def part2():
    with open("in.txt") as file_in:
        arr = [parse2(x) for x in file_in.read().splitlines()]

    total = sum(arr)

    print(total)

part1()
part2()
    