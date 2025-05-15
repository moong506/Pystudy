def solution(sizes):
    max_width, max_height = 0, 0 
    for w, h in sizes:
        if w < h:
            w, h = h, w
        if max_width < w:
            max_width = w
        if max_height < h:
            max_height = h
    answer = max_width * max_height
    return answer