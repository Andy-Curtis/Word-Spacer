from SymbolicRules import *
from parcer import *


def ClauseFeeder(Clause):
    for x in range (0, len(Clause)):
        print(Clause[:x])

buildDict()

print(is_vowel_present("hghgfh"))
print(is_vowel_present("dog"))


#ClauseFeeder("Thequickbrownfoxjumpedoverthelazydog.")

