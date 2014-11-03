import json
from anagram import find_all_anagrams
import string

with open('anagram_dictionary.json') as f:
	anDict = json.load(f)
i = 0
#for key in anDict.keys():
#	newkey = string.upper(key)
#	print newkey
#	print key
#	anDict[newkey] = anDict[key]
#	anDict.pop(key)
#	i = i+1
#	print i
for key in anDict.keys():
	if len(key) == 1 and (key != 'A' and key != 'I'):
		print "popped"
		anDict.pop(key)

anDict['I'] = 'I'
with open('anagram_dictionary2.json', 'w') as f:
	json.dump(anDict,f)

#print find_all_anagrams("hello",'anagram_dictionary1.json')
#print find_all_anagrams("map",'anagram_dictionary1.json')
#print find_all_anagrams("fix",'anagram_dictionary1.json')
print find_all_anagrams("mellow",'anagram_dictionary2.json')
		


