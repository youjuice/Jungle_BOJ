import sys
input = sys.stdin.readline

N = int(input())
time = [[0] * 2 for _ in range(N)]

for i in range(N):
    a, b = map(int, input().split())
    time[i][0] = a
    time[i][1] = b

# 끝나는 시간을 기준으로 정렬. 끝나는 시간이 같다면 시작 시간이 빠른 순으로 정렬
time.sort(key=lambda x: (x[1], x[0]))

count = 1
end = time[0][1]            # 첫번째 활동의 끝나는 시간 저장
for i in range(1, N):
    if time[i][0] >= end:   # 현재 활동의 시작 시간이 이전 활동의 끝나는 시간보다 크거나 같으면 선택
        count += 1          # 선택된 활동의 개수 증가
        end = time[i][1]    # 선택된 활동의 끝나는 시간 갱신

print(count)
