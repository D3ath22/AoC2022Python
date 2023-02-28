from collections import deque
import math

def validNeighbor(y, x, ny, nx, heightmap, visited) -> bool:
    return (ny >= 0 and ny < len(heightmap)
        and nx >= 0 and nx < len(heightmap[0])
        and (ny, nx) not in visited
        and heightmap[ny][nx] <= heightmap[y][x] + 1)

def getNeighbors(y, x, heightmap, visited) -> list[(int, int)]:
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dy, dx in directions:
        ny, nx = y + dy, x + dx
        if validNeighbor(y, x, ny, nx, heightmap, visited):
            neighbors.append((ny, nx))
    return neighbors

def shortest_path(heightmap, start, end) -> int:
    visited = set([start])
    todo = deque([(start, 0)])
    while todo:
        (cy, cx), d = todo.popleft()
        for (ny, nx) in getNeighbors(cy, cx, heightmap, visited):
            if (ny, nx) == end:
                return d + 1
            visited.add((ny, nx))
            todo.append(((ny, nx), d + 1))            
    return math.inf

def makeHeightmap(input) -> list[list[list[int]], int, int]:
    heightmap = [[0] * len(input[0]) for i in range(len(input))]
    start = None
    end = None    
    starts = []
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == 'S':
                start = (y,x)
                heightmap[y][x] = 1
            elif input[y][x] == 'E':
                end = (y,x)
                heightmap[y][x] = 1 + ord('z') - ord('a')
            else:
                if input[y][x] == 'a':
                    starts.append((y,x))
                heightmap[y][x] = ord(input[y][x]) - ord('a') + 1
    return [heightmap, start, end, starts]

with open(f'Days\..\Inputs\Input12_2.txt') as inputFile:
    input = [[*line] for line in inputFile.read().splitlines()]
    heightmap, start, end, starts = makeHeightmap(input)
    print(shortest_path(heightmap, start, end))
    print(min([shortest_path(heightmap, s, end) for s in starts]))