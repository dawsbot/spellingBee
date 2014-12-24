spellingBee
============

Takes a repo URL and performs a spell check on the README file. Upon finding a mapped correction in  ```/spellingBee/words.txt```, Dawson's Spelling Bee now forks, edits, and pull requests these spelling suggestions!<br>

```words/words.txt``` is where all of the corrections are mapped.

Word mappings generated from ```http://en.wikipedia.org/wiki/Wikipedia:Lists_of_common_misspellings/For_machines``` 

Next to add to word list is ```http://cpansearch.perl.org/src/APOCAL/Pod-Spell-CommonMistakes-1.000/lib/Pod/Spell/CommonMistakes/WordList.pm```

Credit to [holdenk](https://github.com/holdenk) for the origin implementation in Perl available [here](https://github.com/holdenk/holdensmagicalunicorn)<br>

