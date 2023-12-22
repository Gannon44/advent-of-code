import re
import time
from math import prod


class EngineCode:
    def __init__(self, _row, _col, _val_str="", _possible_activators=set(), _marked=False) -> None:
        self.val_str = _val_str
        self.possible_activators = _possible_activators
        self.marked = _marked
        self.row = _row
        self.col = _col

    def __str__(self) -> str:
        return f"EC at {self.getStartingLocation()} with value {self.getValStr()}"

    def append(self, val: str) -> None:
        self.val_str += val
        return

    def getVal(self) -> int:
        return int(self.val_str)
    
    def getValStr(self) -> str:
        return self.val_str
    
    def getValStrLen(self) -> str:
        return len(self.getValStr())
    
    def getActivators(self) -> set:
        return self.possible_activators
    
    def getStartingLocation(self) -> tuple:
        return (self.row, self.col)
    
    def isMarked(self) -> bool:
        return self.marked
    
    def calcPossibleActivators(self) -> None:
        possible = set()
        for i in range(-1, 2):
            for j in range(-1, self.getValStrLen()+1):
                possible.add((self.row + i, self.col + j))
        self.possible_activators = possible
        return
    
    def mark(self) -> None:
        self.marked = True
        return



not_symbols = set([x for x in "1234567890."])

def makeEngineCodes(text, row):
    codes = []
    idx = 0
    while idx < len(text):
        char = text[idx]
        if char.isdigit():
            new_code = EngineCode(row, idx, _val_str=char)
            idx += 1
            while idx < len(text):
                char = text[idx]
                if char.isdigit():
                    new_code.append(char)
                    idx += 1
                else:
                    idx += 1
                    break
            new_code.calcPossibleActivators()
            codes.append(new_code)
        else:
            idx += 1
    return codes
            

def part1():
    with open("in.txt") as file_in:
        arr = file_in.read().splitlines()
        
    codes = [makeEngineCodes(x, row) for row, x in enumerate(arr)]

    duplicate_total = 0

    for row, line in enumerate(arr):
        for col, char in enumerate(line):
            if char not in not_symbols:
                if row - 1 >= 0:
                    for code in codes[row - 1]:
                        if (row - 1, col) in code.getActivators():
                            code.mark()
                            # duplicate_total += code.getVal()
                if row + 1 <= len(codes):
                    for code in codes[row + 1]:
                        if (row + 1, col) in code.getActivators():
                            code.mark()
                            # duplicate_total += code.getVal()
                for code in codes[row]:
                        if (row, col) in code.getActivators():
                            code.mark()
                            # duplicate_total += code.getVal()
                

    total = 0
    for code_list in codes:
        for code in code_list:
            if code.isMarked():
                total += code.getVal()


    # print(duplicate_total)
    print(total)






def part2():
    with open("in.txt") as file_in:
        arr = file_in.read().splitlines()
        
    codes = [makeEngineCodes(x, row) for row, x in enumerate(arr)]

    gear_total = 0

    for row, line in enumerate(arr):
        for col, char in enumerate(line):
            if char == '*':
                gear_list = []
                if row - 1 >= 0:
                    for code in codes[row - 1]:
                        if (row - 1, col) in code.getActivators():
                            code.mark()
                            gear_list.append(code.getVal())
                            # duplicate_total += code.getVal()
                if row + 1 <= len(codes):
                    for code in codes[row + 1]:
                        if (row + 1, col) in code.getActivators():
                            code.mark()
                            gear_list.append(code.getVal())
                            # duplicate_total += code.getVal()
                for code in codes[row]:
                        if (row, col) in code.getActivators():
                            code.mark()
                            gear_list.append(code.getVal())
                            # duplicate_total += code.getVal()
                if len(gear_list) == 2:
                    gear_total += prod(gear_list)
                


    # print(duplicate_total)
    print(gear_total)

# part1()
part2()
    