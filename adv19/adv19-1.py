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
        
    for i in range(len(design)):
        
        for pattern in patterns:
            
            if (design.startswith(pattern)):
                
                if (possible(design[len(pattern):],D)):
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