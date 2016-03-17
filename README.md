# Word-Path-Finder

## Outline

The problem is to find “word paths”. What this means is that you find a path from one word to 
another word, changing one letter each step, and each intermediate word must be in the 
dictionary.

We tend to use the dictionary file on a linux in /usr/share/dict/words. 

Some example solutions:

rial -> real -> feal -> foal -> foul -> foud

yagi ­> yali ­> pali ­> palp ­> paup -> plup -> blup

jina -> pina -> pint -> pent -> peat -> prat -> pray 

fike -> fire -> fare -> care -> carp -> camp

The program should take as input the path to the word file, any start word and an end word and 
print out at least one path from start to end, or something indicating there is no possible path if 
appropriate. e.g.

$ python ./wordpaths.py /usr/share/dict/words cat dog

cat -> cag -> cog -> dog
