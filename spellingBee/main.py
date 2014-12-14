#!/usr/bin/env python

from enchant.checker import SpellChecker
checker = SpellChecker("en_US")

checker.set_text("Tis is a rpository wher I purposly hav mispelled sevral importat wordss!")

for err in checker:
  print err.word, " is not a word. How about ", checker.suggest(err.word)[0], "?"

