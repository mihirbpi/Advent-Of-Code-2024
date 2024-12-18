from aocd import get_data
from collections import defaultdict, deque

data = get_data(year=2024, day=18).split("\n")
num_bytes = 1024
dim = 71
all_bytes = [tuple(map(int,reversed(line.split(",")))) for line in data]
corrupted = all_bytes[:num_bytes]
uncorrupted = all_bytes[num_bytes:]
grid_dict = defaultdict(lambda: "")
neighbors_dict = {}

for row in range(dim):
    
    for col in range(dim):
        
        if ((row, col) in corrupted):
            grid_dict[(row, col)] = "#"
        else:
            grid_dict[(row, col)] = "."

neighbors_dict = {}
for row, col in grid_dict.copy():
    neighbors = []
        
    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
        neighbor = (row+dir[0], col+dir[1])
            
        if (grid_dict[neighbor] == "."):
            neighbors.append(neighbor)
                
    neighbors_dict[(row, col)] = neighbors
        

start = (0,0)
end = (dim-1,dim-1)

def can_reach_start(bytes, end, start):
    Q  = deque([end])
    visited = set()
    
    while (len(Q) > 0):
        row, col = Q.pop()
        
        if ((row, col) == start):
            return True
        
        if ((row, col) not in visited):
            visited.add((row, col))
            
            for neighbor in neighbors_dict[(row, col)]:
                if (neighbor not in bytes):
                    Q.append(neighbor)
                
    return False

for i, byte in enumerate(uncorrupted):
    grid_dict[byte] = "#"
    can_reach = can_reach_start(uncorrupted[:i+1], end, start)
    
    if (not can_reach):
        print(tuple(reversed(byte)))
        break