N = int(input())
people = list(map(int, input().split()))
people.sort()
result = 0
for i in range(N):
    result += sum(people[i] for i in range(i+1))
print(result)