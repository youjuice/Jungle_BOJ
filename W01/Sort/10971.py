N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N


for i in range(N):
    for j in range(N):
