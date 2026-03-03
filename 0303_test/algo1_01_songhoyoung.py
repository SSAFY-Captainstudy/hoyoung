# 확인할 방향을 인덱스로 설정
dc = [-1, 1, 0, 0]
dr = [0, 0, -1, 1]

# 술래가 잡을 수 있는 범위 처리
def arange_catch(y, x, d):
    # 그 방향으로 나아가는 횟수 처리
    cnt = 0
    while True:
        # 반복문이 돌 때마다 그 방향으로 한칸더
        cnt += 1
        nc = y + (dc[d] * cnt)
        nr = x + (dr[d] * cnt)
        # 만약, 그곳이 범위 안이거나 방문하지 않았을 경우에
        if 0 <= nc < N and 0 <= nr < N and not visited[nc][nr]:
            # 만약, 그곳이 통로라면 술래가 잡을 수 있다는 표시인 정수 2로 변경.
            if arr[nc][nr] == 0:
                arr[nc][nr] = 2
                visited[nc][nr] = True
            # 만약, 그곳이 벽이라면 다른 방향 탐색하러 리턴
            elif arr[nc][nr] == 1:
                visited[nc][nr] = True
                return
        # 만약, 인덱스 밖으로 나가서 탐색하거나 다 방문한 경우에 리턴
        else:
            return

T = int(input())
for t_c in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    Q = []
    visited = [[False]*N for _ in range(N)]

    # 술래가 있는 위치값을 Q에 담고 방문처리
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                Q.append((i, j))
                visited[i][j] = True

    # 각 술래가 잡을 수 있는 거리 체크
    while Q:
        y, x = Q.pop(0)

        # 델타값 4방향에서 벽이나 격자 끝을 만나기 전까지 함수 처리
        for d in range(4):
            arange_catch(y, x, d)

    # 안전한 위치 카운트
    safe_zone = 0

    # 값이 2로 바뀌지 않거나 통로일 경우에 안전한 위치 값 +1
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                safe_zone += 1

    print(f'#{t_c} {safe_zone}')







