from aocd import get_data

data = get_data(year=2024, day=25).split("\n\n")
#data = open("test.txt", "r").read().split("\n\n")
locks = []
keys = []

for line in data:
    line_split = line.split("\n")
    
    if (line_split[0] == 5*"."):
        keys.append([[x[i] for x in line_split].count("#")-1 for i in range(5)])
    else:
        locks.append([[x[i] for x in line_split].count("#")-1 for i in range(5)])

def fit(lock, key):
    
    for i in range(5):
        
        if (lock[i] + key[i] > 5):
            return False
        
    return True

ans = 0

for lock in locks:
    
    for key in keys:
        ans += fit(lock, key)

print(ans)