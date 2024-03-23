N = int(input())
visited = [0] * N
up_cross = [0] * (2*N-1)       # / 대각선 2N-1개
down_cross = [0] * (2*N-1)     # \ 대각선 2N-1개
count = 0


def queens(i):
    global count
    if i == N:
        count += 1
        return
    for j in range(N):
        if visited[j] == 1:     # 방문 여부 체크
            continue

        a = i + j               # up_cross 라벨링
        b = i - j               # down_cross 라벨링

        if up_cross[a] == 1 or down_cross[b] == 1:      # 대각선 체크
            continue

        visited[j] = up_cross[a] = down_cross[b] = 1    # 방문 체크
        queens(i + 1)
        visited[j] = up_cross[a] = down_cross[b] = 0    # 백트래킹!!

queens(0)
print(count)

