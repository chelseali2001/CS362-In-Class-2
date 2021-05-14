def palin(s):
    if (type(s) is not str):
        return "Strings only"

    s = s.lower()

    if s == s[::-1]:
        return True
    
    return False