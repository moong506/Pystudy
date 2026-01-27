#import sys
#input = sys.stdin.readline
T = int(input())
count = 0
for _ in range(T):
    word = input()
    idx_word = word[0]
    word_lst = [word[0]]

    for w in word:
        if w == idx_word:
            pass
        else:
            idx_word = w
            if w in word_lst:
                break
            word_lst.append(w)
    else:
        count += 1
print(count)

