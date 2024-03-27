import sys
input = sys.stdin.readline

N = int(input())
tops = list(map(int, input().split()))
stack = []

result = []

for i in range(N):
    while stack:
        if stack[-1][1] > tops[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    if not stack:
        result.append(0)
    stack.append((i, tops[i]))

print(*result)
