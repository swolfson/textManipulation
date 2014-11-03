from sys import argv
import json
import itertools
import string
#os_dictionary = "/usr/share/dict/words"
os_dictionary = "./scrabblewords.txt"

script, command, targetword = argv

#creates a dict for fast anagram searching
def make_anagram_dictionary(wordbank=os_dictionary):
	all_words  = [line.strip() for line in open(wordbank)]
	print "dict loaded"
	i = -1
	anagram_dictionary = {}
	for word in all_words:
		i += 1
		print i
		k = "".join(sorted(word))
		try:
			val = anagram_dictionary[k]
			anagram_dictionary[k] = val + ", " +  word
		except KeyError:
			anagram_dictionary[k] = word
		
	with open('anagram_dictionary.json','w') as f:
		json.dump(anagram_dictionary,f)
	print "dump complete"

def find_anagrams(targetword,andict='anagram_dictionary.json'):
	with open(andict) as f:
		anDict = json.load(f)
	word = "".join(sorted(targetword))
	return anDict[word]

def break_word(inword):
	combos = []
	for L in range(0,len(inword)+1):
		for subset in itertools.combinations(inword,L):
			combos.append("".join(subset))
	return combos

def find_all_anagrams(word,andict='anagram_dictionary.json'):
	all_anagrams = []
	with open(andict) as f:
		anDict = json.load(f)
	combos = break_word(word)
	for word in combos:
		wordkey = "".join(sorted(string.upper(word)))
		try:
			all_anagrams.append(anDict[wordkey])
			print anDict[wordkey]
		except KeyError:
			pass	
	return all_anagrams

if __name__=="__main__":
	if command == "make":
		make_anagram_dictionary()
	elif command == "find":
		#print find_anagrams(targetword)
		#print "that was the full word"
		#print find_all_anagrams(targetword,'anagram_dictionary2.json')
		print find_all_anagrams(targetword)
	else:
		print "command has to be either make or find"

