TC = int(input())

for tc in range(1, TC + 1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    maximum = 0
    for i in range(N):
        mid = 0
        for j in range(M):
            if Board[i][j] == 1:
                mid += 1
            else:
                if mid > maximum:
                    maximum = mid
                mid = 0
            if j == M-1 and mid > maximum:
                maximum = mid

    for i in range(M):
        mid = 0
        for j in range(N):
            if Board[j][i] == 1:
                mid += 1
            else:
                if mid > maximum:
                    maximum = mid
                mid = 0
            if j == N - 1 and mid > maximum:
                maximum = mid
    print(f'#{tc}', maximum)