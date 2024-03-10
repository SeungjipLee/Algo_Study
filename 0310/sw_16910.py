TC = int(input())

for test in range(1, TC + 1):
    n = int(input())
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            cal = (i ** 2 + j ** 2) ** (1 / 2)
            if cal <= n:
                cnt += 1
            else:
                break

    print(f'#{test}', cnt * 4 + n * 4 + 1)
