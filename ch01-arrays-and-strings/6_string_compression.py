"""1.6 String Compression:  Implement a method to perform basic string
compression using the counts of repeated characters.  For example, the string
'aabcccccaaa' would become 'a2b1c5a3'.  If the "compressed" string would not
become smaller than the original string, your method should return the
original string.  You can assume the string has only uppercase and lowercase
letters.
"""


def string_compression(chars):
    """Function to compress a string using the counts of repeated chars.
        >>> string_compression("")
        ''
        >>> string_compression("abc")
        'abc'
        >>> string_compression("aabbcc")
        'aabbcc'
        >>> string_compression("aabccc")
        'aabccc'
        >>> string_compression("aaabcccc")
        'a3b1c4'
        >>> string_compression("aaabcccca")
        'a3b1c4a1'
    """
    # First check for empty string
    if not chars:
        return chars

    # Treat upper- and lowercase letters the same
    chars = chars.lower()

    # Create variables to hold letters and counts, plus a counter
    chars_lst = [chars[0]]
    counts = []
    counter = 1
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1]:
            counter += 1
        else:
            counts.append(str(counter))
            chars_lst.append(chars[i])
            counter = 1

    # append the last character's count
    counts.append(str(counter))

    # Create a list [char1, count1, char2, count2, ...]
    chars_and_counts = [i for j in zip(chars_lst, counts) for i in j]

    # Check if compressed length will be longer than original
    if len(chars) <= len(chars_and_counts):
        return chars

    return "".join(chars_and_counts)

#########################################################################
if __name__ == "__main__":
    import doctest
    result = doctest.testmod()

    print
    if not result.failed:
        print "Yay, good job!  All tests passed!"
    print
