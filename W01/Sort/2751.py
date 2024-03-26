def divide(ex_list):
    if len(ex_list) == 1:
        return ex_list

    mid = len(ex_list) // 2
    left = divide(ex_list[:mid])
    right = divide(ex_list[mid:])

    return merge(left, right)


def merge(left, right):
    merge_list = []
    right_num, left_num = 0, 0 

    while len(left) > left_num and len(right) > right_num:
        if left[left_num] <= right[right_num]:
            merge_list.append(left[left_num])
            left_num += 1
        else:
            merge_list.append(right[right_num])
            right_num += 1

    merge_list.extend(left[left_num:])
    merge_list.extend(right[right_num:])

    return merge_list

N = int(input())
n_list = [int(input()) for i in range(1, N+1)]

result = divide(n_list)
for num in result:
    print(num)


# import sys
#
# N = int(sys.stdin.readline())
# n_list = [int(sys.stdin.readline()) for i in range(1, N+1)]
#
# result = sorted(n_list)
#
# for num in result:
#     print(num)
