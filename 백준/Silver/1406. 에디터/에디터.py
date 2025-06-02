from sys import stdin
left = list(stdin.readline().strip())
N = int(input())
right = []

for _ in range(N):
    alphabet = stdin.readline().split()
    if alphabet[0] == 'L' and left:
        right.append(left.pop())
    elif alphabet[0] == 'D' and right:
        left.append(right.pop())
    elif alphabet[0] == 'B' and left:
        left.pop()
    elif alphabet[0] == 'P':
        left.append(alphabet[1])
answer = left + right[::-1]

print(''.join(answer))
