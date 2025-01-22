def groundhog_day(strings):
    if len(strings) < 2:
        return (0, 0)
    
    for i in range(1, len(strings)):
        tekushchaya_string = strings[i]
        predydushchaya_string = strings[i - 1]
        
        differing_indices = [j for j in range(len(tekushchaya_string)) if tekushchaya_string[j] != predydushchaya_string[j]]
        
        if len(differing_indices) > 2:
            return (i, *differing_indices)
    
    return (0, 0)