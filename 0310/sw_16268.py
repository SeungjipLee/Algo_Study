TC = int(input())

# 델타 탐색(우 하 좌 상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for test in range(1, TC + 1):
    N, M = map(int, input().split())
    Board = [list(map(int, input().split())) for _ in range(N)]
    # 최댓값을 미리 설정
    max_value = 0
    for i in range(N):
        for j in range(M):
            # 중간값에서 출발
            mid_sum = Board[i][j]
            for idx in range(4):
                new_x = i + dx[idx]
                new_y = j + dy[idx]
                if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                    continue
                else:
                    mid_sum += Board[new_x][new_y]
            # 나온 것들 중 최대인지 확인
            if mid_sum > max_value:
                max_value = mid_sum
    print(f'#{test}', max_value)
