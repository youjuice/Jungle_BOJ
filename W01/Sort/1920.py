N = int(input())
N_list = set(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for M_value in M_list:
    if M_value in N_list:
        print(1)
    else:
        print(0)