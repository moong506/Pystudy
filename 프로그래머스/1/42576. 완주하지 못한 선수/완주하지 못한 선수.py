def solution(participant, completion):
    name_dict = dict()
    for name in completion:
        if name in name_dict:
            name_dict[name] +=1
        else:
            name_dict[name] = 1
    
    for all_name in participant:
        if all_name not in name_dict.keys():
            return all_name
        if name_dict[all_name] == 0:
            return all_name
        name_dict[all_name] -= 1
        
    
        
    