import re
import time


def parse1(game):
    number, game = game.split(': ')
    subGames = game.split(';')
    for match in subGames:
        handful = match.split(',')
        vals = {'r' : 0,    # vals holds the counters for each color for each match
                'g' : 0,
                'b' : 0}
        for cubes in handful:
            color = cubes.strip().split(' ', )
            vals[color[1][0]] += int(color[0])
            if vals['r'] > 12 or vals['g'] > 13 or vals['b'] > 14:
                return 0 # this stores 0 on fail
    return int(number.split(' ')[1]) # this stores game number on success


def part1():
    start = time.time()
    with open("in.txt") as file_in:
        arr = [parse1(x) for x in file_in.read().splitlines()]

    total = sum(arr) # sum up all game numbers that passed
    end = time.time()

    print(total)
    print(end-start)




def parse2(game):
    number, game = game.split(': ')
    subGames = game.split(';')
    power = {'r' : 1,   # power holds the counters for the minimum number of each color for each game
             'g' : 1,   # defaulted to 1 because we will multiply these
             'b' : 1}
    for match in subGames:
        handful = match.split(',')
        vals = {'r' : 0,    # vals holds the counters for each color for each match
                'g' : 0,
                'b' : 0}
        for cubes in handful:            
            color = cubes.strip().split(' ')
            vals[color[1][0]] += int(color[0])
        power['r'] = max(power['r'], vals['r'])
        power['g'] = max(power['g'], vals['g'])
        power['b'] = max(power['b'], vals['b'])
    return power['r'] * power['g'] * power['b']



def part2():
    start = time.time()
    with open("in.txt") as file_in:
        arr = [parse2(x) for x in file_in.read().splitlines()]

    total = sum(arr)
    end = time.time()
    
    print(total)
    print(end-start)

part1()
part2()
    