def binary_sum(a, b):
    add_zero = abs(len(a) - len(b))
    if len(a) > len(b):
        for _ in range(add_zero):
            b = "0" + b
    elif len(a) < len(b):
        for _ in range(add_zero):
            a = "0" + a

    result = ["0"] * (len(a)+1)
    for i in range(len(a)-1, -1, -1):
        part_sum = int(a[i]) + int(b[i]) + int(result[i+1])
        if part_sum == 2:
            result[i] = "1"
            result[i+1] = "0"
        elif part_sum == 3:
            result[i] = "1"
            result[i+1] = "1"
        else:
            result[i+1] = str(part_sum)

    k = 0
    while len(result) > 1 and result[k] == "0":
        result = result[1:]

    return "".join(result)

t = int(input())
for _ in range(t):
    n1, n2 = input().split()
    print(binary_sum(n1, n2))
