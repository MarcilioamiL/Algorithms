def anagramas(string):
    string = list(string)
    n = len(string)-1
    for i in range(n):
        for aux in range(0, n-i):
            if string[aux] >= string[aux+1]:
                string[aux], string[aux+1] = string[aux+1], string[aux]
    return "".join(string)


def is_anagram(string1, string2):
    string1 = anagramas(string1.replace("-", "")).lower()
    string2 = anagramas(string2.replace("-", "")).lower()

    return (string1, string2, string1 == string2)
