TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    box = [0]*N
    for i in range(M):
        a, b = map(int, input().split())
        for k in range(a-1, b):
            box[k] = i+1
    print(f'#{tc}', *box)