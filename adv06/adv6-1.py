from aocd import get_data
from collections import defaultdict

data = get_data(year=2024, day=6).split("\n")
grid_dict = defaultdict(lambda: "")
guard_pos = None
guard_dir_index = 0
dirs = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(len(data)):
    
    for j in range(len(data[0])):
        grid_dict[(i,j)] = data[i][j]
        
        if (data[i][j] == "^"):
            guard_pos = (i,j)
            
visited = set()

while(grid_dict[guard_pos] != ""):
    visited.add(guard_pos)
    dir = dirs[guard_dir_index]
    new_pos = (guard_pos[0]+dir[0], guard_pos[1]+dir[1])
    
    if (grid_dict[new_pos] != "#"):
        guard_pos = new_pos
    elif (grid_dict[new_pos] == "#"):
        guard_dir_index = (guard_dir_index + 1) % 4
    
print(len(visited))