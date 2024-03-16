TC = int(input())

for tc in range(1, TC+1):
    D, A, B, F = map(int, input().split())
    print(f'#{tc}', D/(A+B) * F)