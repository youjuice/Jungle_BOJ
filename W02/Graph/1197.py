import sys
input = sys.stdin.readline

V, E = map(int, input().split())

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))
edges.sort(key=lambda x: x[2])

parent = [i for i in range(V + 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])
    return parent[x]


def union(x, y):
    x_parent = get_parent(x)
    y_parent = get_parent(y)

    if x < y:
        parent[y_parent] = x_parent
    else:
        parent[x_parent] = y_parent


def same_parent(x, y):
    return get_parent(x) == get_parent(y)

answer = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union(a, b)
        answer += cost

print(answer)
