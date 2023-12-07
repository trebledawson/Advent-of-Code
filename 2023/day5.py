from timeit import default_timer as timer


def main():
    start = timer()
    part_one()
    print(f'Time: {timer() - start} seconds.')
    
    start = timer()
    part_two()
    print(f'Time: {timer() - start} seconds.')
    
    
def part_one():
    filename = 'day5-input.txt'
    seeds, maps = parse_almanac(filename)
    location = pass_through_maps(seeds, maps)
        
    print(f'Part 1: {location}')
                
                
def part_two():
    """
    Each map is a piecewise function. Taking only the final map, because each piece of each function
    is increasing monotonically, we need only to check the lowermost boundary  of each piece. Moving 
    back to the second-to-last map, we need to find the inverse image of these boundaries, and combine 
    with the boundaries of this map. Continue all the way to the first map, then find the candidate 
    seeds that lie in the valid ranges of seeds. Finally, pass these valid test seeds through the maps
    in order to find the minimum location by brute force. 
    """
    filename = 'day5-input.txt'
    seeds, maps = parse_almanac(filename)
    
    # First, get candidate seeds by running backward through the maps
    candidate_seeds = {0}  # Start with lower bound of 0. Can think of as "location-to-location" map [0, inf)
    for map_type in reversed(maps):
        new_seeds = set()  # For storing candidates from this map
        high = 0  # This is to find the lower bound of the highest range, [high, inf)
        
        for map_range in maps[map_type]:
            found = set()  # Store set of found seeds to find those not modified by map
            for seed in candidate_seeds:
                # Inverse image of output boundaries. Should only occur once per output
                if maps[map_type][map_range][0] <= seed < maps[map_type][map_range][1]:
                    new_seeds.add(seed - maps[map_type][map_range][2])  # Map is source + diff = destination
                    found.add(seed)
            candidate_seeds -= found  # Remove found seeds from candidates
            
            # Check if new highest lower bound
            if map_range[1] + 1 > high:
                high = map_range[1] + 1
                
            new_seeds.add(map_range[0])  # Add lower bounds of all given ranges
        new_seeds.add(high)  # Add lower bound of highest range, i.e. [high, inf)
        
        # Seeds not found in non-idempotent ranges map to themselves
        new_seeds.update(candidate_seeds)
        
        candidate_seeds = new_seeds  # Replace candidates
        
    # Now, find the candidate seeds that lie in the seed ranges, including seed range lower bounds
    test_seeds = {seeds[0]}
    while len(seeds) > 0:    
        seeds_in_range = {seed for seed in candidate_seeds if seeds[0] <= seed < seeds[0] + seeds[1]}
        test_seeds.update(seeds_in_range)
        candidate_seeds -= seeds_in_range
        test_seeds.add(seeds[0])
        seeds = seeds[2:]     
    
    # Finally, pass the test seeds through the maps to find the smallest location
    location = pass_through_maps(test_seeds, maps)
        
    print(f'Part 2: {location}')
    
    
def parse_almanac(filename):
    maps = dict()
    current_map = None
    with open(filename, 'r') as f:
        for i, line in enumerate(f):
            if i > 0:
                if line[0].isdigit():  # Create map entry. Cannot fire before new_map is created
                    dest, src, rng = [int(n.strip()) for n in line.split(' ')]
                    new_map[(src, src + rng)] = (dest, dest + rng, dest - src)
                elif len(line) > 1:  # Set current map if line is not empty
                    current_map = line[:-6]   
                    new_map = dict()            
                elif current_map is not None:  # Empty line after map signifies map is complete
                    maps[current_map] = new_map
            elif i == 0:  # Get list of seeds
                seeds = [int(seed.strip()) for seed in line.split(' ')[1:]]                    
        else:  # Write last map, no newline at end of file
            maps[current_map] = new_map
    return seeds, maps


def pass_through_maps(seeds, maps):
    location = float('inf')
    for seed in seeds:
        for map_type in maps:
            for map_range in maps[map_type]:
                if map_range[0] <= seed < map_range[1]:
                    seed = maps[map_type][map_range][0] - map_range[0] + seed
                    break
        if seed < location:
            location = seed
            
    return location


if __name__ == '__main__':
    main()
