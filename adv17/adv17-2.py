from aocd import get_data

data = get_data(year=2024, day=17).split("\n")
program = list(map(int,data[4].split("Program: ")[1].split(",")))

def combo(operand, reg_values):
    
    if (operand in [4,5,6]):
        return reg_values[[4,5,6].index(operand)]
    
    return operand

def run(regA_init, program):
    
    regA = regA_init
    regB = int(data[1].split("Register B: ")[1])
    regC = int(data[2].split("Register C: ")[1])
    
    output = ""
    
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
    
    return output

x = int("611755605224705", 8)
i = 0

while(True):
    output = run(8*x+i, program)
    
    if (output == "2,4,1,3,7,5,1,5,0,3,4,2,5,5,3,0,"):
        print(8*x+i,oct(8*x+i),output)
        break
    i += 1