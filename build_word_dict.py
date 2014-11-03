import json
import string
scrabble_file = "scrabblewords.txt"

words = [line.strip() for line in (open(scrabble_file))]

word_length_dictionary = {}
i = 0
for word in words:
	k = len(word)
	try:
		val = word_length_dictionary[k]
		word_length_dictionary[k] = val + ", " + word
	except KeyError:
		word_length_dictionary[k] = word

	
	with open('word_length_dictionary.json','w') as f:
		json.dump(word_length_dictionary,f)
	i += 1
	print i

print "done"
