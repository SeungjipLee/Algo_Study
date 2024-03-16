TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    arr = [0]*5001
    final = []
    for _ in range(N):
        a, b = map(int, input().split())
        for num in range(a, b+1):
            arr[num] += 1
    P = int(input())
    for _ in range(P):
        c = int(input())
        final.append(arr[c])

    print(f'#{tc}', *final)