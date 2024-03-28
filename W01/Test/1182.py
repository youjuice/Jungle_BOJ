from itertools import combinations
import sys
input = sys.stdin.readline


def solve(numbers, num_sum):
    count = 0
    for i in range(1, len(numbers) + 1):
        for combi in combinations(numbers, i):
            if sum(combi) == num_sum:
                count += 1
    return count


N, S = map(int, input().split())
A = list(map(int, input().split()))

print(solve(A, S))
