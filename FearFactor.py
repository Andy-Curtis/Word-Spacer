from SymbolicRules import *

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
            
        
        if (x == len(Clause) - 1):
            SpacedClause = SpacedClause + " " + Clause[i:x]
        x += 1
    print(SpacedClause)


def create_clause(file):
    testfile = open(file)
    clause = ''
    for line in testfile:
        for ch in line:
            clause = clause + ch
            if ch == "," or ch == ':' or ch == ';' or ch == ":" or ch == '"' or ch == '.' or ch == '?' or ch == '!':
                ClauseFeeder(clause)
                #ruleset(clause) best place to feed caluses into ruleset
                clause = ''
    print("done creating clause")



create_clause("ch9Test.txt")
#ClauseFeeder("Ibegpermissiontohaveafewwitnessesexaminedconcerningmycharacter;")


