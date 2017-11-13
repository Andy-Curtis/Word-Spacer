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

def was_known_in_dictionary(word):
    for words in dictionary:
        if word[:(len(word)-1)] == words[:len(word) - 1]:
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

debug = False #Print out debugging info if set to true
LastKnownWord = 0
Split = "NotYet"

def RunRules(word):
    global debug
    global LastKnownWord
    debug = ""
    global x
    global Split
    
    #High fear factor = more likely to be a word
    #Low fear factor = less likely to be a word

    if (is_word_in_dictionary(word)):
        LastKnownWord = x
    
    if(is_word_in_beginning_of_dictionary(word) == 0 and was_known_in_dictionary(word) == 1):
        Split = "LastKnownWord"
        if debug: print("It is no longer a word in the beggining of dict, but was last time")
    
    if(len(word) > 3 and was_known_in_dictionary(word) == 0):#Length = 4 and not a konwn word
        if debug: print("4 or longer and not in dictionary")
        if(word_end_in_ly_or_ed(word)):
            Split = "Here"

    if(len(word) > 4 and was_known_in_dictionary(word) == 0):#Length = 5 and not a konwn word
        if debug: print("4 or longer and not in dictionary")
        if(word_end_in_ing(word)):
            Split = "Here"

    if(len(word) > 5 and was_known_in_dictionary(word) == 0):#Length = 6 and not a konwn word
        if(check_for_common_last_letters(word)):#e,s,t,d,n
            Split = "Here"
            
    if(len(word) > 3 and was_known_in_dictionary(word) == 0):
        if(check_contractions(word) == 1):
            Split = "Here"
       
def ClauseFeeder(Clause):
    global x
    global LastKnownWord
    global Split
    LastKnownWord = 0
    SpacedClause = ""
    i = 0
    x = 1
    OneAgo = 0
    while(x < len(Clause)):
        possibleWord = Clause[i:x]
        if debug: print(possibleWord)
        RunRules(possibleWord)

        if (is_vowel_not_present(possibleWord) == 0):
            if (Split == "LastKnownWord"):
                xTemp = x
                if(x != OneAgo):
                    x = LastKnownWord
                    SpacedClause = SpacedClause + " " + Clause[i:x]
                    i = x
                    Split = "NotYet"
                #The infinite loop killer
                else:
                    Split = "NotYet"
                OneAgo = xTemp
            if (Split == "Here"):
                LastKnownWord = x
                SpacedClause = SpacedClause + " " + Clause[i:x]
                i = x
                Split = "NotYet"
        
        if (x == len(Clause) -1):
            SpacedClause = SpacedClause + " " + Clause[i:x + 1]
        x += 1
        if debug: print("Last known word: " + str(LastKnownWord))
    print(Clause)
    print(SpacedClause)
    print("")
    if debug: ihduahgdgfvat = input("ready?")


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

def main():
    print('creating new dictionary')
    time.sleep(3)
    buildDict()
    print("done making dictionary")

    create_clause('ch9Test.txt')
    



main()
