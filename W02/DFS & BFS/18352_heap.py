import sys
import heapq
input = sys.stdin.readline


def dijkstras(graph, start):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0

    pq = []
    heapq.heappush(pq, (0, start))

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        for neighbor in graph[curr_node]:
            weight, node = neighbor[0], neighbor[1]
            min_dist = curr_dist + weight
            if distance[node] > min_dist:
                distance[node] = min_dist
                heapq.heappush(pq, (distance[node], node))

    return distance


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

