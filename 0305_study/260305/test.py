# import sys
# sys.stdin = open('input_bi2.txt', 'r')
#
# T = int(input())
# for t_c in range(1, T+1):
#     N = float(input())
#
#     result = ''
#
#     while N > 0:
#         if len(result)>12:
#             result = 'overflow'
#             break
#
#         N *= 2
#
#         if N>=1:
#             result += '1'
#             N -= 1
#         else:
#             result += '0'
#
#     print(f'#{t_c} {result}')
from collections import deque


def get_work(i, visited):
    Q = deque([i])
    visited[i] = True
    cur_day = i
    earn = 0

    while Q:
        d = Q.popleft()
        cur_day += work_time[d]
        earn += work_pay[d]
        if cur_day-1 > n:
            return earn
        else:
            for k in range(cur_day, n+1):
                Q.append(k)

    return earn





n = int(input())

work_time = [-1]*(n+1)
work_pay = [-1]*(n+1)

for day in range(1, n+1):
    t, p = map(int, input().split())
    if day+t-1 > n:
        continue
    work_time[day] = t
    work_pay[day] = p

visited = [False] * (n+1)

earn_list = []

for i in range(1, n+1):
    if work_time[i] != -1 and not visited:
        howmany = get_work(i, visited)
        earn_list.append(howmany)

print(max(earn_list))