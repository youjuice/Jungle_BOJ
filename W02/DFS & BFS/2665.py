from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
d = [[0, 1], [1, 0], [0, -1], [-1, 0]]

miro = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[-1] * N for _ in range(N)]


def bfs(graph):
    visited[0][0] = 0
    queue = deque()
    queue.append((0, 0))

    while queue:
        x, y = queue.popleft()
        if x == N-1 and y == N-1:                           # 도착점에 도달했는지 확인
            return visited[x][y]                            # 도착점까지의 거리 반환
        for i in range(4):
            nx, ny = x + d[i][0], y + d[i][1]               # 상하좌우로 이동
            # 만약 미로 안에 있고, 방문한 적이 없다면
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == -1:
                if graph[nx][ny] == 1:                      # 1. 만약 다음 칸이 흰 방이라면,
                    queue.appendleft((nx, ny))              # 흰 방 먼저 탐색하도록 appendleft
                    visited[nx][ny] = visited[x][y]         # 이전 칸과 개수 동일
                else:                                       # 2. 만약 다음 칸이 검은 방이라면,
                    queue.append((nx, ny))                  # 다음 칸을 큐에 추가
                    visited[nx][ny] = visited[x][y] + 1     # 바꿔야 할 검은 방 개수 +1

print(bfs(miro))
