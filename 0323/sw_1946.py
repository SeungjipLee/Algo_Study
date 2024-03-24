TC = int(input())

for tc in range(1, TC + 1):
    N = int(input())
    info = {}
    final = ''
    print(f'#{tc}')
    for _ in range(N):
        chr, num = input().split()
        info[chr] = int(num)
        final += chr*info[chr]
    for i in range(0, len(final), 10):
        print(final[i:i + 10])