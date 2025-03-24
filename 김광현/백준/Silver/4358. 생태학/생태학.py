# 정해지지 않은 개수의 input을 받는 문제가 재미있어 보여서 도전!!
# 고민하다가 찾아보니 내장 함수로 해결 가능;;
import sys
input = sys.stdin.readline

trees = {}  # 나무 이름과 개수를 저장할 딕셔너리
n = 0  # 전체 나무 개수를 세는 변수

while True:
    tree = input().rstrip()  # 한 줄씩 입력받고 개행문자 제거
    if not tree:  # 입력이 끝나면 (EOF) 루프 종료
        break
    if tree in trees:
        trees[tree] += 1  # 이미 있는 나무라면 개수 증가
    else:
        trees[tree] = 1  # 처음 등장한 나무라면 1로 초기화
    n += 1  # 전체 나무 개수 카운트 증가
    
tree_lst = list(trees.keys())  # 딕셔너리의 키(나무 이름)들을 리스트로 변환
tree_lst.sort()  # 사전순 정렬

for tree in tree_lst:
    print('%s %.4f' %(tree, trees[tree]/n*100))