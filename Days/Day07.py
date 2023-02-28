from collections import defaultdict

with open(f'Days\..\Inputs\Input07_2.txt') as inputFile:
    terminal = inputFile.read().splitlines()
    maxSize = 100000
    dirSizes = defaultdict(int)
    dirs = []
    for output in terminal:
        output = output.split(' ')
        if output[0] == '$':
            if output[1] == 'cd':
                match output[2]:
                    case '/': 
                        dirs.clear()
                    case '..':
                        dirs.pop()
                    case other:
                        dirs.append(other)
        elif output[0].isnumeric():
            for i in range(len(dirs) + 1):
                path = '/' + '/'.join(dirs[:i])
                dirSizes[path] += int(output[0])
            
    print(sum(dirSize for dirSize in dirSizes.values() if dirSize <= maxSize)) #1770595  

    total = 70_000_000
    minUnused = 30_000_000
    needed = minUnused - (total - dirSizes['/'])
    print(min(dirSize for dirSize in dirSizes.values() if dirSize > needed)) #2195372