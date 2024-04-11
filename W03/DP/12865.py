import sys
input = sys.stdin.readline

N, K = map(int, input().split())
stuff = [[0, 0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    stuff.append([a, b])

for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0]
        value = stuff[i][1]

        # 현재 물건을 배낭에 넣을 수 있는지 확인하고, 가능하다면 최대 가치 갱신
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]     # 현재 물건의 무게보다 배낭의 용량이 작으면 이전 상태를 그대로 가져옵니다.
        else:   # 현재 물건을 넣을 수 있을 때, 넣는 경우와 안 넣는 경우 중 더 큰 가치를 선택
            knapsack[i][j] = max(knapsack[i - 1][j - weight] + value, knapsack[i - 1][j])

print(knapsack[N][K])
