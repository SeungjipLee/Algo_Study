TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        mid = 0
        for j in range(N):
            if Board[i][j] == 1:
                mid += 1
            if j == N - 1 or Board[i][j] == 0:
                if mid == M:
                    cnt += 1
                mid = 0

        mid = 0
        for j in range(N):
            if Board[j][i] == 1:
                mid += 1
            if j == N-1 or Board[j][i] == 0:
                if mid == M:
                    cnt += 1
                mid = 0

    print(f'#{tc}', cnt)

