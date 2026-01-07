def get_k(a, b):
    
    d = b - a
    k = d - (a % d)
    if k == 0:
        k = d
    return k
    