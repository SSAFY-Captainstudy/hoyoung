import sys
sys.stdin = open("battle.txt", "r")

tank = ['^', 'v', '<', '>']

def play(lev, r, c, status):
    if lev == N:
        return

    if user_input[lev] == 'S':
        if status == '^':
            aim = r
            while aim > 0:
                aim -= 1
                if arr[aim][c] in ['.', '-']:
                    continue
                elif arr[aim][c] == '#':
                    break
                elif arr[aim][c] == '*':
                    arr[aim][c] = '.'
                    break

        elif status == 'v':
            aim = r
            while aim < H - 1:
                aim += 1
                if arr[aim][c] in ['.', '-']:
                    continue
                elif arr[aim][c] == '#':
                    break
                elif arr[aim][c] == '*':
                    arr[aim][c] = '.'
                    break

        elif status == '<':
            aim = c
            while aim > 0:
                aim -= 1
                if arr[r][aim] in ['.', '-']:
                    continue
                elif arr[r][aim] == '#':
                    break
                elif arr[r][aim] == '*':
                    arr[r][aim] = '.'
                    break

        elif status == '>':
            aim = c
            while aim < W - 1:
                aim += 1
                if arr[r][aim] in ['.', '-']:
                    continue
                elif arr[r][aim] == '#':
                    break
                elif arr[r][aim] == '*':
                    arr[r][aim] = '.'
                    break
        play(lev + 1, r, c, status)

    elif user_input[lev] == 'U':
        next_status = '^'
        arr[r][c] = '^'
        if 0 <= r - 1 < H and arr[r-1][c] == '.':
            arr[r-1][c] = next_status
            arr[r][c] = '.'
            play(lev + 1, r - 1, c, next_status)
        else:
            play(lev + 1, r, c, next_status)

    elif user_input[lev] == 'D':
        next_status = 'v'
        arr[r][c] = 'v'
        if 0 <= r + 1 < H and arr[r + 1][c] == '.':
            arr[r + 1][c] = next_status
            arr[r][c] = '.'
            play(lev + 1, r + 1, c, next_status)
        else:
            play(lev + 1, r, c, next_status)

    elif user_input[lev] == 'L':
        next_status = '<'
        arr[r][c] = '<'
        if 0 <= c - 1 < W and arr[r][c - 1] == '.':
            arr[r][c - 1] = next_status
            arr[r][c] = '.'
            play(lev + 1, r, c - 1, next_status)
        else:
            play(lev + 1, r, c, next_status)

    elif user_input[lev] == 'R':
        next_status = '>'
        arr[r][c] = '>'
        if 0 <= c + 1 < W and arr[r][c + 1] == '.':
            arr[r][c + 1] = next_status
            arr[r][c] = '.'
            play(lev + 1, r, c + 1, next_status)
        else:
            play(lev + 1, r, c, next_status)

T = int(input())
for t_c in range(1, T+1):
    H, W = map(int, input().split())
    arr = [list(input().strip()) for _ in range(H)]
    N = int(input())
    user_input = list(input().strip())

    status = tank[0]
    start_r = 0
    start_c = 0

    for i in range(H):
        for j in range(W):
            if arr[i][j] in tank:
                status = arr[i][j]
                start_r = i
                start_c = j

    play(0, start_r, start_c, status)
    print(f'#{t_c}', end=' ')
    for k in range(H):
        print(''.join(arr[k]))

