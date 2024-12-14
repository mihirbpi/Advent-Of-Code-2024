from aocd import get_data

data = get_data(year=2024, day=14).split("\n")

x_dim = 101
y_dim = 103
    
def display(grid_dict, output):
    disp_string = ""
    
    for y in range(y_dim):
        y_string = ""
        
        for x in range(x_dim):
            
            if (grid_dict[(x,y)] > 0):
                y_string += "#"
            else:
                y_string += "."
                
        disp_string += y_string+"\n"
    output.write(disp_string)

output_file = open("output.txt", "w")

for num_steps in range(1+(101*103)):
    grid_dict = {}
    
    for x in range(x_dim):
        
        for y in range(y_dim):
            grid_dict[(x,y)] = 0
            
    robots = []
    
    for line in data:
        pos = list(map(int,line.split(" ")[0].split("=")[1].split(",")))
        vel = list(map(int,line.split(" ")[1].split("=")[1].split(",")))
        robots.append([pos, vel])
        
    for pos, vel in robots:
        pos[0] += vel[0]* num_steps
        pos[0] %= x_dim
        pos[1] += vel[1] *num_steps
        pos[1] %= y_dim 
        grid_dict[tuple(pos)] += 1
        
    safety_factor = 1

    for x_range in [(0, x_dim // 2), (x_dim//2+1, x_dim)]:
    
        for y_range in  [(0, y_dim // 2), (y_dim//2+1, y_dim)]:
            total = 0
        
            for x in range(*x_range):
            
                for y in range(*y_range):
                    total += grid_dict[(x,y)]

            safety_factor *= total
            
    output_file.write(f"output after {num_steps} steps: ")
    display(grid_dict,output_file)
    
output_file.close()