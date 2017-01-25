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


############################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    print
    if not result.failed:
        print "YAY, ALL TESTS PASSED!!"
    print