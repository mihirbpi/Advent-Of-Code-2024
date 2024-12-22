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

def get_changes(secret_num, num_steps):
    changes = []
    new_secret_num = secret_num
    
    for _ in range(num_steps):
        old_secret_num = new_secret_num
        new_secret_num = next(new_secret_num)
        digit_old = old_secret_num % 10
        digit_new = new_secret_num % 10
        changes.append((digit_new, digit_new-digit_old))
        
    return changes

seq_bananas = {}

for secret_num in init:
    changes = get_changes(secret_num, 2000)
    diffs = [x[1] for x in changes]
    seen = set()
    
    for i in range(len(diffs)-4):
        seq = tuple(diffs[i:i+4])
        
        if (seq not in seen):
        
            if (seq in seq_bananas):
                seq_bananas[seq] += changes[i+3][0]
            else:
                seq_bananas[seq] = changes[i+3][0]
                
        seen.add(seq)
            
print(max(seq_bananas.values()))
