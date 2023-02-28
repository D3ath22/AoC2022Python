import re
import copy

def makeStacks(data) -> list[list[str]]:
    crateDistance = 4 #[M] [S]
    stacksLen = int(data[data.index('') - 1].split(' ')[-2])    # 1   2   3   4   5   6   7   8   9 -> 9
    stacks = [[] for _ in range(stacksLen)] 
    for lineIndex in range(data.index('') - 1, -1, -1): #[G]     [P] [C] [F] [G] [T]   reversed     
        for charIndex in range(0, len(data[0])):
            if data[lineIndex][charIndex].isalpha():    #G is a crate
                stackIndex = int((1 + charIndex) / crateDistance)
                stacks[stackIndex].append(data[lineIndex][charIndex])
    return stacks

def applyProcedures(stacks, procedures, crateMover9000) -> list[list[str]]:
    for procedure in procedures:
        crates = [stacks[procedure[1] - 1].pop() for _ in range(0, procedure[0])]
        if not crateMover9000:
            crates.reverse()
        stacks[procedure[2] - 1].extend(crates)   
    return stacks

def cratesOnTop(stacks) -> str:
    return ''.join(stack[-1] for stack in stacks)

with open(f'Days\..\Inputs\Input05_2.txt') as inputFile:
    data = inputFile.read().splitlines()
    stacks = makeStacks(data)
    procedures = [list(map(int, re.findall(r'(\d+)', procedure))) for procedure in data[data.index('') + 1:]] #move 1 from 7 to 4 -> [1,7,4]
    print(cratesOnTop(applyProcedures(copy.deepcopy(stacks), procedures, True))) #TLNGFGMFN
    print(cratesOnTop(applyProcedures(stacks, procedures, False))) #FGLQJCMBD
