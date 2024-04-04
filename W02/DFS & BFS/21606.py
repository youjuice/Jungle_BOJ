import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N = int(input())
A = input().rstrip()
graph = [[] for _ in range(N+1)]
place = [0] + [int(x) for x in A]                                   # 실내인지 실외인지 입력 받음
visited = [False] * (N+1)
answer = 0

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

    if place[a] == 1 and place[b] == 1:                             # 둘 다 실내라면
        answer += 2                                                 # 서로 방문하는 경우 추가 (+2)


def dfs(node):                                                      # 정점 번호
    visited[node] = True                                            # 방문 처리
    inside = 0                                                      # 실내 개수 카운트
    for neighbor in graph[node]:                                    # 이웃 노드에 대해서
        if place[neighbor] == 1:                                    # 이웃 노드가 실내라면
            inside += 1                                             # 실내 개수 +1
        elif not visited[neighbor] and place[neighbor] == 0:        # 방문한 적 없고 해당 위치가 실외라면,
            inside += dfs(neighbor)                                 # 해당 실외 노드에서 dfs
    return inside

for i in range(1, N+1):
    if place[i] == 0 and not visited[i]:                            # 실외 노드를 기준으로
        in_cnt = dfs(i)                                             # 주변 실내 노드 계산
        answer += in_cnt * (in_cnt - 1)                             # 경우의 수 추가

print(answer)
