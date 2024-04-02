# 시간 초과 ㅋ
import sys
input = sys.stdin.readline


def dijkstras(graph, start):
    shortest_path = [float('inf')] * (N + 1)
    shortest_path[start] = 0
    visited = [False] * (N + 1)

    for _ in range(N):
        min_dist = float('inf')
        min_node = -1

        for i in range(1, N + 1):
            if not visited[i] and shortest_path[i] < min_dist:
                min_dist = shortest_path[i]
                min_node = i

        visited[min_node] = True

        for cost, next_node in graph[min_node]:
            if shortest_path[min_node] + cost < shortest_path[next_node]:
                shortest_path[next_node] = shortest_path[min_node] + cost

    return shortest_path


N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append((1, end))

result = dijkstras(graph, X)
answer = [node for node, dist in enumerate(result) if dist == K]

if answer:
    for node in answer:
        print(node)
else:
    print(-1)

