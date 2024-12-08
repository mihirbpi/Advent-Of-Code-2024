from aocd import get_data
from collections import defaultdict
from itertools import combinations

data = get_data(year=2024, day=8).split("\n")
map_dict = defaultdict(lambda: "")
antennas_dict = {}

for row in range(len(data)):
    
    for col in range(len(data[0])):
        map_dict[(row,col)] = data[row][col]
        
        if(data[row][col] != "."):
            
            if (data[row][col] in antennas_dict):
                antennas_dict[data[row][col]].append((row,col))
            else:
                antennas_dict[data[row][col]] = [(row,col)]
                
antinodes = set()
        
for antenna_label in antennas_dict:
    
    if (len(antennas_dict[antenna_label]) > 1):
        
        for antenna in antennas_dict[antenna_label]:
            antinodes.add(antenna)
    
    for antenna1, antenna2 in sorted(combinations(antennas_dict[antenna_label],2)):
        dx = antenna2[0]-antenna1[0]
        dy =  antenna2[1]-antenna1[1]  
        start_antinode_left = (antenna1[0]-dx, antenna1[1]-dy)
        start_antinode_right = (antenna2[0]+dx, antenna2[1]+dy)
        
        for start_antinode in [start_antinode_left, start_antinode_right]:
            curr_antinode = start_antinode
            
            while (0 <= curr_antinode[0] <= len(data)-1 and 0 <= curr_antinode[1] <= len(data[0])-1):
                antinodes.add(curr_antinode)
                
                if(start_antinode == start_antinode_left):
                    curr_antinode = (curr_antinode[0]-dx, curr_antinode[1]-dy)
                else:
                    curr_antinode = (curr_antinode[0]+dx, curr_antinode[1]+dy)
                    
print(len(antinodes))       