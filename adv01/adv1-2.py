from aocd import get_data

data = get_data(year=2024, day=1).split("\n")

left, right = [sorted([list(map(int,x.split("   ")))[i] for x in data]) for i in [0,1]]

print(sum([left[i]*right.count(left[i]) for i in range(len(left))]))