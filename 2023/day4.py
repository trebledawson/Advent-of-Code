def main():
    part_one()
    part_two()
    
    
def part_one():
    with open('day4-input.txt', 'r') as f:
        sum_of_points = 0
        for card in f:
            # Get matches per card
            winning = {int(n) for n in card[card.index(':')+1:card.index('|')].split(' ') if n != ''}  # Checked that winning numbers are unique, so set comprehension is faster than set(listcomp)
            my_nums = {int(n) for n in card[card.index('|')+1:].split(' ') if n != ''}  # My numbers are also unique
            
            # Get points per card
            sum_of_points += int(2 ** (len(winning.intersection(my_nums))-1))
            
        print(f'Part 1: {sum_of_points}')
    
    
def part_two():
    from collections import Counter
    
    with open('day4-input.txt', 'r') as f:
        card_counts = Counter()
        for card in f:
            # Get matches per card
            winning = {int(n) for n in card[card.index(':')+1:card.index('|')].split(' ') if n != ''}
            my_nums = {int(n) for n in card[card.index('|')+1:].split(' ') if n != ''}
            num_matches = len(winning.intersection(my_nums))
            
            # Track copies of cards
            card_id = int(card[card.index('d')+1:card.index(':')])
            card_counts[card_id] += 1
            for copy in range(card_counts[card_id]):
                for i in range(1, num_matches + 1):
                    card_counts[card_id + i] += 1
        
        print(f'Part 2: {card_counts.total()}')
        
            
if __name__ == '__main__':
    main()
