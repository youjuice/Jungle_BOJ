import sys
import heapq

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())

    if x == 0:      # 0을 입력하면 최댓값 출력
        if heap:
            print(-heapq.heappop(heap))

        else:
            print(0)
    else:           # 최소 힙을 최대 힙으로 쓰기 위해 -를 붙여줌
        heapq.heappush(heap, -x)
