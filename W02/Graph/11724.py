import sys
input = sys.stdin.readline


def dfs(start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(neighbor for neighbor in graph[vertex] if neighbor not in visited)
    return visited

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
visited = set()
count = 0

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

for i in range(1, N+1):
    if i not in visited:
        visited.update(dfs(i))
        count += 1

print(count)
