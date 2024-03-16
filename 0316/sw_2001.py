TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            mid = 0
            for k in range(M):
                for l in range(M):
                    mid += board[i+k][j+l]
            if mid >= max:
                max = mid
    print(f'#{tc}', max)