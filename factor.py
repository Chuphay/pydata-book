def method(integer):
    s = str(integer)
    A = int(s[:len(s)/2])
    B = int(s[len(s)/2:])
    return A*B
