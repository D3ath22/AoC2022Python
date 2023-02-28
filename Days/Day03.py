def priority(item, islower) -> int:
    return item - ord('a') + 1 if islower else item - ord('A') + 27

with open(f'Days\..\Inputs\Input03_2.txt') as inputFile:
    rucksacks = inputFile.read().splitlines()
    print(sum(priority(ord(item), item.islower()) for items in rucksacks for item in set(items[:(len(items)//2)]) if item in set(items[(len(items)//2):]))) #7446
    print(sum(priority(ord(item), item.islower()) for i in range(0, len(rucksacks), 3) for item in set(rucksacks[i]) if item in rucksacks[i+1] and item in rucksacks[i+2])) #2646
   