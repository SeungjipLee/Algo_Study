def turn_box(Board, n):
    newBoard = []
    for i in range(n):
        mid = []
        for j in range(n):
            mid.append(Board[n-j-1][i])
        newBoard.append(mid)
    return newBoard

TC = int(input())

for tc in range(1, TC+1):
    N = int(input())
    Board = [list(map(int, input().split())) for _ in range(N)]
    turn90 = turn_box(Board, N)
    turn180 = turn_box(turn90, N)
    turn270 = turn_box(turn180, N)
    final = []
    for i in range(N):
        mid = ''
        for j in range(N):
            mid += str(turn90[i][j])
        mid += ' '
        for j in range(N):
            mid += str(turn180[i][j])
        mid += ' '
        for j in range(N):
            mid += str(turn270[i][j])
        final.append(mid)
    print(f'#{tc}')
    for i in final:
        print(i)