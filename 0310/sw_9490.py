test_case = int(input())

delta_x = [0, 1, 0, -1]
delta_y = [1, 0, -1, 0]

for test_number in range(1, test_case + 1):
    height, width = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(height)]
    max_value = 0
    for height_idx in range(height):
        for width_idx in range(width):
            bomb_length = board[height_idx][width_idx]
            mid_sum = bomb_length
            for rang in range(1, bomb_length + 1):
                for delta in range(4):
                    new_x = height_idx + rang * delta_x[delta]
                    new_y = width_idx + rang * delta_y[delta]
                    if new_x < 0 or new_y < 0 or new_x >= height or new_y >= width:
                        continue
                    else:
                        mid_sum += board[new_x][new_y]
            if mid_sum > max_value:
                max_value = mid_sum
    print(f'#{test_number}', max_value)
