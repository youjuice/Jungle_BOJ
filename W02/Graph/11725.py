import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def find(v, parent):
    parents[v] = parent
    for j in graph[v]:
        if parents[j] == 0:
            find(j, v)

n = int(input())
parents = [0] * (n+1)

graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

find(1, 0)

for i in range(2, n+1):
    print(parents[i])
