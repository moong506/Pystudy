def f(i,cnt,s,selected):
    global ans
    if s > 100:
        return
    if i == 10:
        if cnt == 7 and s == 100:
            ans = selected[:]
            return
    else:   # 포함할지 안할지 결정
        f(i+1,cnt,s,selected)

        selected.append(candidates[i])
        f(i+1,cnt+1,s + candidates[i],selected)
        selected.pop()


candidates = []
for _ in range(9):
    candidate = int(input())
    candidates.append(candidate)
candidates = [0] + candidates
# print(candidates)
ans = []
f(1,0,0, [])
ans.sort()
for i in range(7):
    print(ans[i])