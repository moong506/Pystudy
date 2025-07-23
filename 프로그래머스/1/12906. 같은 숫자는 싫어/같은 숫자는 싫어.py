def solution(arr):
    answer = [-1]*len(arr)
    answer[0] = arr[0]
    top = 0
    for num in arr:
        if num == answer[top]:
            continue
        top += 1
        answer[top] = num
    
    answer = answer[:top+1]
    return answer