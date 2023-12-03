def main():
    part_one()
    part_two()
    
    
def part_one():
    bag = {'red': 12,
           'green': 13,
           'blue': 14}
    with open('day2-input.txt', 'r') as f:
        ids = 0
        for game in f.readlines():
            game_id = int(game[game.index(' ')+1:game.index(':')])
            game = game[game.index(':')+1:]
            
            end_game = False  # Flag for impossible game
            
            # First N-1 grabs in game
            while ';' in game:
                idx = game.index(';')
                grab = game[:idx]
                for color in bag:
                    if color in grab:
                        idx = grab.index(color)
                        if int(grab[idx-3:idx]) > bag[color]:
                            end_game = True
                            break
                if end_game:
                    break
                game = game[game.index(';')+1:]
            if end_game:
                continue
            
            # Last grab in game
            for color in bag:
                if color in game:
                    idx = game.index(color)
                    if int(game[idx-3:idx]) > bag[color]:
                        end_game = True
                        break        
            
            # If last grab not illegal, add game_id to sum
            if not end_game:
                ids += game_id
                
        print(f'Part 1: {ids}')
                
    
def part_two():
    with open('day2-input.txt', 'r') as f:
        sum_of_powers = 0
        for game in f.readlines():
            game = game[game.index(':')+1:]
            
            # Set minimums to 1 for easier power calculation later
            bag = {'red': 1,
                   'green': 1,
                   'blue': 1}
            power = 1
                   
            # First N-1 grabs in game
            while ';' in game:
                idx = game.index(';')
                grab = game[:idx]
                for color in bag:
                    if color in grab:
                        idx = grab.index(color)
                        if int(grab[idx-3:idx]) > bag[color]:
                            bag[color] = int(grab[idx-3:idx])
                game = game[game.index(';')+1:]
            
            # Last grab in game
            for color in bag:
                if color in game:
                    idx = game.index(color)
                    if int(game[idx-3:idx]) > bag[color]:
                            bag[color] = int(game[idx-3:idx])
                power *= bag[color]
            
            sum_of_powers += power
            
        print(f'Part 2: {sum_of_powers}')
            
    
def parse_game(line):
    game = dict()
    
    
if __name__ == '__main__':
    main()
