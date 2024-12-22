from aocd import get_data
from itertools import permutations, product

data = get_data(year=2024, day=21).split("\n")
#data = open("test.txt", "r").read().split("\n")
numeric_dict = {}
direction_dict = {}

for i, num in enumerate(["7","8","9"]):
    numeric_dict[num] = (0,i)
    
for i, num in enumerate(["4","5","6"]):
    numeric_dict[num] = (1,i)

for i, num in enumerate(["1","2","3"]):
    numeric_dict[num] = (2,i)
    
for i, num in enumerate(["0","A"]):
    numeric_dict[num] = (3,i+1)

for i, dir in enumerate(["^","A"]):
    direction_dict[dir] = (0,i+1)
    
for i, dir in enumerate(["<","v",">"]):
    direction_dict[dir] = (1,i)

symbol_to_dir = {"v":(1,0), "^": (-1,0), ">": (0,1), "<": (0,-1)}

    
def paths(start, end, grid_dict):
    drow = grid_dict[end][0]-grid_dict[start][0]
    dcol = grid_dict[end][1]-grid_dict[start][1]
    seqs = ""
    
    if drow > 0:
        seqs += drow*"v"
    if drow < 0:
        seqs += -drow*"^"
    if dcol > 0:
        seqs += dcol*">"
    if  dcol < 0:
        seqs += -dcol*"<"
        
    valid_seqs = []
    
    for seq in ["".join(x) + "A" for x in list(set(permutations(seqs)))]:
        curr  = grid_dict[start]
        invalid = False

        for i in range(len(seq)-1):
            symbol = seq[i]
            dir = symbol_to_dir[symbol]
            curr = (curr[0]+dir[0],curr[1]+dir[1])
                
            if (curr not in grid_dict.values()):
                invalid = True
                break
            
        if (not invalid): 
            valid_seqs.append(seq)

    return valid_seqs

map_numeric = {}

for x in numeric_dict:
    for y in numeric_dict:
        if (x == y):
            map_numeric[(x,y)] = ["A"]
        else:
            map_numeric[(x,y)] = paths(x,y,numeric_dict)

map_direction = {}

for x in direction_dict:
    for y in direction_dict:
        if (x == y):
            map_direction[(x,y)] = ["A"]
        else:
            map_direction[(x,y)] = paths(x,y,direction_dict)

def code_seqs(code, map):
    instruction_seqs = [map[(start,end)] for start, end in zip("A" + code, code)]
    return ["".join(p) for p in product(*instruction_seqs)]

def get_min_length(code):
    seqs = code_seqs(code, map_numeric)
    seqs1 = []
    min_length1 = min([len(x) for x in seqs])
    seqs = [seq for seq in seqs if len(seq) == min_length1]

    for seq in seqs:
        seqs1.extend(code_seqs(seq,map_direction))
        
    min_length2 = min([len(x) for x in seqs1])
    seqs1 = [seq for seq in seqs1 if len(seq) == min_length2]

    min_length = 1e99

    for seq in seqs1:
        res = code_seqs(seq,map_direction)
        min_length = min(min_length, min([len(x) for x in res]))

    return min_length

ans = 0   

for code in data:
    ans += get_min_length(code) * int(code[:-1])
    
print(ans)