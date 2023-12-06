def main():
    part_one()
    part_two()
    
    
def part_one():
    schematic = [line for line in open('day3-input.txt', 'r').readlines()]
    sum_of_parts = 0
    for i in range(len(schematic)):
        number = None
        start_column = 0
        for j in range(len(schematic[i])):
            if j > 0:  # All but first char in row
                if schematic[i][j].isdigit():  # Current char is digit
                    if number is not None:  # Current number is valid. This will catch any valid cases where previous char is digit
                        number += schematic[i][j]
                    elif schematic[i][j-1] == '.':  # If previous char is not symbol, initialize new number
                        number = schematic[i][j]
                        start_column = j
                    else:  # Previous char is symbol
                        number = schematic[i][j]
                        start_column = j
                else:  # Current character follows number
                    if number is not None: 
                        sum_of_parts += check_number(number, schematic, row=i, start_column=start_column, end_column=j)
                    number = None
            elif schematic[i][j].isdigit():  # First char in row is number
                number = schematic[i][j]
                                
    print(f'Part 1: {sum_of_parts}')
    
    
def part_two():
    from collections import defaultdict
    
    schematic = [line for line in open('day3-input.txt', 'r').readlines()]
    gear_dict = defaultdict(list)
    sum_of_ratios = 0
    for i in range(len(schematic)):
        number = None
        start_column = 0
        for j in range(len(schematic[i])):
            if j > 0:  # All but first char in row
                if schematic[i][j].isdigit():  # Current char is digit
                    if number is not None:  # Current number is valid. This will catch any valid cases where previous char is digit
                        number += schematic[i][j]
                    elif schematic[i][j-1] == '.':  # If previous char is not symbol, initialize new number
                        number = schematic[i][j]
                        start_column = j
                    else:  # Previous char is symbol
                        number = schematic[i][j]
                        start_column = j
                else:  # Current character follows number
                    if number is not None: 
                        gears, number = check_gears(number, schematic, row=i, start_column=start_column, end_column=j)
                        for gear in gears:
                            gear_dict[gear].append(number)
                    number = None
            elif schematic[i][j].isdigit():  # First char in row is number
                number = schematic[i][j]
    for gear in gear_dict:
        if len(gear_dict[gear]) == 2:
            sum_of_ratios += gear_dict[gear][0] * gear_dict[gear][1]
    
    print(f'Part 2: {sum_of_ratios}')
                    

def check_gears(number, schematic, row, start_column, end_column):
    gears = []
    def test_rows(start, end):    
        # Test rows above and below
        if 0 < row < len(schematic)-1:  # Most common case, rows exist above and below
            if '*' in schematic[row-1][start:end]:
                gears.append((row-1, start + schematic[row-1][start:end].index('*')))
            if '*' in schematic[row+1][start:end]:
                gears.append((row+1, start + schematic[row+1][start:end].index('*')))
        elif row == 0:  # First row, so only check below
            if '*' in schematic[row+1][start:end]:
                gears.append((row+1, start + schematic[row+1][start:end].index('*')))
        else:  # Last row, so only check above
            if '*' in schematic[row-1][start:end]:
                gears.append((row-1, start + schematic[row-1][start:end].index('*')))
    
    # Check left/right, then check above/below
    if 0 < start_column and end_column < len(schematic[row]) - 1:  # Most common case, number in the middle of a row
        if schematic[row][start_column-1] == '*':
            gears.append((row, start_column-1))
        if schematic[row][end_column] == '*':
            gears.append((row, end_column))
        test_rows(start_column-1, end_column+1)
    elif len(number) == len(schematic[row]):  # Pathological case, number spans entire row
        test_rows(start=0, end=len(schematic[row]))
    else:  # Number is either first in row or last in row
        if start_column == 0 and schematic[row][end_column] == '*':
            gears.append((row, end_column))
        if end_column == len(schematic[row]) - 1 and schematic[row][start_column-1] == '*':
            gears.append((row, start_column-1))
        if start_column == 0:
            test_rows(start_column, end_column+1)
        else:
            test_rows(start_column-1, end_column)
    
    return gears, int(number)
    
    
def check_number(number, schematic, row, start_column, end_column):
    def test_rows(test_string, start, end):    
        # Test rows above and below
        if 0 < row < len(schematic)-1:  # Most common case, rows exist above and below
            if schematic[row-1][start:end] == schematic[row+1][start:end] == test_string:
                return 0
            return int(number)
        elif row == 0:  # First row, so only check below
            if schematic[row+1][start:end] == test_string:
                return 0
            return int(number)
        else:  # Last row, so only check above
            if schematic[row-1][start:end] == test_string:
                return 0
            return int(number)
    
    # Test left/right, else build test string and compare above/below
    if 0 < start_column and end_column < len(schematic[row]) - 1:  # Most common case, number in the middle of a row
        if schematic[row][start_column-1] != '.' or schematic[row][end_column] != '.':
            return int(number)
        test_string = '.' * (len(number) + 2)
        return test_rows(test_string, start_column-1, end_column+1)
    elif len(number) == len(schematic[row]):  # Pathological case, number spans entire row
        test_string == '.' * len(number)
        return test_rows(test_string, start=0, end=len(schematic[row]))
    else:  # Number is either first in row or last in row
        if start_column == 0 and schematic[row][end_column] != '.':
            return int(number)
        elif end_column == len(schematic[row]) - 1 and schematic[row][start_column-1] != '.':
            return int(number)
        test_string = '.' * (len(number) + 1)
        if start_column == 0:
            return test_rows(test_string, start_column, end_column+1)
        else:
            return test_rows(test_string, start_column-1, end_column)


if __name__ == '__main__':
    main()
