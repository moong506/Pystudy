word = input().upper()      # 대소문자 구분 안하니까 대문자로 통일해서 보자
word_lst = list(set(word))
lst = []

for i in word_lst:
    
    count = word.count(i)
    lst.append(count)

if lst.count(max(lst)) != 1:    # 가장 많이 사용된 알파벳이 여러 개면 '?'출력
    print("?")
else:
    print(word_lst[lst.index(max(lst))])