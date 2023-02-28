def findMarker(markerSize) -> int:
    for i in range(0, len(data) - markerSize):
        if len(set(data[i : i + markerSize])) == markerSize:
            return i + markerSize
    return -1

with open(f'Days\..\Inputs\Input06_2.txt') as inputFile:
    data = inputFile.read().splitlines()[0]
    markerSize = 4    
    print(findMarker(markerSize)) #1816
    markerSize = 14
    print(findMarker(markerSize)) #1816