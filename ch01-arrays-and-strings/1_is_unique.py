"""Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?"""

def is_unique(chars):
    """Function to detmerine if a string has all unique characters.
    Does not use additional data structures.
        >>> is_unique('Leila')
        False
        >>> is_unique('Alex')
        True
        >>> is_unique('')
        True
        >>> is_unique('I am a')
        False
    """
    if not chars:
        return True

    for i in range(len(chars) - 1):
        chars = chars.lower()
        if chars[i] in chars[(i + 1):]:
            return False

    return True


def is_unique_alt(chars):
    """Function to determine if a string has all unique characters,
    using additional data structures.
        >>> is_unique_alt('Leila')
        False
        >>> is_unique_alt('Alex')
        True
        >>> is_unique_alt('')
        True
        >>> is_unique_alt('I am a')
        False
    """
    if not chars:
        return True

    return len(set(chars.lower())) == len(chars)


####################################################################


if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED.  GOOD WORK!"
    print
