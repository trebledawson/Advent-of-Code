from timeit import default_timer as timer
from math import sqrt


def main():
    """
    Let D be an integer representing the distance record for time T, and let
    f(Z) be a function defined on integers such that f(z) = z * (t - z). We 
    are interested in the number of integers for which f(T) > D. This value 
    can be found by finding the difference between the integer roots of 
    f(z) = D, so 
        
        D = z * (t - z).                                                 (1)
    
    Expanding into standard form yields 
    
        0 = -(z ** 2) + tz - D.                                          (2)
    
    Solving the quadratic equation as usual and finding the integer 
    difference between the roots yields the solution.
    """
    
    start = timer()
    part_one()
    print(f'Time: {timer() - start} seconds.')
    
    start = timer()
    part_two()
    print(f'Time: {timer() - start} seconds.')
    
    
def part_one():
    filename = 'day6-input.txt'
    times, distances = parse_input(filename)
    
    product_of_winning_ways = 1
    for time, distance in zip(times, distances):
        root_one = int((time - sqrt((time ** 2) - (4 * distance))) / 2)
        root_two = int((time + sqrt((time ** 2) - (4 * distance))) / 2)
        product_of_winning_ways *= (root_two - root_one)
    
    print(f'Part 1: {product_of_winning_ways}')
        
    
def part_two():
    filename = 'day6-input.txt'
    times, distances = parse_input(filename)
    time = int(''.join([str(t) for t in times]))
    distance = int(''.join([str(d) for d in distances]))
    root_one = int((time - sqrt((time ** 2) - (4 * distance))) / 2)
    root_two = int((time + sqrt((time ** 2) - (4 * distance))) / 2)
    
    print(f'Part 2: {root_two - root_one}')
    
    
def parse_input(filename):
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i == 0:
                times = [int(time.strip()) for time in line[9:].split(' ') if time != '']
            else:
                distances = [int(distance.strip()) for distance in line[9:].split(' ') if distance != '']
    
    return times, distances
    
    
if __name__ == '__main__':
    main()
