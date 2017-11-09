#Takes in text file and parses the dict for AI to use
#version 1.0
#11/6/2017
#Kyle Boutin
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
    makeLines('frankch9.txt')




#main Only thing running at the begining
print('creating new dictionary')
time.sleep(3)
buildDict()
print'done making dictionary'
for k in dictionary:
    print k , dictionary[k]

print 'finished printing dictionary'