#!/usr/bin/env python
'''
  Author: Dawson Botsford
  Purpose: Fork, edit, and pull request conservative
  spelling suggestions from a GitHub repo's readme
  Date: Fri Dec 19, 2014

'''

import re
import os
import subprocess
import enchant
import github3

wordDict = {}
checker = enchant.Dict("en_US")

#Create Github object
fp = open("../keys.txt")
USERNAME = fp.readline().rstrip() # put your github username here.
PASSWORD = fp.readline().rstrip() # put your github password here.
g = github3.login(USERNAME, PASSWORD)

#Fork the repo of interest
target_repo = g.repository('alexwalling', 'ChainLink')
target_fork = target_repo.create_fork()
myString = target_fork.readme().decoded

#Fill replacement dictionary from file
with open("words.txt") as f:
  for line in f:
    (key, value) = line.split("->")
    wordDict[key] = value.rstrip()

print "These are the contents in your README of interest:\n"

print myString
splitUp = re.compile('\w+').findall(myString)

for word in splitUp:
  if (not checker.check(word)):
    #print word, " is wrong. How about ", checker.suggest(word)[0], "?"
    #Only replace if the replacement is found within words.txt
    if (word in wordDict):
      myString = re.sub(word, wordDict[word], myString)
 
print myString 

clone_url = target_fork.clone_url
os.chdir("../..")
bashCommand = "git clone " + clone_url
print bashCommand
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
