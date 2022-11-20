def anagrama(string):
    word = ''
    while len(string) > 0:
        word += min(string)
        string = string.replace(min(string), '', 1)

    return word


def is_anagram(string1, string2):
    string1 = anagrama(string1).lower()
    string2 = anagrama(string2).lower()

    return (string1, string2, string1 == string2)
