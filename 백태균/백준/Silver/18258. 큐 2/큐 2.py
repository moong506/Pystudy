import sys
from collections import deque

N = int(sys.stdin.readline())
q = deque()

for i in range(N):
    command = sys.stdin.readline().split()

    # push
    if command[0] == 'push':
        q.append(int(command[1]))

    # pop
    elif command[0] == 'pop':
        if q:
            print(q[0])
            q.popleft()
        else:
            print(-1)

    # size
    elif command[0] == 'size':
        print(len(q))

    # empty
    elif command[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)

    # front
    elif command[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)

    # back
    elif command[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)
