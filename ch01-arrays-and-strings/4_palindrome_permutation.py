"""1.4 Palindrome Permutation:  Given a string, write a function to check if
it is a permutation of a palindrome.  A palindrome is a word or phrase that is
the same forwards and backwards.  A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
"""

def is_palindrome_perm(chars):
    """Function to determine if the input characters are a permutation
    of a palindrome.
        >>> is_palindrome_perm("Tact Coa")
        True
        >>> is_palindrome_perm("")
        True
        >>> is_palindrome_perm("hello")
        False
        >>> is_palindrome_perm("alla")
        True
    """
    if not chars:
        return True

    # Create a dictionary to count the characters
    chars_count = {}
    # Remove spaces and make all characters lowercase
    for char in chars.replace(" ", "").lower():
        chars_count[char] = chars_count.get(char, 0) + 1

    # Create a list of the count values and a counter for the odd counts.
    counts = chars_count.values()
    odd_count = 0

    for count in counts:
        if count % 2 != 0:
            odd_count += 1

    # If all counts are even, or if all but one count is even, the input string
    # is a permutation of a palindrome.
    if odd_count <= 1:
        return True

    return False


########################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()

    print
    if not result.failed:
        print "WOOHOOOOOOO!  GREAT JOB, ALL TESTS PASSED!"
    print
