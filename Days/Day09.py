def moveHead(pos, dir) -> list[int,int]:
    match dir:
        case 'U':
            pos[0] += 1
        case 'D':
            pos[0] -= 1                
        case 'L':
            pos[1] -= 1
        case 'R':
            pos[1] += 1
    return pos

def moveTails(positions) -> list[list[int,int]]:
    for i, ((hy, hx), (ty, tx)) in enumerate(zip(positions, positions[1:])):
        if abs(hx - tx) > 1:
            tx += 1 if hx > tx else -1
            if abs(hy - ty) > 0:
                ty += 1 if hy > ty else -1
        elif abs(hy - ty) > 1:
            ty += 1 if hy > ty else -1
            if abs(hx - tx) > 0:
                tx += 1 if hx > tx else -1
        positions[i + 1][0] = ty
        positions[i + 1][1] = tx
    return positions

def simulate(motions, knots):
    positions = [[0, 0] for _ in range(knots)]
    tailVisited = set()
    
    for motion in motions:
        dir, steps = motion.split()
        for _ in range(int(steps)):
            tailVisited.add(tuple(positions[-1]))
            positions[0] = moveHead(positions[0], dir)
            positions = moveTails(positions)            

    tailVisited.add(tuple(positions[-1]))
    return len(tailVisited)

with open(f'Days\..\Inputs\Input09_2.txt') as inputFile:
    motions = inputFile.read().splitlines()
    print(simulate(motions, 1 + 1)) #6314
    print(simulate(motions, 1 + 9)) #2504