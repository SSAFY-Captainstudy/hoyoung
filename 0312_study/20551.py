import sys
sys.stdin = open("input.txt", "r")

def eat(cur, cnt):
    global min_eat

    if cur == 0:
        min_eat = min(min_eat, cnt)
        return

    if box[cur-1] >= box[cur]:
        before = box[cur-1]
        box[cur-1] = box[cur] - 1
        if box[cur-1] <= 0:
            min_eat = -1
            return
        eat_candy = before - box[cur-1]
        eat(cur-1, cnt+eat_candy)
        box[cur-1] = before
    else:
        eat(cur-1, cnt)

T = int(input())
for tc in range(1, T+1):
    box = list(map(int, input().split()))

    min_eat = float("inf")

    eat(2, 0)

    print(f'#{tc} {min_eat}')