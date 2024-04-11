import sys
input = sys.stdin.readline

N = int(input())
Map = []

for _ in range(N):
    Map.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for x in range(N):
    for y in range(N):
        if x == N - 1 and y == N - 1:
            print(dp[x][y])
            sys.exit()

        score = Map[x][y]
        for dx, dy in [(0, 1), (1, 0)]:
            nx, ny = x + dx * score, y + dy * score
            if 0 <= nx < N and 0 <= ny < N:
                dp[nx][ny] += dp[x][y]
