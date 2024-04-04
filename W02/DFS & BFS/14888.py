from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
xy = list(map(int, input().split()))
xy_list, result_list = [], []
max_result, min_result = float('-inf'), float('inf')

for index, value in enumerate(xy):
    xy_list.extend([index] * value)


def solve(nums, xy):
    result = nums[0]

    for i in range(N-1):
        if xy[i] == 0:
            result += nums[i+1]
        elif xy[i] == 1:
            result -= nums[i+1]
        elif xy[i] == 2:
            result *= nums[i+1]
        elif xy[i] == 3:
            result = int(result / nums[i + 1])

    return result


xy_list_combi = list(permutations(xy_list, len(xy_list)))
for combi in xy_list_combi:
    solve(nums, combi)
    result_list.append(solve(nums, combi))

max_result = max(result_list)
min_result = min(result_list)

print(max_result)
print(min_result)
