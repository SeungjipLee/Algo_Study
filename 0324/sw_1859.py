TC = int(input())
for tc in range(1, TC + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    final = 0
    maximum = arr[-1]
    for i in range(N-1, -1, -1):
        if arr[i] > maximum:
            maximum = arr[i]
        else:
            final += maximum - arr[i]
    print(f'#{tc}', final)