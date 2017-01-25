"""Write a method to replace all spaces in a string with '%20'.  You may assume
that the string has sufficient space at the end to hold the additional
characters, and that you are given the "true" length of the string.  (Note:
If implementing in Java, please use a character array so that you can perform
this operation in place.)  **I will not be using the length input, as it seems
unnecessary in Python
"""
def urlify(chars):
    """Function to replace each space with '%20'
        >>> urlify("Mr John Smith")
        'Mr%20John%20Smith'
        >>> urlify("")
        ''
        >>> urlify(" ")
        '%20'
    """
    urlified = ""
    # This is unnecessary
    # if not chars:
    #     return urlified

    for char in chars:
        if char == " ":
            char = "%20"
        urlified += char

    return urlified


def urlify_alt1(chars):
    """Function to replace each space with '%20'.  Uses join with list,
    instead of concatenating string on each iteration to save memory space.
        >>> urlify_alt1("Mr John Smith")
        'Mr%20John%20Smith'
        >>> urlify_alt1("")
        ''
        >>> urlify_alt1(" ")
        '%20'
    """
    urlified = []
    for char in chars:
        if char == " ":
            char = "%20"
        urlified.append(char)

    return "".join(urlified)


def urlify_alt2(chars):
    """Function to replace each space with '%20'.
        >>> urlify_alt2("Mr John Smith")
        'Mr%20John%20Smith'
        >>> urlify_alt2("")
        ''
        >>> urlify_alt2(" ")
        '%20'
    """
    urlified = list(chars)
    if urlified:
        for i in range(len(urlified)):
            if urlified[i] == " ":
                urlified[i] = "%20"
    # If chars is None, this will still return the correct answer
    return "".join(urlified)


############################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    print
    if not result.failed:
        print "YAY, ALL TESTS PASSED!!"
    print