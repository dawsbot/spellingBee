#!/usr/bin/env python

import re
import json 
import enchant
import urllib2

print "These are the contents in your README of interest:\n"
print urllib2.urlopen("https://raw.githubusercontent.com/dawsonbotsford/mispell/master/README.md").read()

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
