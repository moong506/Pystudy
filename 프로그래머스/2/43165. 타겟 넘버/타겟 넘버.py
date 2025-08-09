from collections import deque
def bfs(arr, num):
    q = deque([(arr[0], 0), (-arr[0], 0)])
    max_length = len(arr)
    count = 0
    while q:
        p_num, idx = q.popleft()
        if idx == max_length - 1:
            if p_num == num:
                count += 1
            continue
        for c in [1, -1]:
            p_num += c*arr[idx+1]
            q.append((p_num, idx+1))
            p_num -= c*arr[idx+1]
    return count


def solution(numbers, target):
    
    answer = bfs(numbers, target)
    
    return answer