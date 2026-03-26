import sys
sys.stdin = open("input.txt", "r")

def play(order):
    out = 0
    inning = 0
    score = 0
    base_1, base_2, base_3 = 0, 0, 0
    idx = 0

    while inning < N:
        if idx == 9:
            idx = 0

        hit = player[inning][order[idx]]

        if hit == 4:
            score += 1 + base_3 + base_2 + base_1
            base_1, base_2, base_3 = 0, 0, 0

        elif hit == 3:
            score += base_3 + base_2 + base_1
            base_1, base_2, base_3 = 0, 0, 1

        elif hit == 2:
            score += (base_2 + base_3)
            base_1, base_2, base_3 = 0, 1, base_1

        elif hit == 1:
            score += base_3
            base_1, base_2, base_3 = 1, base_1, base_2

        elif hit == 0:
            out += 1

        if out == 3:
            inning += 1
            out = 0
            base_1, base_2, base_3 = 0, 0, 0

        idx += 1

    return score

def permu(l, p_s):
    global max_score
    if l == 9:
        max_score = max(max_score, play(p_s))
        return

    if l == 3:
        permu(l+1, p_s + [0])
    else:
        for i in range(1, 9):
            if not visited[i]:
                visited[i] = 1
                permu(l+1, p_s + [i])
                visited[i] = 0

N = int(input())
player = [list(map(int, input().split())) for _ in range(N)]
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
visited = [0]*9
visited[0] = 1

max_score = 0

permu(0, [])

print(max_score)
