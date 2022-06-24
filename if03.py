def main(a):
    """
    If the number is positive, increase it to 1, else decrease it to 2. If it is 0, assign 10.
    Args:
        a: integer
    Returns:
        a: integer
    """
    s = a
    if a>0:
        s += 1
    elif a<0:
        s -= 2
    else: 
        s += 10
    return s

print(main(11))

