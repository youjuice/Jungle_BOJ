import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [list(input().strip()) for _ in range(N)]
visited = [[False] * M for _ in range(N + 1)]
count = 0


# 왜 안되는지 도저히 모르겠음... 계속 0이 나옴
def dfs(graph, x, y):
    visited[x][y] = True

    if graph[x][y] == '_':
        if not visited[x + 1][y] and x + 1 < N and graph[x + 1][y] == '_':
            dfs(graph, x + 1, y)
        else:
            return

    if graph[x][y] == '|':
        if not visited[x][y + 1] and y + 1 < M and graph[x][y + 1] == '|':
            dfs(graph, x, y + 1)
        else:
            return

for i in range(N):
    for j in range(M):
        if visited[i][j] is False:
            dfs(floor, i, j)
            count += 1

print(count)
