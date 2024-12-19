from aocd import get_data

data = get_data(year=2024, day=19).split("\n\n")
patterns = data[0].split(", ")
designs = data[1].split("\n")

def num_ways(design, D):
    
    if (design == ""):
        D[design] = 1
        return 1
    
    if (design in D):
        return D[design]
    
    res = 0
        
    for i in range(min(len(design), max([len(pattern) for pattern in patterns]))+1):
        
        if (design[:i] in patterns):
            res += num_ways(design[i:],D)
            
    D[design] = res
    return res
        
memo_ways = {}
ans = 0

for design in designs:
    ans += num_ways(design,memo_ways)
    
print(ans)