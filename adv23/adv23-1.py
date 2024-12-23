from aocd import get_data

data = get_data(year=2024, day=23).split("\n")
graph_neighbors = {}

for line in data:
    node1, node2 = line.split("-")
    
    if (node1 not in graph_neighbors):
        graph_neighbors[node1] = [node2]
    else:
        graph_neighbors[node1].append(node2)
        
    if (node2 not in graph_neighbors):
        graph_neighbors[node2] = [node1]
    else:
        graph_neighbors[node2].append(node1)
        
nodes = graph_neighbors.keys()
t_nodes = [node for node in nodes if "t" == node[0]]

triplets = set()

for t_node in t_nodes:
    
    for node1 in graph_neighbors[t_node]:
        
        for node2 in graph_neighbors[node1]:
            
            if (t_node in graph_neighbors[node2]):
                triplets.add(tuple(sorted((t_node,node1,node2))))
    
print(len(triplets))