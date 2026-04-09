import sys
sys.stdin = open("input.txt", "r")

d = ['^', '>', 'v', '<']

def play(lev, r, c, status):
    if lev == C:
        return 1 if field[r][c] == 'Y' else 0

    if command[lev] == 'R':
        return play(lev + 1, r, c, (status + 1) % 4)
    elif command[lev] == 'L':
        return play(lev + 1, r, c, (status + 3) % 4)
    elif command[lev] == 'A':
        if status == 0:
            if 0 <= r - 1 < N:
                if field[r-1][c] == 'T':
                    return play(lev + 1, r, c, status)
                elif field[r-1][c] in ['G', 'X', 'Y']:
                    return play(lev + 1, r - 1, c, status)
            else:
                return play(lev + 1, r, c, status)
        elif status == 2:
            if 0 <= r + 1 < N:
                if field[r+1][c] == 'T':
                    return play(lev + 1, r, c, status)
                elif field[r+1][c] in ['G', 'X', 'Y']:
                    return play(lev + 1, r + 1, c, status)
            else:
                return play(lev + 1, r, c, status)
        elif status == 1:
            if 0 <= c + 1 < N:
                if field[r][c + 1] == 'T':
                    return play(lev + 1,  r, c, status)
                elif field[r][c+1] in ['G', 'X', 'Y']:
                    return play(lev + 1, r, c + 1, status)
            else:
                return play(lev + 1, r, c, status)
        elif status == 3:
            if 0 <= c - 1 < N:
                if field[r][c-1] == 'T':
                    return play(lev + 1, r, c, status)
                elif field[r][c-1] in ['G', 'X', 'Y']:
                    return play(lev + 1, r, c - 1, status)
            else:
                return play(lev + 1, r, c, status)

T = int(input())
for t_c in range(1, T + 1):
    N = int(input())
    field = [list(input().strip()) for _ in range(N)]
    Q = int(input())

    start_r = 0
    start_c = 0

    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start_r = i
                start_c = j
    print(f'#{t_c}', end=' ')
    for _ in range(Q):
        C, command = input().split()
        C = int(C)
        ans = play(0, start_r, start_c, 0)
        print(ans, end=' ')

