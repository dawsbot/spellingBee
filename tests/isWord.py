#!/usr/bin/env python

#Checks if inputted word is recognized as a word by enchant
import sys
import enchant

usage = "USAGE: ./isWord.py WORD_TO_CHECK"
d = enchant.Dict("en_US")
if (len(sys.argv) == 2): 
  print d.check(sys.argv[1])
else:
  print usage
