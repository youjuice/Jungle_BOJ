K = int(input())
graph = []

for i in range(K):
    V, E = map(int, input().split())
    g = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)
    graph.append(g)


def dfs(graph, start, visited, index):
    if visited[start] != 0:
        return visited[start] == index

    visited[start] = index
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, -index)
    else:
        return False


for i in range(K):
    visited = [0] * (len(g) + 1)
    if dfs(graph, 1, visited, 1) is False:
        print('NO')
    else:
        print('YES')
