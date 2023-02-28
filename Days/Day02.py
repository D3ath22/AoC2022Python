resultMatrixOne = [ #rps[me] rps[enemy]
    [4, 1, 7], 
    [8, 5, 2],
    [3, 9, 6],
]
resultMatrixTwo = [ #ldw[me] rps[enemy]
    [3, 1, 2], 
    [4, 5, 6],
    [8, 9, 7],
]
with open(f'Days\..\Inputs\Input02_2.txt') as inputFile:
    rounds = inputFile.readlines()
    print(sum(resultMatrixOne[ord(round[2]) - ord('X')][ord(round[0]) - ord('A')] for round in rounds)) #10816
    print(sum(resultMatrixTwo[ord(round[2]) - ord('X')][ord(round[0]) - ord('A')] for round in rounds)) #11657