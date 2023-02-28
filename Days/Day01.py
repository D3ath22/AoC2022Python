with open(f'Days\..\Inputs\Input01_2.txt') as inputFile:
    sortedTotalCaloriesPerElf = sorted([sum(map(int, calories.splitlines())) for calories in inputFile.read().split('\n\n')])
    print(sortedTotalCaloriesPerElf[-1]) #67027
    print(sum(sortedTotalCaloriesPerElf[-3:])) #197291