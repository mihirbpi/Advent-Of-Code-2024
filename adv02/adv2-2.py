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

def is_actually_safe(report):
    
    if (is_safe(report)):
        return True
    
    for i in range(len(report)):
        report_i_removed = [report[j] for j in range(len(report)) if j != i]
        
        if (is_safe(report_i_removed)):
            return True
        
    return False
    
print(sum([is_actually_safe(report) for report in reports]))