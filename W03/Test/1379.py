N = int(input())
lectures = []
for _ in range(N):
    num, start, end = list(map(int, input().split()))
    lectures.append([num, start, end])

lectures.sort(key=lambda x: (x[1], x[2]))

count = 1
end = lectures[0][1]
for i in range(1, N):
    if lectures[i][0] >= end:
        count += 1
        end = lectures[i][1]

print(count)
