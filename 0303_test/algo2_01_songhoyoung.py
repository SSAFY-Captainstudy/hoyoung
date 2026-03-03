# 확인할 방향을 인덱스로 설정
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]

def mine(i, j):
    Q = [(i, j)]
    gold_cnt = 0
    mine_size = 0

    while Q:
        c, r = Q.pop(0)
        gold_cnt += arr[c][r]
        mine_size += 1
        for d in range(4):
            nc = c + dc[d]
            nr = r + dr[d]
            if 0<=nc<N and 0<=nr<N and not visited[nc][nr]:
                if arr[nc][nr] > 0:
                    Q.append((nc, nr))
                    visited[nc][nr] = True
                else:
                    visited[nc][nr] = True
    return (gold_cnt, mine_size)

T = int(input())
for t_c in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False]*N for _ in range(N)]
    gold_cnt_list = []
    mine_size_list = []


    for i in range(N):
        for j in range(N):
            if arr[i][j]>0 and not visited[i][j]:
                visited[i][j] = True
                g_c, m_s = mine(i, j)
                gold_cnt_list.append(g_c)
                mine_size_list.append(m_s)

    mine_cnt = len(gold_cnt_list)


    print(f'#{t_c} {max(gold_cnt_list)} {min(mine_size_list)}')


