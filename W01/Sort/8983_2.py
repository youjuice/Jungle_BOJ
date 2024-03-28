import sys
input = sys.stdin.readline

M, N, L = map(int, input().split())
shots = list(map(int, input().split()))
animals = []

for i in range(N):
    a, b = map(int, input().split())
    animals.append((a, b))

count = 0
shots.sort()

for a, b in animals:
    if b > L:
        continue

    Min = a + b - L
    Max = a - b + L

    for z in range(len(shots)):
        if Min <= shots[z] <= Max:
            count += 1
            break

print(count)

