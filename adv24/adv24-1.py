from aocd import get_data
from functools import lru_cache

data = get_data(year=2024, day=24).split("\n\n")
#data = open("test.txt", "r").read().split("\n\n")

outputs_dict = {}
instructions_dict = {}

for line in data[0].split("\n"):
    line_split = line.split(": ")
    gate, input = line_split[0], int(line_split[1])
    outputs_dict[gate] = input

for line in data[1].split("\n"):
    instruction, gate = line.split(" -> ")
    instructions_dict[gate] = instruction
    
@lru_cache(None)
def get_output(instruction, gate):
    
    if gate in outputs_dict:
        return outputs_dict[gate]
    
    gate1, op, gate2 = instruction.split(" ")
    out1, out2 = None, None
    
    if (gate1 in outputs_dict):
        out1 = outputs_dict[gate1]
    else:
        out1 = get_output(instructions_dict[gate1],gate1) 
        
    if (gate2 in outputs_dict):
        out2 = outputs_dict[gate2]
    else:
        out2 = get_output(instructions_dict[gate2],gate2) 
    
    if (op == 'XOR'):
        return out1 ^ out2
    if (op == 'OR'):
        return out1 | out2
    if (op == 'AND'):
        return out1 & out2

for gate in instructions_dict:
    outputs_dict[gate] = get_output(instructions_dict[gate],gate)

z_outs = [(x,outputs_dict[x]) for x in outputs_dict if x[0] == "z"]
z_outs = sorted(z_outs, key=lambda x: x[0], reverse=True)
bin_string = "".join([str(x[1]) for x in z_outs])
print(int(bin_string,2))