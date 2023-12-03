def main():
    part_one()
    part_two()
    
    
def part_one():
    with open('day1-input.txt', 'r') as f:
        calibration = 0
        for line in f.readlines():
            first, last = None, None
            for i in range(len(line)):
                if first is None:
                    try:
                        first = int(line[i]) * 10
                    except ValueError:
                        pass
                if last is None:
                    try:
                        last = int(line[-(i+1)])
                    except ValueError:
                        pass
                if first is not None and last is not None:
                    calibration += first + last
                    break
                    
        print(f'Part 1: {calibration}')
                        

def part_two():        
    digits = [0, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    
    with open('day1-input.txt', 'r') as f:
        calibration = 0
        for line in f.readlines():
            first, last = None, None
            for i in range(len(line)):
                if first is None:
                    try:
                        first = int(line[i]) * 10
                    except ValueError:
                        for length in range(3, 6):
                            if line[i:i+length] in digits:
                                first = digits.index(line[i:i+length]) * 10
                                break
                                
                if last is None:
                    try:
                        last = int(line[-(i+1)])
                    except ValueError:
                        for length in range(3, 6):
                            if i == 0 and line[-length:] in digits:
                                last = digits.index(line[:-(i+1)])
                                break
                            elif line[-(i+1+length):-(i+1)] in digits:
                                last = digits.index(line[-(i+1+length):-(i+1)])
                                break
                                
                if first is not None and last is not None:
                    calibration += first + last
                    break
                    
        print(f'Part 2: {calibration}')
    
        
if __name__ == '__main__':
    main()
