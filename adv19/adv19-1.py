from aocd import get_data

data = get_data(year=2024, day=19).split("\n\n")
patterns = data[0].split(", ")
designs = data[1].split("\n")

def possible(design, D):
    
    if (design == ""):
        D[design] = True
        return True
    
    if (design in D):
        return D[design]
        
    for i in range(min(len(design), max([len(pattern) for pattern in patterns]))+1):
        
        if (design[:i] in patterns and possible(design[i:],D)):
            D[design] = True
            return True

    D[design] = False
    return False
                
                
memo_possible = {}
ans = 0

for design in designs:
    
    if (possible(design, memo_possible)):
        ans += 1
        
print(ans)