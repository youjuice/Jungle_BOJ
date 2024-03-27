from collections import deque


def yo(N, K):
    circle = deque(range(1, N+1))
    result = []

    while circle:
        for _ in range(K-1):
            circle.append(circle.popleft())
        result.append(circle.popleft())

    return result

N, K = map(int, input().split())

result = yo(N, K)

print("<", end="")
print(", ".join(map(str, result)), end="")
print(">", end="")
