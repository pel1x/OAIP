def prostoe(n, delitel=None):
    if n <= 1:
        return False
    if delitel is None:
        delitel = n - 1
    if delitel == 1:
        return True
    if n % delitel == 0:
        return False
    
    return prostoe(n, delitel - 1)
