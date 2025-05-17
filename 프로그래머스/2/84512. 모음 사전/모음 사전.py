def solution(word):
    answer = 0
    length = len(word)
    if length < 5:
        for _ in range(5-length):
            word = word + '0'
    word_dict = {'A': 0, 'E': 1, 'I': 2, 'O':3, 'U':4}
    for i in range(5):
        if word[i] == '0':
            break
        count = 0
        target_word = word_dict[word[i]]
        for j in range(5-i-1, 0, -1):
            count += 5**(j) * target_word
        count += (target_word + 1)
        answer += count
    
        
    return answer