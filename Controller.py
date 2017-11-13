#Controller

print("hi")

########################################3
#Parcer.py

import os
import time
import string
dictionary = {}
def makeLines(file):
    wordFile = open(file, 'r')
    for line in wordFile:
        line = line.strip()
       # print(line)
        makeWords(line)

def makeWords(line):
    word = ''
    for letter in line:
        if letter == ' ':
            #print('space')
            #print(word)
            saveWordtoDict(word)
            word = ''
        elif letter == "," or letter == ':' or letter == ';' or letter == ":"or letter == '"' or letter == '.' or letter == '?' or letter == '!'or letter == '(' or letter == ')':
            pass
            #keep ' and - nothing else punc wise
        else:
            word = word + letter

def saveWordtoDict(word):
    global dictionary
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

def buildDict():
    makeLines('holyHandGrenade.txt')
    makeLines('frankch1.txt')
    makeLines('frankch2.txt')
    makeLines('frankch3.txt')
    makeLines('frankch4.txt')
    makeLines('frankch5.txt')
    makeLines('frankch6.txt')
    makeLines('frankch7.txt')
    makeLines('frankch8.txt')

def create_clause(file):
    testfile = open(file)
    clause = ''
    for line in testfile:
        for ch in line:
            clause = clause + ch
            if ch == "," or ch == ':' or ch == ';' or ch == ":" or ch == '"' or ch == '.' or ch == '?' or ch == '!':
                #ClauseFeeder(clause)
                #ruleset(clause) best place to feed caluses into ruleset
                clause = ''
    print("done creating clause")


###################################################
# Symbolic Rules

def ispunct(char):
    if char == "," or char == "." or char == ":" or char == ":" or char == "\"" or char == "!" or char == "?":
        return True
    else:
        return False


def is_vowel_not_present(word):
    for ch in word:
        if (ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u"
                or ch == "y" or ch == "A" or ch == "E" or ch == "I" or ch == "O" or ch == "U"
                or ch == "Y"):
            return 0
    return 1

def is_I(word):
    if word == "I":
        return 1
    else:
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


def word_end_in_ly_or_ed(word):
    if word[-2:] == "ly" or word[-2:] == "ed":
        return 1
    else:
        return 0


def is_word_in_dictionary(word):
    for words in dictionary:
        if word == words:
            return 1
    return 0

def had_word_in_dictionary(word):
    for words in dictionary:
        if word[:(len(word)-1)] == words or word[:(len(word)-2)] == words:
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
    if word[-1:].isupper() and len(word) > 1:
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


def length_of_word(word):
    return len(word)


def check_frequency_of_word_in_dictionary(word):
    return dictionary[word]

######################################################
# Fear Factor

FearFactorOld = -100.0
FearFactorNew = -100.0
debug = ""

def RunRules(word):
    global FearFactorOld
    global FearFactorNew
    global debug
    debug = ""
    FearFactorOld = FearFactorNew
    #High fear factor = more likely to be a word
    #Low fear factor = less likely to be a word
    FearSum = 0.0

    FearSum += (is_vowel_not_present(word) * -10.0)
    debug += " " + str(is_vowel_not_present(word))
    
    FearSum += (is_I(word) * 1.0)
    debug += " " + str(is_I(word))
    
    FearSum += (word_end_in_ing(word) * 0.9)
    debug += " " + str(word_end_in_ing(word))
    
    FearSum += (word_end_in_y_or_s(word) * 0.2)
    debug += " " + str(word_end_in_y_or_s(word))
    
    FearSum += (word_end_in_ly_or_ed(word) * 0.5)
    debug += " " + str(word_end_in_ly_or_ed(word))
    
    FearSum += (is_word_in_dictionary(word) * 20.0)
    debug += " " + str(is_word_in_dictionary(word))

    if (is_word_in_dictionary(word) == 0):
        FearSum += (had_word_in_dictionary(word) * -4.0)
        debug += " " + str(had_word_in_dictionary(word))
    else:
        debug += " " + "0"
    
    FearSum += (is_word_in_beginning_of_dictionary(word) * -20.0)
    debug += " " + str(is_word_in_beginning_of_dictionary(word))
    
    FearSum += (is_last_letter_capital(word) * -6.0)
    debug += " " + str(is_last_letter_capital(word))
    
    FearFactorNew = FearSum

def ClauseFeeder(Clause):
    SpacedClause = ""
    i = 0
    x = 1
    while(x < len(Clause)):
        possibleWord = Clause[i:x]
        print(possibleWord)
        RunRules(possibleWord)
        print(FearFactorNew)
        print(debug)

        if (FearFactorOld < 0):
            if (FearFactorNew < (FearFactorOld * 1.1)):
                x = x - 1
                SpacedClause = SpacedClause + " " + Clause[i:x]
                i = x
        else:
            if (FearFactorNew < (FearFactorOld * 0.95)):
                x = x - 1
                SpacedClause = SpacedClause + " " + Clause[i:x]
                i = x
            
        
        if (x == len(Clause) -1):
            SpacedClause = SpacedClause + " " + Clause[i:x + 1]
        x += 1
    print(Clause)
    print(SpacedClause)
    ihduahgdgfvat = input("go")


def create_clause(file):
    testfile = open(file)
    clause = ''
    for line in testfile:
        for ch in line:
            clause = clause + ch
            if ch == "," or ch == ':' or ch == ';' or ch == ":" or ch == '"' or ch == '.' or ch == '?' or ch == '!':
                #print(clause)
                ClauseFeeder(clause)
                #ruleset(clause) best place to feed caluses into ruleset
                clause = ''
    print("done creating clause")

def main():
    print('creating new dictionary')
    time.sleep(3)
    buildDict()
    print("done making dictionary")

    create_clause('ch9Test.txt')
    



main()
