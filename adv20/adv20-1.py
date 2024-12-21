from aocd import get_data
from collections import defaultdict, deque

data = get_data(year=2024, day=20).split("\n")
grid_dict = defaultdict(lambda: "")
start, end = None, None

for row in range(len(data)):
    
    for col in range(len(data[0])):
        entry =  data[row][col]
        grid_dict[(row,col)] = entry
        
        if (entry == "S"):
            grid_dict[(row, col)] = "."
            start = (row, col)    
        elif (entry == "E"):
            grid_dict[(row, col)] = "."
            end = (row, col)
            
distances = {}
Q = deque([(*start,0)])

while Q:
    row, col, d = Q.pop()
    distances[(row, col)] = d
    
    if ((row, col) == end):
        break
    
    for dir in [(0,1), (1,0), (0,-1), (-1,0)]:
        neighbor = (row+dir[0], col+dir[1])
        
        if (grid_dict[neighbor] != "#" and grid_dict[neighbor] != "" and neighbor not in distances):
            Q.append((*neighbor, d+1))
            
ans = 0

for pos in distances:
    
    for dir in [(1,1), (1,-1), (-1,1), (-1,-1), (2,0), (0,2), (-2,0), (0,-2)]:
        new_pos = (pos[0]+dir[0], pos[1]+dir[1])
        
        if (grid_dict[new_pos] != "" and grid_dict[new_pos] != "#"):
            saved = distances[pos]-distances[new_pos]
            
            if (saved >= 102):
                ans += 1
                                
print(ans)