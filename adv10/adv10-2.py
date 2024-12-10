from aocd import get_data
from collections import defaultdict

data = get_data(year=2024, day=10).split("\n")
map_dict = defaultdict(lambda: "")
trail_graph = {}

for row in range(len(data)):
    
    for col in range(len(data[0])):
        map_dict[(row,col)] = data[row][col]

for row in range(len(data)):
    
    for col in range(len(data[0])):
        
        if (map_dict[(row,col)] in '0123456789'):
            neighbors = []
        
            for dir in [(0,1),(1,0),(0,-1),(-1,0)]:
                neighbor = (row+dir[0],col+dir[1])
                
                if (map_dict[neighbor] not in ["","."] and int(map_dict[neighbor]) == 1+int(map_dict[(row,col)])):
                    neighbors.append(neighbor)
            trail_graph[(row,col)] = neighbors

trail_heads = [coords for coords in map_dict if (map_dict[coords] not in ['', '.'] and map_dict[coords] == '0')]


def dfs(start, curr_path, visited, paths):
    
    if (start not in visited):
        visited.add(start)
        new_path = curr_path + [start]
        
        if (map_dict[start] == '9'):
            paths.append(tuple(new_path+[start]))
            return
            
        for neighbor in trail_graph[start]:
            dfs(neighbor, new_path, visited.copy(), paths)
    
def get_rank(trail_head):
    paths = []
    visited = set()
    dfs(trail_head, [], visited, paths)
    return len(paths)

print(sum([get_rank(trail_head) for trail_head in trail_heads]))