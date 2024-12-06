from aocd import get_data

rules_string, updates_string = get_data(year=2024, day=5).split("\n\n")
rules_dict = {}

for line in rules_string.split("\n"):
    before, after = list(map(int,line.split("|")))
    
    if before not in rules_dict:
        rules_dict[before] = [after]
    else:
        rules_dict[before].append(after)

def swap(l, i, j):
    temp = l[i]
    l[i] = l[j]
    l[j] = temp
        
def correct(update):
    res = False
    for before in rules_dict:
        
        for after in rules_dict[before]:
            
                if (before in update and after in update and update.index(before) >= update.index(after)):
                        swap_indices = update.index(before), update.index(after)
                        swap(update, *swap_indices)
                        correct(update)
                        res = True
    return res

res = 0

for line in updates_string.split("\n"):
    update = list(map(int,line.split(",")))
    
    if (correct(update)):
        res += update[len(update)//2]
        
print(res)