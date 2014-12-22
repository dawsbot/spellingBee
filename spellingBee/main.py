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

repo_name = 'ChainLink'

#Fork the repo of interest into github account
target_repo = g.repository('alexwalling', repo_name)
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

#Clone the target repo locally
clone_url = target_fork.clone_url
os.chdir("../..")
bashCommand = "git clone " + clone_url
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()

print bashCommand

#Put new README text in place of old
os.chdir(target_fork.name)
f = open(target_fork.readme().name, 'w')
f.write(myString)
f.close()

'''
bashCommand = "git add -A && git status"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()
'''
bashCommand = "git add -A && git status"
process = subprocess.call("../spellingBee/spellingBee/gitItAll.sh", shell=True)

'''
bashCommand = "git commit -m \"Spelling correction automated from Dawson's Spelling Bee\""
print bashCommand
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()


bashCommand = "git push"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()
'''
'''
bashCommand = "echo \"" + myString + "\" > " + target_fork.readme().name
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()
print bashCommand
'''
