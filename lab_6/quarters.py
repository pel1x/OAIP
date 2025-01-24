def quarters(*data):
    count = {
        '1st': 0,
        '2nd': 0,
        '3rd': 0,
        '4th': 0
    }

    for k, v in data:
        if k > 0 and v > 0:
            count['1st'] += 1
        elif k < 0 and v > 0:
            count['2nd'] += 1
        elif k < 0 and v < 0:
            count['3rd'] += 1
        elif k > 0 and v < 0:
            count['4th'] += 1


    return count
