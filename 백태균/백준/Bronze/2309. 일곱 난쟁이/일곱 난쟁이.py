fake_dwarf = []
total_sum = 0

for i in range(9):
    fake_dwarf.append(int(input()))
    total_sum += fake_dwarf[i]

fake_dwarf.sort()
found = False

for i in range(9):
    if found:
        break

    for j in range(i+1, len(fake_dwarf)):
        if total_sum - fake_dwarf[i] - fake_dwarf[j] == 100:
            # 거짓 난쟁이 키 값을 제외하고 출력
            for k in range(len(fake_dwarf)):
                if k == i or k == j:
                    continue
                else:
                    print(fake_dwarf[k])

            found = True
            break
