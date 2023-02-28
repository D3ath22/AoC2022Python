def contained(assignment) -> bool:
    return (assignment[0] >= assignment[2] and assignment[1] <= assignment[3]) or (assignment[0] <= assignment[2] and assignment[1] >= assignment[3])

def overlaped(assignment) -> bool:
    return max(assignment[0], assignment[2]) <= min(assignment[1], assignment[3])

with open(f'Days\..\Inputs\Input04_2.txt') as inputFile:
    assignments = [[int(pair[0].split('-')[0]), int(pair[0].split('-')[1]), int(pair[1].split('-')[0]), int(pair[1].split('-')[1])] for pair in [assignment.split(',') for assignment in inputFile.read().splitlines()]]
    print(sum(contained(assignment) for assignment in assignments)) #513
    print(sum(overlaped(assignment) for assignment in assignments)) #878