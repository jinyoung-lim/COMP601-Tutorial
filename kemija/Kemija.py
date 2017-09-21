import re

def main():
    """
    Fetches an user input. Assumes that the user gives a sentence of words
    :return:
    """
    print("User Input: ", end="")
    userinput = input()
    print("Decoded: ", end="")
    decodeKemijaSent(userinput)

    exit(0)

def decodeKemijaWord(word):
    """
    Decode a single kemija word
    :param word: a single-word string
    :return: prints a decoded string
    """
    word = word.lower()
    i = 0
    while i != len(word):
        if word[i] == "a":
            word = re.sub("apa", "a", word)
            i += 2
            break
        elif word[i] == "e":
            word = re.sub("epe", "e", word)
            i += 2
            break
        elif word[i] == "o":
            word = re.sub("opo", "o", word)
            i += 2
            break
        elif word[i] == "u":
            word = re.sub("upu", "u", word)
            i += 2
            break
        elif word[i] == "i":
            word = re.sub("ipi", "i", word)
            i += 2
            break
        i += 1

    #kemija = ["a[^aeoui]a", "e[^aeoui]e", "o[^aeoui]o", "u[^aeoui]u", "i[^aeoui]i"]

    # papapripikapa zepelepenapa
    # p apa p apa y apa

    print(word, end=" ")

    return(0)

def decodeKemijaSent(sent):
    wordList = re.split(" ", sent)
    for word in wordList:
        if word != None:
            decodeKemijaWord(word)

    return(0)


if __name__ == "__main__":
    main()