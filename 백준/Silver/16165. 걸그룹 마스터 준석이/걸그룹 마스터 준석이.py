N, M = map(int,input().split())
group = {}
member = {}
for _ in range(N):
    group_name = input()
    number = int(input())
    member_list = []
    for _ in range(number):
        member_name = input()
        # 멤버 이름으로 그룹 맞추기
        member[member_name] = group_name
        member_list.append(member_name)
    member_list.sort()
    group[group_name] = member_list

for _ in range(M):
    quest = input()
    quest_num = int(input())
    if quest_num == 0:
        for person in group[quest]:
            print(person)
    else:
        print(member[quest])