import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    rank = sorted([list(map(int, input().split())) for _ in range(N)])

    count = 1
    interview_rank = rank[0][1]

    for i in range(1, N):
        if rank[i][1] < interview_rank:
            count += 1
            interview_rank = rank[i][1]

    print(count)
