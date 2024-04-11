import sys
input = sys.stdin.readline

N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]
dp[1] = [0] + [1] * 9

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:      # 0으로 끝나는 경우
            dp[i][j] = dp[i - 1][1]
        elif j == 9:    # 9로 끝나는 경우
            dp[i][j] = dp[i - 1][8]
        else:           # 1 ~ 8로 끝나는 경우
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1000000000)
