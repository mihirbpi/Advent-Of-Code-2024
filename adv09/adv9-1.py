from aocd import get_data

data = list(map(int,get_data(year=2024, day=9)))
data_new = []

for i in range(0,len(data)):
    
    if (i % 2 == 0):
        data_new.append([i//2, data[i]])
    else:
        data_new.append({".":data[i]})

for i in range(len(data_new)-1,-1,-2):

    for j in range(1,i+1,2):
        
        if (data_new[j]['.'] > 0):
            
            if (data_new[j]['.'] <= data_new[i][1]):
                data_new[i][1] -= data_new[j]['.']
                data_new[j][data_new[i][0]] = data_new[j]['.']
                data_new[j]['.'] = 0
            else:
                data_new[j][data_new[i][0]] = data_new[i][1]
                data_new[j]['.'] -= data_new[i][1]
                data_new[i][1] = 0

result = []

for i in range(len(data_new)):
    
    if (i%2 == 0):
        result.extend(data_new[i][1] * [data_new[i][0]])
    else:
        filled = []
        
        for key in data_new[i]:
            
            if (key != '.'):
                filled.extend(data_new[i][key]*[key])
                
        filled = list(sorted(filled, reverse=True))
        result.extend(filled)
        
checksum = sum([i*result[i] for i in range(len(result))])
print(checksum)