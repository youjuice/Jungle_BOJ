import heapq
import sys

input = sys.stdin.readline

N = int(input())
num_list = [int(input()) for _ in range(N)]

leftHeap = []
rightHeap = []
answer = []

for num in num_list:
    if len(leftHeap) == len(rightHeap):
        heapq.heappush(leftHeap, -num)      # 중간값을 기준으로 작은 값
    else:
        heapq.heappush(rightHeap, num)      # 중간값을 기준으로 큰 값

    if rightHeap and -leftHeap[0] > rightHeap[0]:
        right_min = heapq.heappop(rightHeap)
        left_max = -heapq.heappop(leftHeap)
        heapq.heappush(leftHeap, -right_min)
        heapq.heappush(rightHeap, left_max)

    answer.append(-leftHeap[0])

for num in answer:
    print(num)