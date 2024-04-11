import sys
input = sys.stdin.readline

step_cnt = int(input())
step_list = [0] * (step_cnt + 1)
for i in range(1, step_cnt + 1):
    step_list[i] = int(input())

dp = [0] * (step_cnt + 1)

if step_cnt == 1:
    dp[1] = step_list[1]
elif step_cnt == 2:
    dp[2] = step_list[1] + step_list[2]
elif step_cnt == 3:
    dp[3] = max(step_list[1] + step_list[3], step_list[2] + step_list[3])

else:
    dp[1] = step_list[1]
    dp[2] = step_list[1] + step_list[2]
    dp[3] = max(step_list[1] + step_list[3], step_list[2] + step_list[3])

    for i in range(4, step_cnt + 1):
        dp[i] = max(dp[i - 2] + step_list[i], dp[i - 3] + step_list[i] + step_list[i - 1])

print(dp[step_cnt])
