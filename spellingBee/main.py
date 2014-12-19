#!/usr/bin/env python
'''
  Author: Dawson Botsford
  Purpose: Fork, edit, and pull request conservative
  spelling suggestions from a GitHub repo's readme
  Date: Fri Dec 19, 2014

'''

import re
import json 
import enchant
import urllib2

wordDict = {}
checker = enchant.Dict("en_US")
with open("words.txt") as f:
  for line in f:
    (key, value) = line.split("->")
    wordDict[key] = value.rstrip()

print "These are the contents in your README of interest:\n"
myString = urllib2.urlopen("https://raw.githubusercontent.com/dawsonbotsford/mispell/master/README.md").read()

print myString
splitUp = re.compile('\w+').findall(myString)

for word in splitUp:
  if (not checker.check(word)):
    #print word, " is wrong. How about ", checker.suggest(word)[0], "?"
    #Only replace if the replacement is found within words.txt
    if (word in wordDict):
      myString = re.sub(word, wordDict[word], myString)
 
print myString 
