from aocd import get_data
import re

data = get_data(year=2024, day=3)
real_instructions = re.finditer(r"(mul\(\d+,\d+\))|(do\(\))|(don't\(\))",data)

ans = 0
mul_enabled = True

for instruction_match in real_instructions:
    instruction = instruction_match.group(0)
    
    if (instruction[:3]=="mul" and mul_enabled):
        digits = re.match(r"mul\((\d+),(\d+)\)", instruction)
        n1, n2 = digits.group(1,2)
        ans += int(n1) * int(n2)
    elif (instruction == "do()"):
        mul_enabled = True
    else:
        mul_enabled = False
        
print(ans)