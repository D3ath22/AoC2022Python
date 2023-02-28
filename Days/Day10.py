import numpy as np

def makeCycles(program) -> list[int]:
    cycles = [] 
    pending = None

    for instruction in program:
        if pending is None:
            cycles.append(0)
        else:
            cycles.append(pending)
        pending = None
        if instruction.startswith('addx'):
            cycles.append(0)
            pending = int(instruction.split(' ')[1])
    
    return cycles

def sumSignalStrength(cycles) -> int:
    step = 40
    register = 1
    result = 0
    
    for i in range(20, 220 + 1, step):
        if i == 20:
            cycleSum = sum(cycles[:20])
        else:
            cycleSum = sum(cycles[i - step : i])
        register = register + cycleSum
        result += i * register

    return result

def drawPixels(cycles) -> list[list[str]]:
    register = 1
    screen = []
    pixelLit = '#'
    pixelDark = '.'    
    drawPos = 0
    row = []

    for i in range(0, len(cycles)):
        register += cycles[i]
        if drawPos in range(register - 1, register + 2):
            row.append(pixelLit)
        else:
            row.append(pixelDark)
        drawPos += 1
        if drawPos > 0 and (drawPos % 40 == 0):
            screen.append(row)
            row = []            
            drawPos = 0 

    return screen

with open(f'Days\..\Inputs\Input10_2.txt') as inputFile:
    program = inputFile.read().splitlines()
    cycles = makeCycles(program)
    print(sumSignalStrength(cycles)) #14320    
    np.set_printoptions(linewidth=np.inf)
    print(np.matrix(drawPixels(cycles))) #PCPBKAPJ