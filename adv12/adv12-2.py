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

def sides(region):
    sides = []
    fence = set()
    
    for row, col in region:
        
        for dir in [(0,1), (1,0), (0,-1), (-1,0)]:
            
            if ((row+dir[0], col+dir[1]) not in region):
                fence.add((row, col, dir))
                
    seen = set()           
    for row, col, dir in fence:
        
        if ((row, col, dir) not in seen):
            seen.add((row, col, dir))
            side = [(row, col, dir)]
            
            if (dir in [(0,1), (0,-1)]):
                i = 1
                
                while(row + i < len(data) and (row+i, col, dir) in fence):
                    
                    if ((row+i, col, dir) not in seen):
                        seen.add((row+i, col, dir))
                        side.append((row+i, col, dir))
                    i += 1
                i = 1
                
                while(row - i >= 0 and (row-i, col, dir) in fence):
                    
                    if ((row-i, col, dir) not in seen):
                        seen.add((row-i, col, dir))
                        side.append((row-i, col, dir))
                    i += 1
            elif (dir in [(1,0), (-1,0)]):
                i = 1
                
                while(col + i < len(data[0]) and (row, col+i, dir) in fence):
                    
                    if ((row, col+i, dir) not in seen):
                        seen.add((row, col+i, dir))
                        side.append((row, col+i, dir))
                    i += 1
                i = 1
                
                while(col - i >= 0 and (row, col-i, dir) in fence):
                    
                    if ((row, col-i, dir) not in seen):
                        seen.add((row, col-i, dir))
                        side.append((row, col-i, dir))
                    i += 1
            sides.append(side)
            
    return len(sides)       
        
price = sum([area(region)*sides(region) for region in regions])
print(price)