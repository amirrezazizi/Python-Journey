# countc() function


def countc(s, c):
    """
    c =  [str]
    this function count and return how many character you have in a string.

    """
    found = 0
    for i in range(len(s)):
        if s[i] == c:
            found += 1
    return found
