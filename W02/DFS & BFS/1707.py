import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(graph, start, visited, index):
    if visited[start] != 0:                 # 현재 노드가 이미 방문되었는지 확인
        return visited[start] == index      # 이미 할당된 색과 현재 색이 같은지를 확인하여 이분 그래프 여부 판별

    visited[start] = index                                      # 현재 노드에 색 할당
    for neighbor in graph[start]:                               # 현재 노드와 인접한 이웃 노드에 대해
        if visited[neighbor] == 0:                              # 만약 방문한 적이 없다면
            if not dfs(graph, neighbor, visited, -index):       # 함수 재귀 호출 (현재 노드와 다른 색을 할당하여 호출)
                return False
        elif visited[neighbor] == visited[start]:               # 인접한 노드가 이미 방문되었고, 색이 현재 노드와 같다면
            return False                                        # False 반환
    return True                                                 # 위의 조건을 모두 통과하면, True 반환


K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [0] * (V + 1)
    is_right = True
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not dfs(graph, i, visited, 1):
                is_right = False
                break

    if is_right:
        print('YES')
    else:
        print('NO')
