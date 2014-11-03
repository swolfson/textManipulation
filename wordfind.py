'''
a script to find hidden words of a defined length in a sentence
Ex:  "hope only traps a peasant" 
	---hidden 4 letter word "peon"
	---hidden 3 letter word "sap", "ant", "rap", etc
'''
from sys import argv
import string
import json

script, n_letters, insentence = argv


test_sentence = "hope only traps. a peasant"

#remove all whitespace and punctuation from the input string
def clean_input(in_sentence):
	exclude = set(string.punctuation).union(set(string.whitespace))
	sentence = ''.join(ch for ch in in_sentence if ch not in exclude)
	return sentence

def import_dictionary(wordlength,dictionary="word_length_dictionary.json"):
	with open(dictionary) as f:
		allwords = json.load(f)
	wordlist = allwords[wordlength].replace(',','').split()
	return wordlist

def find_words(insentence, wordlength):
	wordlist = import_dictionary(wordlength)
	sentence = clean_input(insentence)
	print "looking for words of %r letters in:" %n_letters
	print insentence
	for i in range(0,len(sentence)):
		scan = sentence[i:i + int(wordlength)]
		if scan.upper() in wordlist: print scan



if __name__=="__main__":
	print "starting"
	find_words(test_sentence,n_letters)
	find_words(insentence,n_letters)
