import math

def parseDirection(trees, tree, y, x, range, ny, nx) -> list[bool, int]: 
    visibility = True
    score = 0
    y = y * nx
    x = x * ny
    for i in range:
        score += 1
        if trees[y + ny * i][x + nx * i] >= tree:
            visibility = False
            break
    return [visibility, score]

def parseTree(trees, y, x) -> list[bool, int]:
    tree = trees[y][x]
    visibility = []
    scores = []
    directions = [
        [range(y - 1, -1, -1), 1, 0],
        [range(y + 1, len(trees)), 1, 0],
        [range(x - 1, -1, -1), 0, 1],
        [range(x + 1, len(trees[0])), 0, 1],
    ]
    for direction in directions:
        nVisibility, nScore = parseDirection(trees, tree, y, x, direction[0], direction[1], direction[2])
        visibility.append(nVisibility)
        scores.append(nScore)

    return [True in visibility, math.prod(scores)]

with open(f'Days\..\Inputs\Input08_2.txt') as inputFile:
    trees = [list(map(int, row)) for row in inputFile.read().splitlines()]
    count = 2 * len(trees) + 2 * len(trees[0]) - 4
    maxScore = 0
    for y in range(1, len(trees) - 1):
        for x in range(1, len(trees[0]) - 1):
            visible, score = parseTree(trees, y, x)
            count += visible
            maxScore = max(maxScore, score)
    print(count) #1796
    print(maxScore) #288120