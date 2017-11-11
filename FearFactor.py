from SymbolicRules import *

FearFactorOld = 0.0
FearFactorNew = 0.0

def RunRules(word):
    global FearFactorOld
    global FearFactorNew
    FearFactorOld = FearFactorNew
    FearSum = 0.0
    FearSum += (is_vowel_present(word) * -1.0)
    FearSum += (word_end_in_ing(word) * -3.0)
    FearSum += (word_end_in_y_or_s(word) * -0.3)
    FearSum += (word_end_in_ly(word) * -0.5)

    FearFactorNew = FearSum

def ClauseFeeder(Clause):
    SpacedClause = ""
    i = 0
    for x in range (0, len(Clause)):
        possibleWord = Clause[i:x]
        print(possibleWord)
        RunRules(possibleWord)
        print(FearFactorNew)
    print(SpacedClause)
    


ClauseFeeder("Thequickbrownfoxjumpedoverthelazydog.")


#print(is_word_in_dictionary("The"))

#possibleWord[len(possibleWord)-1:]
#This is the last letter of the word
