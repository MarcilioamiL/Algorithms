def is_palindrome_iterative(word):
    """
    >>> is_palindrome_iterative('ana')
    True
    >>> is_palindrome_iterative('roma')
    False

    :param num:
    :return:
    """
    inverted_word = word[::-1]
    if not word or word == '':
        return False
    if word == inverted_word:
        return True
    if word != inverted_word:
        return False
