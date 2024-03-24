# for tc in range (1, 11):
N, password = map(int, input().split())
stack = []
for chr in str(password):
    if stack and stack[-1] == chr:
        stack.pop()
    else:
        stack.append(chr)
print(f'#{1}', int(''.join(stack)))