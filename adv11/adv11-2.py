from aocd import get_data

data = get_data(year=2024, day=11).split(" ")
stones = list(map(int,data))

def num_stones_produced(n, D, blinks_remaining):
    
    if (n,  blinks_remaining) in D:
        return D[(n, blinks_remaining)]
    
    elif (blinks_remaining == 0):
        return 0
    
    elif (blinks_remaining == 1):
        
        if (n == 0):
            return 1
        elif (len(str(n)) % 2 == 0):
            return 2
        else:
            return 1
    
    else:
        res = None
        
        if (n == 0):
            res = num_stones_produced(1, D, blinks_remaining-1)
        elif (len(str(n)) % 2 == 0):
            stone_str = str(n)
            half1 = int(stone_str[:len(stone_str)//2])
            half2 = int(stone_str[len(stone_str)//2:])
            res = num_stones_produced(half1, D, blinks_remaining-1) + num_stones_produced(half2, D, blinks_remaining-1)
        else:
            res = num_stones_produced(2024*n, D, blinks_remaining-1)
            
        D[(n, blinks_remaining)] = res
        return res

D = {}
num_blinks = 75
final_num_stones = sum([num_stones_produced(stone, D, num_blinks) for stone in stones])
print(final_num_stones)