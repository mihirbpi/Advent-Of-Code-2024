from aocd import get_data
from collections import defaultdict

data = get_data(year=2024, day=6).split("\n")
grid_dict_init = defaultdict(lambda: "")
guard_pos_init = None
dirs = [(-1,0), (0,1), (1,0), (0,-1)]

for i in range(len(data)):
    
    for j in range(len(data[0])):
        grid_dict_init[(i,j)] = data[i][j]
        
        if (data[i][j] == "^"):
            guard_pos_init = (i,j)

count_loops = 0

for i in range(len(data)):
    
    for j in range(len(data[0])):
        
        if (grid_dict_init[(i,j)] == "."):
            guard_pos = guard_pos_init
            guard_dir_index = 0   
            encountered_states = set()
            grid_dict = grid_dict_init.copy()
            grid_dict[(i,j)] = "#"
            steps = 0
            
            while(grid_dict[guard_pos] != ""):
                
                if ((guard_pos, guard_dir_index) in encountered_states and steps > 1):
                    count_loops += 1
                    break
                
                encountered_states.add((guard_pos,guard_dir_index))
                dir = dirs[guard_dir_index]
                new_pos = (guard_pos[0]+dir[0], guard_pos[1]+dir[1])
                steps += 1
                
                if (grid_dict[new_pos] != "#"):
                    guard_pos = new_pos
                elif (grid_dict[new_pos] == "#"):
                    guard_dir_index = (guard_dir_index + 1) % 4
                    steps += 1
    
print(count_loops)