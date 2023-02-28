from dataclasses import dataclass
import re
import copy
import math

@dataclass
class Monkey:
    items: list[int]
    operation: str
    divBy: int
    next: tuple[int, int]
    inspections : int

def getInts(string) -> list[int]:
    return list(map(int, re.findall(r"-?[0-9]+", string)))

def parseMonkeys(input) -> list[Monkey]:
    monkeys = []
  
    for monkeyData in input:
        monkeyLines = monkeyData.splitlines()

        items = getInts(monkeyLines[1])
        operation = monkeyLines[2].split(' = ')[-1]
        divBy = getInts(monkeyLines[3])[0]
        next = (getInts(monkeyLines[4])[0], getInts(monkeyLines[5])[0])

        monkeys.append(Monkey(items, operation, divBy, next, 0))
    
    return monkeys

def simulateRounds(monkeys, rounds, veryWorried, commonDiv):
    for _ in range(rounds):
        monkeys = simulateRound(monkeys, veryWorried, commonDiv)
    
    monkeys.sort(key = lambda m: m.inspections, reverse=True)

    return monkeys[0].inspections * monkeys[1].inspections

def simulateRound(monkeys, veryWorried, commonDiv) -> list[Monkey]:
    for i in range(len(monkeys)):
        for old in monkeys[i].items:
            monkeys[i].inspections += 1
            worry = eval(monkeys[i].operation)
            worry = worry // 3 if not veryWorried else worry % commonDiv
            divisible = worry % monkeys[i].divBy != 0
            monkeys[monkeys[i].next[divisible]].items.append(worry)
        monkeys[i].items.clear()
    return monkeys

with open(f'Days\..\Inputs\Input11_2.txt') as inputFile:
    input = inputFile.read().split('\n\n')
    monkeys = parseMonkeys(input)
    commonDiv = math.prod(m.divBy for m in monkeys)
    print(simulateRounds(copy.deepcopy(monkeys), 20, False, commonDiv)) #99840
    print(simulateRounds(monkeys, 10000, True, commonDiv)) #20683044837