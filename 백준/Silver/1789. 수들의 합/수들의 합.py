S = int(input())
i = 1

while i < S and i < S-i:
    S -= i
    i += 1

print(i)