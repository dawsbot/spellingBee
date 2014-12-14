#!/usr/bin/env python

import re
import json 
import enchant

f = open('words.json', 'rw')
print json.loads(f.read())[0]

checker = enchant.Dict("en_US")
myString = "Tis is a rpository wher I purposly hav mispelled sevral importat wordss!"
print myString
#myString = myString.replace(" rpository ", " repository ")
splitUp = re.compile('\w+').findall(myString)

for word in splitUp:
  if (not checker.check(word)):
    #print word, " is wrong. How about ", checker.suggest(word)[0], "?"
    #if word.lower 
    myString = re.sub(word, checker.suggest(word)[0], myString)
 
print myString 
