"""1.2 Check Permutation:  Given two strings, write a method to decide if one
is a permutation of the other."""

def check_perm(chars1, chars2):
    """Function to determine if two strings are permutations of each other.
        >>> check_perm("tar", "rat")
        True
        >>> check_perm("Tar", "rat")
        True
        >>> check_perm("tar", "")
        False
        >>> check_perm("", "rat")
        False
        >>> check_perm("", "")
        True
        >>> check_perm("I", "am")
        False
    """
    # If both inputs are empty strings
    if not chars1 and not chars2:
        return True

    # If only one of the inputs is an empty string
    # if not chars1 or not chars2:
    #     return False

    # Instead of the above, let's check the lengths of the two string.
    # This will cause us to fail fast for more inputs
    # Remove spaces and make all characters lowercase
    chars1 = list(chars1.replace(" ", "").lower())
    chars2 = list(chars2.replace(" ", "").lower())
    if len(chars1) != len(chars2):
        return False

    return chars1.sort() == chars2.sort()



#####################################################################
if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED, YAY!"
    print