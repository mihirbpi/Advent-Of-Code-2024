from aocd import get_data

data = get_data(year=2024, day=11).split(" ")
stones = list(map(int,data))

def blink(stones):
    new_stones = []
    
    for i in range(len(stones)):
        stone_num = stones[i]
        
        if (stone_num == 0):
            new_stones.append(1)
        elif (len(str(stone_num)) % 2 == 0):
            stone_str = str(stone_num)
            half1 = int(stone_str[:len(stone_str)//2])
            half2 = int(stone_str[len(stone_str)//2:])
            new_stones.extend([half1, half2])
        else:
            new_stones.append(2024*stone_num)
            
    return new_stones

num_blinks = 25

for _ in range(num_blinks):
    stones = blink(stones)
    
print(len(stones))