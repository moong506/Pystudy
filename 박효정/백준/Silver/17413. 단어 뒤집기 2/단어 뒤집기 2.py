S = input()
ans = ''
arr = []
i = 0
while True:
    if i == len(S):
        break
    if S[i] == '<':
        li = []
        while i < len(S):
            if S[i] == '>':
                li.append('>')
                i += 1
                break
            li.append(S[i])
            i += 1
        arr.append(li)

    else:
        li = []
        while i < len(S):
            if S[i] == ' ':
                li.append(' ')
                i += 1
                break
            if S[i] == '<':
                break
            li.append(S[i])
            i += 1
        arr.append(li)

for word in arr:
    if word[0] == '<':
        for i in range(len(word)):
            ans += word[i]
    elif word[-1] == ' ':
        for i in range(len(word)-2, -1, -1):
            ans += word[i]
        ans += ' '
    else:
        for i in range(len(word)-1, -1, -1):
            ans += word[i]


print(ans)