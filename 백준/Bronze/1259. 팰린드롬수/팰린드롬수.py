while True:
    N = input()

    if N == '0':
        break

    M = len(N)

    for i in range(M//2):
        if N[i] != N[M - i - 1]:
            print("no")
            break
        else:
            continue
    else:
        print("yes")
