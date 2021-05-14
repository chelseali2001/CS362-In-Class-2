def count(s):
    if (type(s) is not str):
        return "Strings only"

    arr = s.split(" ")
    total = 0

    for x in range(len(arr)):
        if arr[x] != "":
            total += 1

    return total