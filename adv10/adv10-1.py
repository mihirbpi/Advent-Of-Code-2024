from aocd import get_data
from collections import defaultdict, deque

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

def get_score(trail_head):
    visited = set()
    nines = set()
    Q = deque([trail_head])
    
    while (len(Q) > 0):
        curr = Q.pop()
        if (curr not in visited):
            visited.add(curr)
            if (map_dict[curr] == '9'):
                nines.add(curr)
            for neighbor in trail_graph[curr]:
                Q.append(neighbor)
    return len(nines)

print(sum([get_score(trail_head) for trail_head in trail_heads]))