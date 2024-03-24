TC = int(input())

for tc in range(1, TC + 1):
    word = list(input())
    copy = word[:]
    copy.reverse()
    ans = 0
    if copy == word:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')