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

    start = 0
    end = len(shots) - 1

    while start <= end:
        mid = (start + end) // 2
        if Min <= shots[mid] <= Max:
            count += 1
            break

        elif shots[mid] < Max:
             start = mid + 1

        else:
            end = mid - 1

print(count)

