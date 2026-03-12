import sys
sys.stdin = open("input.txt", "r")

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs(r, c, K_albe, lenth):
    global max_lenth
    max_lenth = max(max_lenth, lenth)

    visited[r][c] = 1

    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if arr[nr][nc] < arr[r][c]:
                dfs(nr, nc, K_albe, lenth+1)

            elif K_albe and arr[nr][nc] - K < arr[r][c]:
                before = arr[nr][nc]
                arr[nr][nc] = arr[r][c] - 1
                dfs(nr, nc, False, lenth+1)
                arr[nr][nc] = before

            # elif K_albe:
            #     for k in range(1, K+1):
            #         if arr[nr][nc] - k < arr[r][c]:
            #             before = arr[nr][nc]
            #             arr[nr][nc] -= k
            #             dfs(nr, nc, False, lenth+1)
            #             arr[nr][nc] = before

    visited[r][c] = 0

T = int(input())
for t_c in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    top = max(map(max, arr))

    top_list = []

    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:
                top_list.append((i, j))

    max_lenth = 0

    visited = [[0]*N for _ in range(N)]

    for r, c in top_list:
        dfs(r, c, True, 1)

    print(f'#{t_c} {max_lenth}')

