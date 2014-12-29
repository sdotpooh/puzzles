__author__ = "Sean R. Vinas"
__date__ = "2 December 2014"
__doc__ = """In this challenge you're given a random string containing hidden and visible digits. The digits are hidden behind lower case latin letters as follows: 0 is behind 'a', 1 is behind ' b ' etc., 9 is behind 'j'. Any other symbol in the string means nothing and has to be ignored. So the challenge is to find all visible and hidden digits in the string and print them out in order of their appearance."""


from sys import argv

def decode_letter(letter, latin):
	"""Check if letter is in the Latin alphabet, if so return index. If it's
	a Latin alphabet index, return index.
	Args:
		letter: Character
		latin: A dictionary mapping latin alphabet to index number
	Returns:
		If a letter is in the dictionary return it's index as a string.
		If an index is in the dictionary, return the index as a string.
		If neither return an empty string.
	For example:
	>>> decode_letter('a', {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4',
	... 'f':'5', 'g':'6','h':'7', 'i':'8', 'j':'9'})
	'0'
	"""
	if letter in latin:
		return latin[letter]
	elif letter in latin.values():
		return letter
	else:
		return ''


def decode_word(word, latin):
	"""Decode an entire word into it's latin alphabet index.
	Args:
		word: Line from the text file without \n, string.
		latin: A dictionary mapping latin alphabet to index number
	Returns:
		decoded: A string comprised of the index of each Latin character
	For example:
	decode_letter('abc', {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4',
	... 'f':'5', 'g':'6','h':'7', 'i':'8', 'j':'9'})
	'012'
	"""
	decoded = ''
	for letter in word:
		decoded += decode_letter(letter, latin)
	if len(decoded) == 0:
		decoded = 'NONE'
	return decoded


def main():
	"""Read line by line from text file, convert each character in each line
	into a decoded index value."""
	latin = {'a':'0', 'b':'1', 'c':'2', 'd':'3', 'e':'4', 'f':'5', 'g':'6',
		'h':'7', 'i':'8', 'j':'9'}
	textfile = open(argv[1], 'r')
	for line in textfile:
		line = line.rstrip('\n')
		print(decode_word(line, latin))
	textfile.close()


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
