from aocd import get_data

data = get_data(year=2024, day=22).split("\n")
init = list(map(int, data))

def mix(val, secret_num):
    return secret_num ^ val

def prune(secret_num):
    return secret_num % 16777216

def next(secret_num):
    next_secret_num = secret_num
    next_secret_num = mix(64*next_secret_num, next_secret_num)
    next_secret_num = prune(next_secret_num)
    next_secret_num = mix(next_secret_num//32, next_secret_num)
    next_secret_num = prune(next_secret_num)
    next_secret_num = mix(2048*next_secret_num, next_secret_num)
    next_secret_num = prune(next_secret_num)
    return next_secret_num

def evolve(secret_num, num_steps):
    final = secret_num
    
    for _ in range(num_steps):
        final = next(final)
        
    return final    

ans = sum([evolve(secret_num, 2000) for secret_num in init])   
print(ans)