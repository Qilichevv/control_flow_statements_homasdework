def main(a):
    """
    The two-digit integer is given.
    Replace the digits of the number.
    True if the resulting number is less than or equal to the old number, otherwise return False.
    
    Args:
        a: integer
    Returns:
        boolean: True if the resulting number is less than or equal to the old number, otherwise return False.
    """
    a1=a%10
    a=a//10
    a2=a%10
    s=a1*10+a2
    return a>=s

print(main(24))