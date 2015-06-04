#!/usr/bin/env python
'''
  Author: Dawson Botsford
  Purpose: Fork, edit, and pull request conservative
  spelling suggestions from a GitHub repo's readme
  Date: Fri Dec 19, 2014

'''

import re
import os
import sys
import subprocess
import enchant
import github3

usage = "ERROR, INCORRECT USAGE: ./main.py USER_OF_INTEREST REPO_OF_INTEREST [-t]"
wordDict = {}
ignoreDict = {}
checker = enchant.Dict("en_US")

#Create Github object
keys_file = open("../keys.txt")
USERNAME = keys_file.readline().rstrip() # put your github username here.
PASSWORD = keys_file.readline().rstrip() # put your github password here.
g = github3.login(USERNAME, PASSWORD)

#Check command line argument length
if (len(sys.argv) < 3 or len(sys.argv) > 4):
  print usage
  sys.exit()
  
#Parse command line arguments
target_user = sys.argv[1]
repo_name = sys.argv[2] 
if (len(sys.argv) == 4):
  training_flag = sys.argv[3] 
  if (training_flag == "-t"):
    training_mode = True
    print "Training flag set"
  else:
    print usage
    sys.exit()
else:
  training_mode = False
  print "Training flag NOT set"

#Fork the repo of interest into GitHub account
target_repo = g.repository(target_user, repo_name)
oldText = target_repo.readme().decoded

#Fill replacement dictionary from file
with open("../words/words.txt") as f:
  for line in f:
    (key, value) = line.split("->")
    wordDict[key] = value.rstrip()

#Fill ignore dictionary from file
with open("../words/ignore.txt") as f:
  for line in f:
    ignoreDict[line.rstrip()] = 1 #Provide dictionary value of 1 (using dictionary for quick hashing)

print "These are the contents in your README of interest:\n"
print oldText

newText = oldText #Create duplicate where corrections will be made

#Remove URL's and words that contain underscores from text
splitUp = re.compile('\w+').findall(re.sub(r'\b\w*_\w*\b', '', re.sub(r'https?[^\s]*', '', oldText)))

for word in splitUp:
  if (not checker.check(word)):
    if (training_mode):
      if (word in wordDict):
        #newText = re.sub(word, wordDict[word], newText)
        newText = re.sub(r"\b%s\b" % word, wordDict[word], newText)
        #newText.replace(word, wordDict[word])
        print word, " replaced with ", wordDict[word], "!"
      elif (word in ignoreDict): #Do not alert user if word is in ignore
        continue
      else: #Allow user to input new word map
        solution = raw_input("\n" + word + " unrecognized.\n* \'\' == add to ignore\n* [word] == replacement for new mapping\n* i == continue w/no new mappings: ")
        if (solution == 'i'): #user does not want this mapped
          continue
        elif (solution == ''): #user wants to map new ignore
          with open('../words/ignore.txt','a') as f: f.write(word[:1].lower() + word[1:] + "\n" + word[:1].title() + word[1:] + "\n")
          ignoreDict[word] = 1 
        else: #user wants to map new correction
          with open('../words/words.txt','a') as f: f.write(word[:1].lower() + word[1:] + "->" + solution[:1].lower() + solution[1:] + "\n" + word[:1].title() + word[1:] + "->" + solution[:1].title() + solution[1:] + "\n")
          wordDict[word] = solution
          newText = re.sub(word, wordDict[word], newText)
    else:
      if (word in wordDict):
        newText = re.sub(word, wordDict[word], newText)

'''
print "Corrected version: \n", newText 
'''
if (oldText == newText):
  print "\nThere were no changes to be made!" 
  sys.exit()

#Clone the target repo locally
target_fork = target_repo.create_fork()
clone_url = target_fork.clone_url
os.chdir("../..")
bashCommand = "git clone " + clone_url
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()

#Put new README text in place of old
os.chdir(target_fork.name)
f = open(target_fork.readme().name, 'w')
f.write(newText)
f.close()

process = subprocess.call("../spellingBee/spellingBee/gitItAll.sh", shell=True)

target_repo.create_pull("Spelling Correction from Dawson's Spelling Bee", target_repo.default_branch, "dawsonbotsford:master", "Automated corrections from https://github.com/dawsonbotsford/spellingBee . If the correction is useful, star me! Keep in mind, this is solely spelling updates for your README, it should not affect functionality.")

os.chdir("..")
bashCommand = "rm -rf " + repo_name 
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
process.wait()

#close files
keys_file.close()
