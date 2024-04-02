import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    global count
    queue = deque([(x, y, 1)])
    visited[x][y] = 1

    while queue:
        x, y, dist = queue.popleft()
        if x == N - 1 and y == M - 1:
            return dist
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0 and miro[nx][ny] == 1:
                queue.append((nx, ny, dist + 1))
                visited[nx][ny] = 1
    return -1

N, M = map(int, input().split())
miro = [list(map(int, input().strip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

print(bfs(0, 0))
