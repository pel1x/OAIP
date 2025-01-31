def max(num):
    if len(num) == 1:
        return num[0]
    
    ostavsheysya_chast = max(num[1:])
    return num[0] if num[0] > ostavsheysya_chast else ostavsheysya_chast
