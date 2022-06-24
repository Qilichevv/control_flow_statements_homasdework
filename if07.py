def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    s=""
    if a>0:
        if a%2==0:
            s+="positive even number"
        else :
            s+="positive odd number"
    elif a<0:
        if a%2==0:
            s+="negative even number"
        else:
            s+="negative odd number"
    else:
        s+= "the number is zero"

    return s
print(main(-7))