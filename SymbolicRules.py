
dictionary = {}
textFile = []
with open("textFile.txt", "r") as file:
    for line in file:
        for chara in line:
            textFile.append(chara)
finishedText = ""
inputArray = []


# there is a method that checks for punctuation, but it has added ones that we don't use so
# I created a new one that checks for the ones we mentioned.
def ispunct(char):
    if char == "," or char == "." or char == ":" or char == ":" or char == "\"" or char == "!" or char == "?":
        return True
    else:
        return False


def is_vowel_present(word):
    for ch in word:
        if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"
                or ch == "y"):
            return 1
    return 0


def word_end_in_ing(word):
    if word[-3:] == "ing":
        return 1
    else:
        return 0


def word_end_in_y_or_s(word):
    if word[-1:] == "s" or word[-1:] == "y":
        return 1
    else:
        return 0


def word_end_in_ly(word):
    if word[-2:] == "ly":
        return 1
    else:
        return 0


def is_word_in_dictionary(word):
    for words in dictionary:
        if word == words:
            return 1
    return 0


def is_word_contained_in_dictionary(word):
    for words in dictionary:
        if word in words:
            return 1
    return 0


def is_word_in_beginning_of_dictionary(word):
    for words in dictionary:
        if word == words[:len(word)]:
            return 1
    return 0


def is_last_letter_capital(word):
    if word[-1:].isupper():
        return 1
    else:
        return 0


def check_contractions(word):
    if word[len(word) - 2] == "'":
        if word[-1:] == "m" or word[-1:] == "s" or word[-1:] == "d" or word[-1:] == "t":
            return 1
    if word[len(word) - 3] == "'":
        if word[-2:] == "re" or word[-2:] == "ve" or word[-2:] == "ll":
            return 1
    return 0


def check_for_common_first_letters(word):
    if word[1] == "t" or word[1] == "o" or word[1] == "a" or word[1] == "w" \
            or word[1] == "b" or word[1] == "s":
        return 1
    else:
        return 0


def check_for_common_last_letters(word):
    if word[-1:] == "e" or word[-1:] == "s" or word[-1:] == "t" \
            or word[-1] == "d" or word[-1:] == "n":
        return 1
    else:
        return 0


def check_for_possession(word):
    if word[-2:] == "'s":
        return 1
    else:
        return 0


# def create_clause(inputs):
#     if not inputs:
#         return ""
#     clause = []
#     index = 0
#     for i in range(inputs):
#         clause[index] = inputs[i]
#         index += 1
#         if inputs[i] == "," or inputs[i] == ".":
#             rules(clause)
#             index = 0
#             break

# TODO: May need to do something with this. Will leave until we discuss

def rules(inputs):
    word = ""
    global finishedText
    for i in range(inputs):
        word += inputs[i]
        if inputs[i].isalpha() and ispunct(inputs[i+1]):
            finishedText += word + inputs[i+1] + " "
            # skip the punctuation
            i += 1
            word = ""
            break

