from aocd import get_data
from collections import defaultdict

data = get_data(year=2024, day=15).split("\n\n")
move_to_dir = {">": (0,1), "<": (0,-1), "v": (1,0), "^": (-1,0)}
moves = ""

for line in data[1].split("\n"):
    moves += line
    
grid_dict = defaultdict(lambda: "")
grid_array = data[0].split("\n")

robot_pos = [0,0]

for row in range(len(grid_array)):
    
    for col in range(len(grid_array[0])):    
        grid_dict[(row, col)] = grid_array[row][col]
        
        if (grid_array[row][col] == "@"):
            robot_pos = [row, col]

def print_grid(grid_dict, grid_array):
    to_print = ""
    for row in range(len(grid_array)):
        to_print += "".join([grid_dict[(row, i)] for i in range(len(grid_array[0]))])+"\n"
    print(to_print)

def move_robot(robot_pos, move, grid):
    curr_pos = tuple(robot_pos)
    moving_positions = [curr_pos]
    
    while (grid[(curr_pos[0]+move_to_dir[move][0], curr_pos[1]+move_to_dir[move][1])] == "O"):
        curr_pos = (curr_pos[0]+move_to_dir[move][0], curr_pos[1]+move_to_dir[move][1])
        moving_positions.append(curr_pos)
        
    if (grid_dict[(moving_positions[-1][0]+move_to_dir[move][0], moving_positions[-1][1]+move_to_dir[move][1])] != "#"):
        to_move = [grid[pos] for pos in moving_positions]
        
        for pos in moving_positions:
            grid_dict[pos] = "."
        
        for i in range(len(moving_positions)):
            pos = moving_positions[i]
            new_pos = (pos[0]+move_to_dir[move][0], pos[1]+move_to_dir[move][1])
            grid_dict[new_pos] = to_move[i]
            
            if (i == 0):
                robot_pos[0], robot_pos[1] = new_pos 
                

    grid[tuple(robot_pos)] = "@"

for move in moves:
    move_robot(robot_pos, move, grid_dict)
    
ans = 0

for pos in grid_dict:
    
    if grid_dict[pos] == "O":
        ans += 100*pos[0] + pos[1]
        
print(ans)
