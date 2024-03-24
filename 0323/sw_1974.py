def is_row_possible(i):
    store = set()
    for j in range(9):
        store.add(Board[i][j])
    if store == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return True
    else:
        return False

def is_col_possible(i):
    store = set()
    for j in range(9):
        store.add(Board[j][i])
    if store == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return True
    else:
        return False

def is_box_possible(i, j):
    store = set()
    for k in range(3):
        for l in range(3):
            store.add(Board[i+k][j+l])
    if store == {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return True
    else:
        return False

TC = int(input())
for tc in range(1, TC+1):
    Board = [list(map(int, input().split())) for _ in range(9)]
    is_possible = 1
    for i in range(9):
        if is_row_possible(i) == False:
            is_possible = 0
            break
        if is_col_possible(i) == False:
            is_possible = 0
            break
        for j in [0, 3, 6]:
            if i in [0, 3, 6] and is_box_possible(i, j) == False:
                is_possible = 0
                break
    print(f'#{tc}', is_possible)