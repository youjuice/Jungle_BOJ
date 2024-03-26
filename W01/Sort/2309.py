from itertools import combinations
short = [int(input()) for _ in range(9)]

for combi in combinations(short, 7):
    if sum(combi) == 100:
        result = sorted(combi)
        print(*result, sep='\n')
        break
