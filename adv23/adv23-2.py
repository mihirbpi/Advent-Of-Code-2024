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
        
nodes = list(graph_neighbors.keys())

def get_max_clique(R: list, P: list, X: list):
    
    if (len(X) == 0 and len(P) == 0):
        yield R
    
    for v in P[:]:
        R_new = R.copy()
        R_new.append(v)
        P_new = [val for val in P if val in graph_neighbors[v]] 
        X_new = [val for val in X if val in graph_neighbors[v]]
        
        for r in get_max_clique(R_new, P_new, X_new):
            yield r
            
        P.remove(v)
        X.append(v)
    
lan_party = sorted(list(get_max_clique([],nodes,[])), key=lambda x: len(x))[-1]
print(",".join(sorted(lan_party)))