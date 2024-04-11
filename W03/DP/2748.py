import sys
input = sys.stdin.readline

n = int(input())
Fib_list = [0, 1]

for i in range(2, n+1):
    Fib_list.append(Fib_list[i-1] + Fib_list[i-2])

print(Fib_list[n])
