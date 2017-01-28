"""1.9 String Rotation:  Assume you have a method 'isSubstring' which checks
if one word is a substring of another.  Given two strings, 's1' and 's2', write
code to check if 's2' is a rotation of 's1' using only one call to
'isSubstring' (e.g. 'waterbottle' is a rotation of 'erbottlewat')
"""

def str_rotation(str1, str2):
    """Function that checks if one string is a rotation of another.
        >>> str_rotation('water', 'watersy')
        False
        >>> str_rotation('waterbottle', 'erbottlewat')
        True
        >>> str_rotation('yes', 'yse')
        False
    """
    # Check if lengths are the same.  If they're not, return False.
    if len(str1) != len(str2):
        return False

    for i in range(len(str1)):
        if str2 == str1[i:] + str1[:i]:
            return True

    return False


########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "Congrats!  You complete String Rotation!"
    print
