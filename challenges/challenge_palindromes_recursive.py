def is_palindrome_recursive(word, low_index, high_index):
    """
    # test manual
    >>> is_palindrome_recursive('ANA', 0, 2)
    True
    >>> is_palindrome_recursive('AGUA', 0, 3)
    False

    :param word:
    :param low_index:
    :param high_index:
    :return:
    """
    if not word:
        return False
    elif word[low_index] != word[high_index]:
        return False
    elif low_index >= high_index:
        return True

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
