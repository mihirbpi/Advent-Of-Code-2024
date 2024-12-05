from aocd import get_data
import re

data = get_data(year=2024, day=4).split("\n")

ans = 0
for row in range(len(data)-2):
    
    for col in range(len(data[0])-2):
        diag1 = "".join([data[row+i][col+i] for i in range(3)])
        diag2 = "".join([data[row+2-i][col+i] for i in range(3)])
        diag1_mas = diag1 == "SAM" or diag1 =="MAS"
        diag2_mas = diag2 == "SAM" or diag2 =="MAS"
        
        if (diag1_mas and diag2_mas):
            ans += 1
    
print(ans)