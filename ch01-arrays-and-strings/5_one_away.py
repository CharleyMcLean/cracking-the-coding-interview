"""1.5 One Away:  There are three types of edits that can be performed on
strings:  insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit (or zero
edits) away.

Example:
pale, ple -> True
pales, pale -> True
pale, bale -> True
pale, bake -> False
"""

def is_one_away(chars1, chars2):
    """Function to determine if two strings are at most one edit away from
    each other
        >>> is_one_away("pale", "ple")
        True
        >>> is_one_away("pales", "pale")
        True
        >>> is_one_away("pale", "bale")
        True
        >>> is_one_away("pale", "bake")
        False
        >>> is_one_away("", "")
        True
        >>> is_one_away("", "a")
        True
        >>> is_one_away("", "ab")
        False
        >>> is_one_away("a", "ab")
        True
        >>> is_one_away("pp", "ppp")
        True
        >>> is_one_away("pp", "pppp")
        False
    """
    # First let's check if they're both empty strings
    if not chars1 and not chars2:
        return True

    # If one is an empty string, and the other is len 1: True
    if (not chars1 and len(chars2) == 1) or (not chars2 and len(chars1) == 1):
        return True

    # If the lengths are more than one off, it's False
    if abs(len(chars1) - len(chars2)) > 1:
        return False

    # Make both strings all lowercase for comparison
    chars1 = chars1.lower()
    chars2 = chars2.lower()

    # Check if they are exactly the same
    if chars1 == chars2:
        return True

    # If the lengths are one off, one is inside the other, it's True
    if abs(len(chars1) - len(chars2)) == 1:
        if (chars1 in chars2) or (chars2 in chars1):
            return True
        if len(chars1) < len(chars2):
            for i in range(len(chars1)):
                if chars1[i] != chars2[i]:
                    chars2 = chars2[:i] + chars2[(i + 1):]
        else:
            for i in range(len(chars2)):
                if chars2[i] != chars1[i]:
                    chars1 = chars1[:i] + chars1[(i + 1):]
        return chars1 == chars2

    # If the lengths are one off, and one is not inside the other, it's False
    if abs(len(chars1) - len(chars2)) == 1 and not ((chars1 in chars2) or (chars2 in chars1)):
        return False

    # Write check for if the lengths are the same
    diffs = 0
    if len(chars1) == len(chars2):
        for i in range(len(chars1)):
            if chars1[i] != chars2[i]:
                diffs += 1

    if diffs <= 1:
        return True

    return False


#########################################################################
if __name__ == "__main__":

    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "Yay, all tests passed!"
    print
