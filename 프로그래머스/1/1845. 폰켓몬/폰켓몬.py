def solution(nums):
    N= len(nums)
    answer = 0
    po_dict = {}
    for num in nums:
        if num in po_dict.keys():
            po_dict[num] += 1
        else:
            po_dict[num] = 1
    count = len(po_dict.keys())
    if count >= N//2:
        answer = N//2
    else:
        answer = count
    return answer