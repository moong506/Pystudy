import sys

M = int(sys.stdin.readline())
S = set() # 중복 제거를 위해 set 사용

for _ in range(M):
    command = sys.stdin.readline().split()
    
    if len(command) == 2: # 명령어와 숫자가 입력된다면
        num = int(command[1])
    
    if command[0] == 'add':
        S.add(num)
    elif command[0] == 'remove':
        S.discard(num)
    elif command[0] == 'check':
        print(1 if num in S else 0)
    elif command[0] == 'toggle':
        if num in S:
            S.discard(num)
        else:
            S.add(num)
    elif command[0] == 'all':
        S = set(range(1, 21))
    elif command[0] == 'empty':
        S = set()
