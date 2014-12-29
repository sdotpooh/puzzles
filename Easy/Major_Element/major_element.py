__author__ = "Sean R. Vinas"
__date__ = "2 December 2014"
__doc__ = """The major element in a sequence with the length of L is the element which appears in a sequence more than L/2 times. The challenge is to find that element in a sequence."""


from sys import argv


def max_frequency(numbers):
	"""Find the element in numbers with more than half occurrences.
	Args:
		numbers: A list of numbers
	Returns:
		freq_dict: A dictionary of numbers as keys and frequency as values
	For example:
	>>> max_frequency(['1', '2', '1', '3', '1', '2', '1'])
	'1'

	>>> max_frequency(['1', '2', '1', '3', '1', '2'])
	'None'
	"""
	threshold = len(numbers)/2
	freq_dict = dict()
	max_value = 0
	max_key = ''
	for n in numbers:
		if n in freq_dict:
			freq_dict[n] += 1
			if freq_dict[n] > max_value:
				max_value = freq_dict[n]
				max_key = n
		else:
			freq_dict[n] = 1
	if max_value > threshold:
		return max_key
	else:
		return 'None'


def main():
	""" Read each line in text file, find & print major element."""
	textfile = open(argv[1], 'r')
	for line in textfile:
		line = line.rstrip('\n').split(',')
		print(max_frequency(line))
	textfile.close()


if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
