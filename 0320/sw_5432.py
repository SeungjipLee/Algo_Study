TC = int(input())

for tc in range(1, TC+1):
    stick = input()
    now = 0
    final = 0
    for i in range(len(stick)):
        if stick[i] == '(' and stick[i + 1] != ')':
            now += 1
        elif stick[i] == '(' and stick[i + 1] == ')':
            final += now
        elif stick[i] == ')' and stick[i - 1] != '(':
            now -= 1
            final += 1
    print(f'#{tc}', final)