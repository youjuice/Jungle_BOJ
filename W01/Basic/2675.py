T = int(input())

for i in range(T):
    R, S = input().split()
    for s in S:
        print(int(R) * s, end='')
    print()