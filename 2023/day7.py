from timeit import default_timer as timer
from collections import defaultdict


def main():    
    start = timer()
    part_one()
    print(f'Time: {timer() - start} seconds.')
    
    start = timer()
    part_two()
    print(f'Time: {timer() - start} seconds.')
    
    
def part_one():
    filename = 'day7-input.txt'
    hands = parse_hands(filename)
    
    # Rank hands by counting instances of unique cards in each hand
    hands_by_type = defaultdict(list)
    for hand in hands:
        hand_dict = defaultdict(int)
        for card in hand:
            hand_dict[card] += 1
        
        if len(hand_dict) == 1:
            hands_by_type['6 five of a kind'].append((hand, hands[hand]))
        elif len(hand_dict) == 2:
            for card in hand_dict:
                if hand_dict[card] in [1, 4]:
                    hands_by_type['5 four of a kind'].append((hand, hands[hand]))
                else:
                    hands_by_type['4 full house'].append((hand, hands[hand]))
                break
        elif len(hand_dict) == 3:
            for card in hand_dict: 
                if hand_dict[card] == 3:
                    hands_by_type['3 three of a kind'].append((hand, hands[hand]))
                    break
            else:
                hands_by_type['2 two pair'].append((hand, hands[hand]))
        elif len(hand_dict) == 4:
                hands_by_type['1 one pair'].append((hand, hands[hand]))
        else:  # len(hand_dict) == 5:
                hands_by_type['0 high card'].append((hand, hands[hand]))
    
    # Rank hands in type using custom sorting dict to go through each card in each hand,
    # starting with the lowest-value hands. Keep a running counter of hands and the running
    # sum (winnings) as we go. 
    card_values = {
        '2': 0,
        '3': 1,
        '4': 2,
        '5': 3,
        '6': 4,
        '7': 5,
        '8': 6,
        '9': 7,
        'T': 8,
        'J': 9,
        'Q': 10,
        'K': 11,
        'A': 12
    }
    rank = 1
    winnings = 0
    for hand_type in sorted(hands_by_type.keys()):
        hands_by_card = dict()
        for card_type in card_values:
            hands_by_card[card_type] = sorted([hand for hand in hands_by_type[hand_type] if hand[0][0] == card_type], 
                                              key=lambda hand: card_values[hand[0][0][0]])
        for i in range(1, 5):
            hands_by_card = sort_hands(hands_by_card, card_values)
        for hand in hands_by_card:
            winnings += hands_by_card[hand][0][1] * rank
            rank += 1
    
    print(f'Part 1: {winnings}')
                            
    
def part_two():
    filename = 'day7-input.txt'
    hands = parse_hands(filename)
    
    # Rank hands by type
    hands_by_type = defaultdict(list)
    for hand in hands:
        hand_dict = defaultdict(int)
        for card in hand:
            hand_dict[card] += 1
        
        #####################################################################################
        #
        # This part replaces 'J' cards with the card in hand with the most copies, but only 
        # when finding hand types. Note that we want to retain 'J' cards for calculating 
        # tiebreaks. Also note that it doesn't matter which card get assigned the joker for 
        # full houses, since tiebreaks are calculated differently. 
        
        if 'J' in hand_dict:
            for card in sorted(hand_dict, key=lambda card: hand_dict[card], reverse=True):
                if card == 'J':
                    continue
                hand_dict[card] += hand_dict['J']
                break
            del hand_dict['J']
            
        ############################## End part 2 modification ##############################
        
        if len(hand_dict) <= 1:  # Length of dict for 'JJJJJ' is zero
            hands_by_type['6 five of a kind'].append((hand, hands[hand]))
        elif len(hand_dict) == 2:
            for card in hand_dict:
                if hand_dict[card] in [1, 4]:
                    hands_by_type['5 four of a kind'].append((hand, hands[hand]))
                else:
                    hands_by_type['4 full house'].append((hand, hands[hand]))
                break
        elif len(hand_dict) == 3:
            for card in hand_dict:
                if hand_dict[card] == 3:
                    hands_by_type['3 three of a kind'].append((hand, hands[hand]))
                    break
            else:
                hands_by_type['2 two pair'].append((hand, hands[hand]))
        elif len(hand_dict) == 4:
                hands_by_type['1 one pair'].append((hand, hands[hand]))
        else:  # len(hand_dict) == 5:
                hands_by_type['0 high card'].append((hand, hands[hand]))
    
    # New scoring dict, otherwise the same as part 1
    card_values = {
        'J': 0,
        '2': 1,
        '3': 2,
        '4': 3,
        '5': 4,
        '6': 5,
        '7': 6,
        '8': 7,
        '9': 8,
        'T': 9,
        'Q': 10,
        'K': 11,
        'A': 12
    }
    rank = 1
    winnings = 0
    for hand_type in sorted(hands_by_type.keys()):
        hands_by_card = dict()
        for card_type in card_values:
            hands_by_card[card_type] = sorted([hand for hand in hands_by_type[hand_type] if hand[0][0] == card_type], 
                                              key=lambda hand: card_values[hand[0][0][0]])
        for i in range(1, 5):
            hands_by_card = sort_hands(hands_by_card, card_values)
            
        for hand in hands_by_card:
            winnings += hands_by_card[hand][0][1] * rank
            rank += 1
    
    print(f'Part 2: {winnings}')
    

def sort_hands(hands_by_card, card_values):
    hands_by_card_new = dict()
    for card_root in hands_by_card:
        hands_with_root = hands_by_card[card_root]
        for card_type in card_values:
            root = card_root + card_type
            hands = sorted([hand for hand in hands_with_root if hand[0][:len(root)] == root], 
                                             key=lambda hand: card_values[hand[0][0][0]])
            if hands:
                hands_by_card_new[root] = hands
    return hands_by_card_new
    
    
def parse_hands(filename):
    hands_dict = dict()
    with open(filename, 'r') as f:
        for line in f:
            hand, score = line.split(' ')
            hands_dict[hand] = int(score)
            
    return hands_dict

    
if __name__ == '__main__':
    main()
