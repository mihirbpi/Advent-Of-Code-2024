from aocd import get_data
from functools import lru_cache

data = get_data(year=2024, day=24).split("\n\n")
data = open("test.txt", "r").read().split("\n\n")

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
    
def get_next_adder(carry_out, sum):
    if (carry_out not in instructions_dict):
        print(f"carry_out: {carry_out} not in instructions dict")
        return
    
    if (sum not in instructions_dict):
        print(f"sum: {sum} not in instructions dict")
        return
    carry_out_inputs = instructions_dict[carry_out]
    
    if ("OR" not in carry_out_inputs):
        print(f"OR not in carry_out_inputs: {carry_out_inputs} for carry_out: {carry_out} and sum: {sum}")
        return
    sum_inputs = instructions_dict[sum]
    
    if ("XOR" not in sum_inputs):
        print(f"XOR not in sum_inputs: {sum_inputs} for carry_out: {carry_out} and sum: {sum}")
        return
    
    bit_input = None
    bit_input_inputs = []
    and_input = None
    and_input_inputs = []
    input1, input2 = list(sorted(carry_out_inputs.split(" OR ")))
    suminput1, suminput2 = list(sorted(sum_inputs.split(" XOR ")))
    
    if (input1 not in instructions_dict):
        print(f"carry out input: {input1} not in instructions dict for carry_out: {carry_out} and sum: {sum}")
        return
    
    if (input2 not in instructions_dict):
        print(f"carry out input: {input2} not in instructions dict for carry_out: {carry_out} and sum: {sum}")
        return
                    
    if ((f"x{sum[1:]} AND y{sum[1:]}" == instructions_dict[input1]) or (f"y{sum[1:]} AND x{sum[1:]}" == instructions_dict[input1])):
        bit_input_inputs = list(sorted([f"x{sum[1:]}", f"y{sum[1:]}"]))
        bit_input = input1
    elif ((f"x{sum[1:]} AND y{sum[1:]}" == instructions_dict[input2]) or (f"y{sum[1:]} AND x{sum[1:]}" == instructions_dict[input2])):
        bit_input_inputs = list(sorted([f"x{sum[1:]}", f"y{sum[1:]}"]))
        bit_input = input2
        
    if not bit_input:
        print(f"bit input inputs not found for input1: {input1} and input2: {input2} for carry_out: {carry_out} and sum: {sum}")
        return
    to_check_and_input = None
    to_check_and_input = input1
    if (bit_input == input1):
        to_check_and_input = input2
    
    if (("AND" in instructions_dict[to_check_and_input])):
        and_input_inputs = list(sorted(instructions_dict[to_check_and_input].split(" AND ")))
        
        if (and_input_inputs == [suminput1, suminput2]):
            and_input = to_check_and_input
        else:
            print(f"and_input_inputs: {and_input_inputs} for and_input: {to_check_and_input} do not match sum inputs: {[suminput1, suminput2]} for carry_out: {carry_out} and sum: {sum}")
            return
    if (not and_input):
        print(f"AND/and_input_inputs not found for input1: {input1} and input2: {input2} for carry_out: {carry_out} and sum: {sum}")
        return   
    # print(bit_input, bit_input_inputs)
    # print(and_input, and_input_inputs)
    
    and_input_input1, and_input_input2 = and_input_inputs
    xor_output = None
    
    if ((f"x{sum[1:]} XOR y{sum[1:]}" == instructions_dict[and_input_input1]) or (f"y{sum[1:]} XOR x{sum[1:]}" == instructions_dict[and_input_input1])):
        xor_output = and_input_input1
    elif ((f"x{sum[1:]} XOR y{sum[1:]}" == instructions_dict[and_input_input2]) or (f"y{sum[1:]} XOR x{sum[1:]}" == instructions_dict[and_input_input2])):
        xor_output = and_input_input2
    
    if (not xor_output):
        print(f"XOR output not found for and_input_input1: {and_input_input1} and and_input_input2: {and_input_input2} for and_input: {and_input} for carry_out: {carry_out} and sum: {sum}")
        return  
    
    or_ouput = None
    to_check_or_output = None
    to_check_or_output = and_input_input2
    if (xor_output == and_input_input2):
        to_check_or_output = and_input_input1
        
    if ("OR" in instructions_dict[to_check_or_output]):
        or_output = to_check_or_output 
        
    if (not or_output):
        print(f"OR output not found for to_check_or_output: {to_check_or_output} for and_input_input1: {and_input_input1} and and_input_input2: {and_input_input2} for and_input: {and_input} for carry_out: {carry_out} and sum: {sum}")
        return
    print(f"get_next_adder('{or_output}','z{str(int(sum[1:])-1)}')")
    return f"get_next_adder('{or_output}','z{str(int(sum[1:])-1)}')"

# get_next_adder("z45","z44")
# get_next_adder('ftb','z43')
# get_next_adder('qgm','z42')
# get_next_adder('sdk','z41')
# get_next_adder('dcd','z40')
# get_next_adder('jhd','z39')
# get_next_adder('mhr','z38')
# get_next_adder('gft','z37')
# get_next_adder('wdr','z36')
# get_next_adder('prt','z35')
# get_next_adder('rtj','z34')
# get_next_adder('ghp','z33')
# get_next_adder('mvc','z32')
# get_next_adder('nwt','z31')
# get_next_adder('dfm','z30')
# get_next_adder('vhs','z29')
# get_next_adder('mgr','z28')
# get_next_adder('shk','z27')
# get_next_adder('kkb','z26')
# get_next_adder('pcf','z25')
# get_next_adder('hnd','z24')
# get_next_adder('bvg','z23')
# get_next_adder('nkp','z22')
# get_next_adder('hhc','z21')
# get_next_adder('scj','z20')
# get_next_adder('qfd','z19')
# get_next_adder('nwb','z18')
# get_next_adder('fnb','z17')
# get_next_adder('nsj','z16')
# get_next_adder('nwk','z15')
# get_next_adder('fkn','z14')
# get_next_adder('jmk','z13')
# get_next_adder('vjt','z12')
# get_next_adder('jjs','z11')
# get_next_adder('tdj','z10')
# get_next_adder('whd','z09')
# get_next_adder('bgn','z08')
# get_next_adder('twg','z07')
# get_next_adder('tfg','z06')
# get_next_adder('vdv','z05')
# get_next_adder('wcr','z04')
# get_next_adder('sdf','z03')
# get_next_adder('jrj','z02')

# gates = list(instructions_dict.keys())
# for gate in gates:
#     old_z = instructions_dict['z10'] 
#     old_gate = instructions_dict[gate]
#     if("XOR" in instructions_dict[gate]):
#         instructions_dict['z10'] = instructions_dict[gate]
#         instructions_dict[gate] = old_z
#     try:
#         if (get_next_adder('tdj','z10') and "get_next_adder" in get_next_adder('tdj','z10')):
#             print(gate)
#             break
#     except ValueError:
#         instructions_dict[gate] = old_gate
#         instructions_dict['z10'] = old_z    
#     instructions_dict[gate] = old_gate
#     instructions_dict['z10'] = old_z

# print(",".join(sorted(["cpm", "krs", "ghp", "z33", "nks", "z21", "z10", "gpr"])))