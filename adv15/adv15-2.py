from aocd import get_data
from collections import defaultdict, deque

data = get_data(year=2024, day=15).split("\n\n")
move_to_dir = {">": (0,1), "<": (0,-1), "v": (1,0), "^": (-1,0)}
moves = ""

for line in data[1].split("\n"):
    moves += line

grid_dict = defaultdict(lambda: "")
grid_array = []

for line in data[0].split("\n"):
    row = ""
    new_char = {"#": "##", "O": "[]", "@": "@.", ".": ".." }
    
    for c in line:
        row += new_char[c]
    grid_array.append(row)

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

def shift(pos, shift):
    return (pos[0]+shift[0], pos[1]+shift[1])
    
def is_blocked(pos, move):
    blocked = False
    new_pos = (pos[0]+move_to_dir[move][0], pos[1]+move_to_dir[move][1])
    
    if (move ==  ">"):
        blocked = (grid_dict[pos] == "]" and grid_dict[new_pos] == "#")
        
    elif (move == "<"):
        blocked = (grid_dict[pos] == "[" and grid_dict[new_pos] == "#")
        
    elif (move in "^v"):
        blocked = grid_dict[new_pos] == "#"
        
    return blocked
            
            
def move_robot(robot_pos, move, grid):
    moving_positions = set()
    new_pos = (tuple(robot_pos)[0]+move_to_dir[move][0], tuple(robot_pos)[1]+move_to_dir[move][1])
    
    if (grid_dict[new_pos] in "#"):
        return
    
    if (grid_dict[new_pos] == "."):
        grid_dict[tuple(robot_pos)] = "."
        robot_pos[0], robot_pos[1] = new_pos 
        grid_dict[tuple(robot_pos)] = "@"
        return
    
    moving_positions.add(tuple(robot_pos))
    Q = deque([new_pos])
    
    while (len(Q) > 0):
        curr_pos = Q.pop()

        if (is_blocked(curr_pos, move)):
                return
            
        if (curr_pos not in moving_positions):
            moving_positions.add(curr_pos)
            new_pos = (curr_pos[0]+move_to_dir[move][0], curr_pos[1]+move_to_dir[move][1])
                    
            if (move ==  ">"):
                
                if (grid_dict[curr_pos] == "]"):
                    Q.append(shift(curr_pos, (0,-1)))
                    
                    if (grid_dict[new_pos] == "["):
                        Q.append(new_pos)
                        Q.append(shift(new_pos,(0,1)))
                        
                if (grid_dict[curr_pos] == "["):
                    Q.append(shift(curr_pos, (0,1)))
                    
                    if (grid_dict[new_pos] == "]"):
                        Q.append(new_pos)
                        Q.append(shift(new_pos,(0,-1)))
            elif (move == "<"):
                
                if (grid_dict[curr_pos] == "["):
                    Q.append(shift(curr_pos, (0,1)))
                    
                    if (grid_dict[new_pos] == "]"):
                        Q.append(new_pos)
                        Q.append(shift(new_pos,(0,-1)))
                        
                if (grid_dict[curr_pos] == "]"):
                    Q.append(shift(curr_pos, (0,-1)))
                    
                    if (grid_dict[new_pos] == "["):
                        Q.append(new_pos)
                        Q.append(shift(new_pos,(0,1)))
                        
            elif (move in "^v"):
                
                if (grid_dict[curr_pos] == "["):
                    Q.append(shift(curr_pos, (0,1)))
                if (grid_dict[curr_pos] == "]"):
                    Q.append(shift(curr_pos, (0,-1)))
                if (grid_dict[new_pos] == "]"):
                        Q.append(new_pos)
                        Q.append(shift(new_pos,(0,-1)))
                if (grid_dict[new_pos] == "["):
                        Q.append(new_pos)
                        Q.append(shift(new_pos,(0,1)))
                        
    moving_positions = list(moving_positions)
    to_move = [grid_dict[pos] for pos in moving_positions]


    for pos in moving_positions:
        grid_dict[pos] = "."

    for i, pos in enumerate(moving_positions):
        new_pos = (pos[0]+move_to_dir[move][0], pos[1]+move_to_dir[move][1])
        grid_dict[new_pos] = to_move[i]
        
        if (grid_dict[new_pos] == "@"):
            robot_pos[0], robot_pos[1] = new_pos 
                

    grid[tuple(robot_pos)] = "@"

for move in moves:
    move_robot(robot_pos, move, grid_dict)
    
ans = 0

for pos in grid_dict:
    
    if grid_dict[pos] == "[":
        ans += 100*pos[0] + pos[1]
        
print(ans)
