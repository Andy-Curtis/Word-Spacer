from SymbolicRules import *

FearFactorOld = -100.0
FearFactorNew = -100.0

def RunRules(word):
    global FearFactorOld
    global FearFactorNew
    FearFactorOld = FearFactorNew
    #High fear factor = more likely to be a word
    #Low fear factor = less likely to be a word
    FearSum = 0.0
    FearSum += (is_vowel_not_present(word) * -10.0)
    FearSum += (word_end_in_ing(word) * 3.0)
    FearSum += (word_end_in_y_or_s(word) * 0.3)
    FearSum += (word_end_in_ly(word) * 0.5)
    FearSum += (is_word_in_dictionary(word) * 8.0)
    FearSum += (is_word_in_beginning_of_dictionary(word) * -8.0)
    FearSum += (is_last_letter_capital(word) * -6.0)
    
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

        if (FearFactorNew < FearFactorOld):
            x = x - 1
            SpacedClause = SpacedClause + " " + Clause[i:x]
            i = x
        if (x == len(Clause) - 1):
            SpacedClause = SpacedClause + " " + Clause[i:x]
        x += 1
    print(SpacedClause)
    


ClauseFeeder("Ibegpermissiontohaveafewwitnessesexaminedconcerningmycharacter;")


