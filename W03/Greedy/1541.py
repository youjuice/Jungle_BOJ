num = input().split('-')

sum_list = []

for i in num:
    sum = 0
    tmp = i.split('+')

    for j in tmp:
        sum += int(j)
    sum_list.append(sum)

n = sum_list[0]

for i in range(1, len(sum_list)):
    n -= sum_list[i]

print(n)