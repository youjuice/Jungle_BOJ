import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = {i: [] for i in range(1, N + 1)}
visited = set()

for i in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)


def dfs(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)
    return visited

print(len(dfs(1)) - 1)
