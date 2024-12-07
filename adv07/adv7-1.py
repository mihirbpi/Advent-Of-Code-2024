from aocd import get_data
from itertools import product

data = get_data(year=2024, day=7).split("\n")

def evaluate(equation):
    res = equation[0]
    
    for i in range(1, len(equation)-1, 2):
        
        if (equation[i] == '+'):
            res = res + equation[i+1]
            
        elif(equation[i] == "*"):
            res = res * equation[i+1]
            
    return res
    
answer = 0

for entry in data:
    test_val, equation_nums = entry.split(": ")
    test_val = int(test_val)
    equation_nums = list(map(int,equation_nums.split(" ")))
    equation_template = []
    
    for num in equation_nums:
        equation_template.append(num)
        equation_template.append("")
        
    equation_template = equation_template[:-1]
    operator_indices = [i for i in range(len(equation_template)) if equation_template[i]==""]
    found = False

    for comb in product(["+","*"],repeat=len(operator_indices)):
        
        if (found):
            break
        
        equation = equation_template.copy()
        
        for i in range(len(comb)):
            equation[operator_indices[i]] = comb[i]
        
        result = evaluate(equation)
        
        if(test_val == result):
            answer += result
            found = True
            break  

print(answer)         
