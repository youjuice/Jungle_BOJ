from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
students = [[] for _ in range(N + 1)]
deg = [0] * (N + 1)
q = deque()
result = []

for _ in range(M):
    a, b = map(int, input().split())
    students[a].append(b)
    deg[b] += 1

for i in range(1, N + 1):
    if deg[i] == 0:
        q.append(i)

while q:
    curr = q.popleft()
    result.append(curr)

    for i in students[curr]:
        deg[i] -= 1
        if deg[i] == 0:
            q.appendleft(i)

print(*result)
