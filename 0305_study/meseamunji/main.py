import sys
sys.stdin = open("input.txt", "r")

from collections import deque

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

air_converter = []

for i in range(R):
    if arr[i][0] == -1:
        air_converter.append(i)

while T:
    T -= 1

    Q = deque()

    for i in range(R):
        for j in range(C):
            if arr[i][j] >= 5:
                Q.append((i, j, arr[i][j]//5))

    while Q:
        r, c, move_dust = Q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] != -1:
                arr[r][c] -= move_dust
                arr[nr][nc] += move_dust

    end_dust = deque()

    # 공기 청정 출발
    for i in range(air_converter[0], air_converter[1]+1):
        # 마지막 먼지 리스트에 추가
        end_dust.append(arr[i][C-1])
        for j in range(C-1, 1, -1):
            arr[i][j] = arr[i][j-1]
        # 공기 청정기 바로 앞쪽은 0
        arr[i][1] = 0

    # 우측 최상단, 최하단 추가
    end_dust.append(arr[0][C - 1])
    end_dust.append(arr[R - 1][C - 1])

    for i in range(0, air_converter[0]):
        if i == air_converter[0]-1:
            arr[i][C-1] = end_dust.popleft()
        else:
            arr[i][C - 1] = arr[i + 1][C - 1]

    for i in range(R-1, air_converter[1], -1):
        if i == air_converter[1]+1:
            arr[i][C-1] = end_dust.popleft()
        else:
            arr[i][C - 1] = arr[i - 1][C - 1]

    end_dust.append(arr[0][0])
    end_dust.append(arr[R-1][0])

    for i in range(C-1):
        if i == C-2:
            arr[0][C-2] = end_dust.popleft()
        else:
            arr[0][i] = arr[0][i+1]

    for i in range(C-1):
        if i == C-2:
            arr[R-1][C-2] = end_dust.popleft()
        else:
            arr[R-1][i] = arr[R-1][i+1]

    # 공기 청정
    arr[air_converter[0]-1][0] = 0
    arr[air_converter[1]+1][0] = 0

    for i in range(air_converter[0]-1, 0, -1):
        if i == 1:
            arr[i][0] = end_dust.popleft()
        else:
            arr[i][0] = arr[i-1][0]

    for i in range(air_converter[1]+1, R-1):
        if i == R-2:
            arr[i][0] = end_dust.popleft()
        else:
            arr[i][0] = arr[i+1][0]

dust_cnt = 0

for i in range(R):
    for j in range(C):
        if arr[i][j] > 0:
            dust_cnt += arr[i][j]

print(dust_cnt)