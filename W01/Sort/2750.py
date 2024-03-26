N = int(input())
n_set = set(int(input()) for i in range(1, N+1))

result = sorted(n_set)
for num in result:
    print(num)