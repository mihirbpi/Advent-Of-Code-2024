from aocd import get_data

data = get_data(year=2024, day=2).split("\n")
reports = [list(map(int,line.split(" "))) for line in data]

def is_safe(report):
    
    if(sorted(report) != list(reversed(report)) and sorted(report) != report):
        return False
    
    for i in range(len(report)-1):
        change = abs(report[i+1] - report[i])
        
        if (change < 1):
            return False
        elif(change > 3):
            return False
        
    return True

print(sum([is_safe(report) for report in reports]))