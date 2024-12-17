from aocd import get_data
from collections import defaultdict, deque

data = get_data(year=2024, day=16).split("\n")
grid_dict = defaultdict(lambda: "")
moves = ["^", ">", "v", "<"]
move_to_dir = {"^": (-1,0), ">": (0,1), "v": (1,0), "<":(0,-1)}

nodes = set()
edges = set()
edge_weight_dict = {}
neighbors_dict = {}

start, ends = None, []

for row in range(len(data)):
    
    for col in range(len(data[0])):
        
        if (data[row][col] == "S"):
            start = (row, col, ">")
        elif (data[row][col] == "E"):
            ends.extend([(row, col,move) for move in moves])
            
        grid_dict[(row, col)] = data[row][col]

for row in range(len(data)):
    
    for col in range(len(data[0])):
        
        if (grid_dict[(row, col)] in "ES."):
            
            for move in moves:
                node = (row, col, move)
                node_90cw = (row, col, moves[(moves.index(move)+1)%4])
                nodes.add(node_90cw)
                edge_cw = (node, node_90cw)
                edges.add(edge_cw)
                edge_weight_dict[edge_cw] = 1000
                node_90ccw = (row, col, moves[(moves.index(move)-1)%4])
                nodes.add(node_90ccw)
                edge_ccw = (node, node_90ccw)
                edges.add(edge_ccw)
                edge_weight_dict[edge_ccw] = 1000
                node_ahead = (row+move_to_dir[move][0], col+move_to_dir[move][1], move)
                
                if (node not in neighbors_dict):
                    neighbors_dict[node] = [node_90cw, node_90ccw]
                else:
                    neighbors_dict[node].extend([node_90cw, node_90ccw])
                
                if (grid_dict[(node_ahead[0], node_ahead[1])] in "ES."):
                    nodes.add(node_ahead)
                    edge_ahead = (node, node_ahead)
                    edges.add(edge_ahead)
                    edge_weight_dict[edge_ahead] = 1
                    neighbors_dict[node].append(node_ahead)
                        
# Dijkstra
def dijkstra(end):
    dist = {}
    prev = {}
    Q = deque([])

    for v in nodes:
        dist[v] = 1e99
        prev[v] = []
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
            alt = dist[u] + edge_weight_dict[(u, v)]
            
            if (alt < dist[v]):
                dist[v] = alt
                prev[v] = [u]
            elif (alt == dist[v]):
                prev[v].append(u)

    return prev        
    
prev = dijkstra(ends[0])
seen = set()
tiles = set()

def dfs(s):
    
    if (s in seen):
        return
    
    seen.add(s)
    tiles.add((s[0], s[1]))
    
    for other in prev[s]:
        dfs(other) 
        
dfs(ends[0])
print(len(tiles))