import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N)]
for _ in range(M):
    from_node, to_node, cost = map(int, input().split())
    graph[from_node - 1].append((to_node - 1, cost))    # graph[1] = (2, 2), (3, 3), (노드, 비용)
start, end = map(int, input().split())
start -= 1


def dijkstra(graph, start):
    dist_list = [float('inf') for _ in range(N)]
    dist_list[start] = 0

    dijk_heap = []
    heapq.heappush(dijk_heap, (start, 0))

    while dijk_heap:
        curr_node, curr_dist = heapq.heappop(dijk_heap)

        if dist_list[curr_node] < curr_dist:
            continue

        for neighbor in graph[curr_node]:
            node, weight = neighbor[0], neighbor[1]
            min_dist = curr_dist + weight
            if min_dist < dist_list[node]:
                dist_list[node] = min_dist
                heapq.heappush(dijk_heap, (node, dist_list[node]))
    return dist_list[end-1]

print(dijkstra(graph, start))
