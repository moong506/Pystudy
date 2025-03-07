n = input()
freq = {i: 0 for i in range(10)}
for i in range(len(n)):
    freq[int(n[i])] += 1
num = list(freq.values())
spin = (num[6] + num[9]) // 2
if (num[6] + num[9]) % 2 == 1:
    spin += 1
num[6], num[9] = spin, 0
print(max(num))
