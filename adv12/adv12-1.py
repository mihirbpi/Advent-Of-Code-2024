from aocd import get_data
from collections import defaultdict, deque

data = get_data(year=2024, day=12).split("\n")

garden_dict = defaultdict(lambda: "")
garden_neighbors_dict = {}

for row in range(len(data)):
    
    for col in range(len(data[0])):
        garden_dict[(row, col)] = data[row][col]

for row in range(len(data)):
    
    for col in range(len(data[0])):
        curr = garden_dict[(row, col)]
        garden_neighbors_dict[(row, col)] = []
        
        for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
            neighbor = (row+dir[0], col+dir[1])
            
            if (garden_dict[neighbor] == curr):
                garden_neighbors_dict[(row, col)].append(neighbor)

regions = []
seen = set()
for row in range(len(data)):
    
    for col in range(len(data[0])):
        if ((row, col) not in seen):
            visited = set()
            Q = deque([(row, col)])
                
            while (len(Q) > 0):
                curr = Q.pop()
                    
                if (curr not in visited):
                    visited.add(curr)
                    seen.add(curr)
                        
                    for neighbor in garden_neighbors_dict[curr]:
                        Q.append(neighbor)
            regions.append(list(visited))
        
def area(region):
    return len(region)

def perimeter(region):
    p = 0
    for row, col in region:
        
        for dir in [(0,1), (0,-1), (1,0), (-1,0)]:
            neighbor = (row+dir[0],col+dir[1])
            
            if (neighbor not in region):
                p += 1
    return p

price = sum([area(region)*perimeter(region) for region in regions])
print(price)