def solution(my_string, is_suffix):
    return 1 if my_string[-1*len(is_suffix):]==is_suffix else 0