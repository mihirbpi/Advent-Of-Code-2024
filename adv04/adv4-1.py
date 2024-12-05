from aocd import get_data
import re

data = get_data(year=2024, day=4).split("\n")
rows = data
columns = ["".join([row[i] for row in rows]) for i in range(len(data[0]))]

diags_bleft_tright = []
for row in range(len(rows)):
    diags_bleft_tright.append("".join([data[row-i][i] for i in range(row+1)]))
    
for col in range(1,len(columns)):
    diags_bleft_tright.append("".join([data[len(rows)-1-i][col+i] for i in range(len(rows)-col)]))
    
diags_bright_tleft = []
for row in range(len(rows)):
    diags_bright_tleft.append("".join([data[row-i][len(columns)-1-i] for i in range(row+1)]))
    
for col in range(1,len(columns)):
    diags_bright_tleft.append("".join([data[len(rows)-1-i][len(columns)-1-col-i] for i in range(len(rows)-col)]))
    
ans = 0

for string in rows + columns + diags_bleft_tright + diags_bright_tleft :
    ans += len(re.findall(r'XMAS', string))
    ans += len(re.findall(r'SAMX', string))
    
print(ans)