from aocd import get_data

data = get_data(year=2024, day=13).split("\n\n")

def solve(a_coeff_x, a_coeff_y, b_coeff_x, b_coeff_y, prize_x, prize_y):
    min_cost = 1e99
    D =  a_coeff_x * b_coeff_y - a_coeff_y * b_coeff_x

    if (D == 0):
        return min_cost
    
    D_a = prize_x * b_coeff_y - b_coeff_x * prize_y
    D_b = a_coeff_x * prize_y - prize_x * a_coeff_y
    
    a = D_a / D
    b = D_b / D
    
    if (int(a) != a or int(b) != b):
        return min_cost

    else:
        return int(3*a + b)

tokens_spent = 0
for machine_info_string in data:
    A_info, B_info, prize_info = machine_info_string.split("\n")
    a_coeff_x = int(A_info.split(" ")[2].split("+")[1][:-1])
    a_coeff_y = int(A_info.split(" ")[3].split("+")[1])
    b_coeff_x = int(B_info.split(" ")[2].split("+")[1][:-1])
    b_coeff_y = int(B_info.split(" ")[3].split("+")[1])
    prize_x = int(prize_info.split(" ")[1].split("=")[1][:-1])
    prize_y = int(prize_info.split(" ")[2].split("=")[1])
    offset = 10000000000000
    solution = solve(a_coeff_x, a_coeff_y, b_coeff_x, b_coeff_y, prize_x+offset, prize_y+offset)
    
    if (solution < 1e99):
        tokens_spent += solution

print(tokens_spent)