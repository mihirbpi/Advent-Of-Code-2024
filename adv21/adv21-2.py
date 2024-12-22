from aocd import get_data
from itertools import permutations
from functools import lru_cache

data = get_data(year=2024, day=21).split("\n")
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

@lru_cache(None)  
def get_paths(start, end, use_numeric):
    grid_dict = direction_dict
    
    if (use_numeric):
        grid_dict = numeric_dict
    
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

@lru_cache(None)
def get_cost(a,b,use_numeric,depth):
    if (depth == 0):
        return min([len(x) for x in get_paths(a,b,False)])
    
    paths = get_paths(a,b,use_numeric)
    best_cost = 1e9999999
    
    for path in paths:
        cost = 0
    
        for start, end in zip("A"+path, path):
            cost += get_cost(start, end, False, depth-1)
            
        best_cost = min(cost, best_cost)
        
    return best_cost

@lru_cache(None)
def get_code_cost(code, depth):
    cost = 0
    
    for start, end in zip("A"+code, code):
        cost += get_cost(start, end, True, depth)
        
    return cost

ans = 0   

for code in data:
    ans += get_code_cost(code, 25) * int(code[:-1])
    
print(ans)