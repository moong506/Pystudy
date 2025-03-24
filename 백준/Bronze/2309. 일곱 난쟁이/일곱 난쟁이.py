def find_fake_dwarfs():
    nine_sum = sum(dwarfs)
    diff_sum = nine_sum - 100

    for i in range(9):
        mode = diff_sum - dwarfs[i]
        for j in range(9):
            if j == i:
                continue
            if dwarfs[j] == mode:
                return i, j

dwarfs = [int(input()) for _ in range(9)]
dwarfs.sort()

fake1, fake2 = find_fake_dwarfs()

for i in range(9):
    if i != fake1 and i != fake2:
        print(dwarfs[i])