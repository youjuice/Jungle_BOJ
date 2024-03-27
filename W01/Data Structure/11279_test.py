# 출력은 구현 됐지만 시간 초과 및 오류가 있는 코드
N = int(input())
pri_queue = []


def Heapify(arr, index, heap_size):
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if left < heap_size and arr[left] > arr[largest]:
        largest = left
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    if largest != index:
        arr[index], arr[largest] = arr[largest], arr[index]
        Heapify(arr, largest, heap_size)    # 하위 서브트리를 힙으로 만든다.

for _ in range(N):
    x = int(input())

    if x > 0:
        pri_queue.append(x)
        Heapify(pri_queue, 0, len(pri_queue))
    elif x == 0:
        if len(pri_queue) > 0:
            print(pri_queue.pop(0))
            Heapify(pri_queue, 0, len(pri_queue))
        else:
            print(0)

