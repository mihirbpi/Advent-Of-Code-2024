from aocd import get_data

data = get_data(year=2024, day=17).split("\n")
regA = int(data[0].split("Register A: ")[1])
regB = int(data[1].split("Register B: ")[1])
regC = int(data[2].split("Register C: ")[1])
program = list(map(int,data[4].split("Program: ")[1].split(",")))
output = ""

def combo(operand, reg_values):
    
    if (operand in [4,5,6]):
        return reg_values[[4,5,6].index(operand)]
    
    return operand

instr_ptr = 0

while(instr_ptr < len(program)):
    opcode, operand = program[instr_ptr], program[instr_ptr+1]
        
    if (opcode == 0):
        regA = regA // (2**combo(operand, [regA, regB, regC]))
        instr_ptr += 2
    
    if (opcode == 1):
        regB = regB ^ operand
        instr_ptr += 2
        
    if (opcode == 2):
        regB = combo(operand, [regA, regB, regC]) % 8
        instr_ptr += 2
        
    if (opcode == 3):
        
        if regA == 0:
            instr_ptr += 2
        else:
            instr_ptr = operand
            
    if (opcode == 4):
        regB = regB ^ regC
        instr_ptr += 2
    
    if (opcode == 5):
        output += str(combo(operand, [regA, regB, regC]) % 8)+","
        instr_ptr += 2
    
    if (opcode == 6):
        regB = regA // (2**combo(operand, [regA, regB, regC]))
        instr_ptr += 2
    
    if (opcode == 7):
        regC = regA // (2**combo(operand, [regA, regB, regC]))
        instr_ptr += 2  
        
print(output[:-1])    
    
        
    
        
        