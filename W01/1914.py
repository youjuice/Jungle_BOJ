def hanoi(n, start, end):
    if n > 1:
        hanoi(n-1, start, 6-start-end)

    print(f'{start} {end}')

    if n > 1:
        hanoi(n-1, 6-start-end, end)

N = int(input())

print(2**N - 1)

if N <= 20:
    hanoi(N, 1, 3)
