from aocd import get_data
import re

data = get_data(year=2024, day=3)
real_instructions = re.findall(r"mul\(\d+,\d+\)",data)

ans = 0

for instruction in real_instructions:
    digits = re.match(r"mul\((\d+),(\d+)\)", instruction)
    n1, n2 = digits.group(1,2)
    ans += int(n1) * int(n2)
    
print(ans)