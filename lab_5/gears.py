def gears(data, n, m):
    slovar_1, slovar_2 = {}, {}
    
    for gear_list in data:
        for gear in gear_list:
            if gear % n == 0 and gear >= n:
                rn = gear // n
                if rn not in slovar_1 and rn in slovar_2:
                    return gear, slovar_2[rn]
                slovar_1[rn] = gear
            
            elif gear % m == 0 and gear >= m:
                rm = gear // m
                if rm not in slovar_2 and rm in slovar_1:
                    return slovar_1[rm], gear
                slovar_2[rm] = gear

    return (None, None)
