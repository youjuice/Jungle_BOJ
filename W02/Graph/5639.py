import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

num_list = []

while True:
    try:
        n = int(input())
        num_list.append(n)
    except:
        break


def solve(graph):
    if len(graph) == 0:
        return

    tmp_left, tmp_right = [], []
    mid = graph[0]

    for i in range(1, len(graph)):
        if graph[i] > mid:
            tmp_left = graph[1:i]
            tmp_right = graph[i:]
            break

    else:
        tmp_left = graph[1:]

    solve(tmp_left)
    solve(tmp_right)
    print(mid)

solve(num_list)

