'''
학생을 앞으로 보내면서 어떻게 인덱스를 관리할 것인지를 생각하기
학생이 앞으로 이동하면 그 위에 인덱스는 1씩 뒤로 이동하기 때문에 인덱스 +1 해주기
단! 뒤에서부터 바꿔줘야 인덱스에 오류가 안생김
그리고 마지막에 해당 학생이 옮겨질 위치에 추가하기
'''
N = int(input())
arr = list(map(int, input().split()))
students = [0] * N
for i in range(N):
    j = i - arr[i]
    if i > j:
        for k in range(i-1, j-1, -1):
            students[k+1] = students[k]
    students[j] = i+1
print(*students)