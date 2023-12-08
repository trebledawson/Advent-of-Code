from timeit import default_timer as timer
from math import lcm


def main():
    start = timer()
    part_one()
    print(f'Time: {timer() - start} seconds')
    
    start = timer()
    part_two()
    print(f'Time: {timer() - start} seconds')
    
def part_one():
    filename = 'day8-input.txt'
    instructions, nodes = parse_map(filename)
    
    node = 'AAA'
    target = 'ZZZ'
    
    steps = 0
    while node != target:
        for instruction in instructions:
            node = nodes[node][instruction]
            steps += 1
            if node == target:
                break
                
    print(f'Part 1: {steps}')
    
    
def part_two():
    filename = 'day8-input.txt'
    instructions, nodes = parse_map(filename)
    
    lcm_of_steps = 1
    for node in nodes:
        if node[-1] != 'A':
            continue
        steps = 0
        while node[-1] != 'Z':
            for instruction in instructions:
                node = nodes[node][instruction]
                steps += 1
                if node[-1] == 'Z':
                    break
        lcm_of_steps = lcm(lcm_of_steps, steps)
        
    print(f'Part 2: {lcm_of_steps}')
    
    
def parse_map(filename):
    nodes = dict()
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i > 1:
                nodes[line[:line.index('=')-1]] = (line[line.index('=')+1:][2:5], line[line.index('=')+1:][-5:-2])
            elif i == 0:
                instructions = []
                for direction in line.strip():
                    instructions.append(0 if direction == 'L' else 1)
                
    return instructions, nodes

    
if __name__ == '__main__':
    main()
