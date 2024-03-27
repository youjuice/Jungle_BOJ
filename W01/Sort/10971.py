import sys
input = sys.stdin.readline

N = int(input())
Map = [list(map(int, input().split())) for _ in range(N)]

visited = [False] * N           # 방문 체크
min_cost = float('inf')         # 최소 비용을 업데이트 할 것이므로 무한으로 초기화


def visit(start, next, cost, visited):
    global min_cost
    if len(visited) == N:                           # 순회가 끝나면,
        tmp = Map[next][start]                      # 다시 시작 노드로 돌아가는 비용 추가
        if tmp != 0:                                # 간선이 존재할 때
            min_cost = min(min_cost, cost + tmp)    # 최소 비용 업데이트
        return

    for i in range(N):
        tmp = Map[next][i]                          # 현재 노드에서 다음 노드로의 비용
        if tmp != 0 and i not in visited and cost < min_cost:
            visited.append(i)                       # 방문 체크
            visit(start, i, cost + tmp, visited)    # 재귀적으로 탐색
            visited.remove(i)                       # 백트래킹

for i in range(N):
    visit(i, i, 0, [i])

print(min_cost)
