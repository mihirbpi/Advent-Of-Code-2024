from aocd import get_data
from collections import defaultdict, deque

data = get_data(year=2024, day=18).split("\n")
num_bytes = 1024
dim = 71
corrupted = [tuple(map(int,reversed(line.split(",")))) for line in data[:num_bytes]]
grid_dict = defaultdict(lambda: "")
neighbors_dict = {}

for row in range(dim):
    
    for col in range(dim):
        
        if ((row, col) in corrupted):
            grid_dict[(row, col)] = "#"
        else:
            grid_dict[(row, col)] = "."

for row, col in grid_dict.copy():
    neighbors = []
    
    for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
        neighbor = (row+dir[0], col+dir[1])
        
        if (grid_dict[neighbor] == "."):
            neighbors.append(neighbor)
            
    neighbors_dict[(row, col)] = neighbors

start = (0,0)
end = (dim-1,dim-1)

def dijkstra(start, end):
    dist = {}
    prev = {}
    Q = deque([])

    for v in grid_dict.copy():
        dist[v] = 1e99
        prev[v] = None 
        Q.append(v)
        
    dist[start] = 0

    while (len(Q) > 0):

        min_dist = 1e99
        u = None
        
        for v in Q:
            
            if (dist[v] <= min_dist):
                min_dist = dist[v]
                u = v
                
        if (u == end):
            break
        Q.remove(u)
        
        for v in neighbors_dict[u]:
            alt = dist[u] + 1
            
            if (alt < dist[v]):
                dist[v] = alt
                prev[v] = u
    S = deque([])
    u = end 
    
    if (prev[u] or u == start):
        
        while u:
            S.appendleft(u)
            u = prev[u] 
    total_cost = 0
    
    for i in range(len(S)-1):
        total_cost += 1

    return S, total_cost  

_, cost = dijkstra(start, end)
print(cost)
    