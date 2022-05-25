# Don't forget to run the tests (and create some of your own)
def count_char(input_string):
	"""
	Given a string, return a dictonary with its character as keys
	and values as the number of times the character shows up in the string.
	"""
	string_ = [char.lower() for char in input_string if char != ' '] #to account for uppercase
	char_dict = {}
	for char in string_:
		if char in char_dict:
			char_dict[char] +=1
		else:
			char_dict[char] = 1 #if not in dict, then add an entry with value 1

	return char_dict

def is_character_match(string1, string2):
	"""
	Given two strings, return True if the number characters match.
	"""
	char_dict1 = count_char(string1)
	char_dict2 = count_char(string2)

	for k,v in char_dict1.items():
		if k not in char_dict2: #a char in string1 not in string2
			return False
		elif k in char_dict2:
			if char_dict1[k] != char_dict2[k]:
				return False
		
	return True
	
def anagrams_for(word, list_of_words):
	"""
	Given a string and a list of strings, return a list of all the words that 
	are anagrams.
	"""
	anagrams = []
	for word_ in list_of_words:
		if is_character_match(word, word_): #helper func to test each word
			anagrams.append(word_)

	return anagrams
	

