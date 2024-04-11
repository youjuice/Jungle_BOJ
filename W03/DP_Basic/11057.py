import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for i in range(N + 1)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]      # 점화식

print(sum(dp[N]) % 10007)

