i__author__ = "Sean R. Vinas"
__date__ = "30 November 2014"
__doc__ = """Convert a cardinal number to a Roman numeral. Reads lines from a
text file, each line contains a cardinal number. For each line output it's
roman numeral equivalent."""


from sys import argv


def break_down_digit(digit, position):
    """ converts a digit to a list of sub digits
    Args:
	digit: a string digit
	position: what decimal place it is (10's, 100's, etc)
    Returns:
	digit_list: a list of digits broken down
    For example:
    >>> break_down_digit('3', 0)
    ['1', '1', '1']

    >>> break_down_digit('3', 2)
    ['100', '100', '100']

    >>> break_down_digit('6', 0)
    ['5', '1']
    """
    digit_list = []
    if digit in '1459':
	digit_list = [digit]
    else:
	int_digit = int(digit)
	if int_digit < 5:
	    for i in range(int_digit):
		digit_list.append('1')
	else:
	    digit_list.append('5')
	    for i in range(int_digit-5):
		digit_list.append('1')
    d = ''
    for i in range(len(digit_list)):
	d = digit_list[i]
	for n in range(position):
	    d += '0'
	digit_list[i] = d
    return digit_list


def cardinal_to_roman(cardinal, roman_lookup):
    """Converts a cardinal number to a roman number.
    Args:
	cardinal: a single digit, 0-9
	roman_lookup: a dictionary object that contains a digit to roman
	    conversion
    Returns:
	roman: A roman numeral string
    For example:
    >>> cardinal_to_roman('1', {'1':'I', '4':'IV', '5':'V', '9':'IX', '10':'X',
    ... '40':'XL', '50':'L', '90':'XC', '100':'C', '400':'CD',
    ... '500':'D', '900':'CM', '1000':'M'})
    'I'
    """
    if cardinal == '0':
    	return ''
    elif cardinal in roman_lookup:
    	return roman_lookup[cardinal]
    else:
    	return 'Error'


def roman(cardinal_list, roman_lookup):
    """
    digits_to_cardinal([['100', '100', '100'], ['1']], {'1':'I', '4':'IV',
    	'5':'V', '9':'IX', '10':'X', '40':'XL', '50':'L', '90':'XC', '100':'C',
    	'400':'CD', '500':'D', '900':'CM', '1000':'M'}))
    ['C', 'C', 'C', 'I']
    """
    roman = []
    for c in cardinal_list:
    	for i in c:
	    roman.append(cardinal_to_roman(i, roman_lookup))
    return roman


def decode(cardinal, roman_lookup):
    """
    Args:
	cardinal: a string representation of a number
	roman_lookup: a dictionary of the roman numerals as strings
    Returns:
	a list of string roman numerals
    For example:
    >>> decode('296', {'1':'I', '4':'IV', '5':'V', '9':'IX', '10':'X', '40':'XL',
    ... '50':'L', '90':'XC', '100':'C', '400':'CD', '500':'D', '900':'CM',
    ... '1000':'M'})
    ['C', 'C', 'XC', 'V', 'I']

    >>> decode('3992', {'1':'I', '4':'IV', '5':'V', '9':'IX', '10':'X',
    ... '40':'XL', '50':'L', '90':'XC', '100':'C', '400':'CD', '500':'D',
    ... '900':'CM', '1000':'M'})
    ['M', 'M', 'M', 'CM', 'XC', 'I', 'I']
    """
    number = []
    len_cardinal = len(cardinal)-1
    for c in range(len(cardinal)):
    	number.append(break_down_digit(cardinal[c], len_cardinal))
    	len_cardinal -= 1
    return roman(number, roman_lookup)


def main():
    """Read a text file line by line which is defined by input argument.
    Each line is a number, convert it to it's roman numeral equivalent and
    display it."""
    roman_lookup = {'1':'I', '4':'IV', '5':'V', '9':'IX', '10':'X', '40':'XL',
	'50':'L', '90':'XC', '100':'C', '400':'CD', '500':'D', '900':'CM',
	'1000':'M'}
    textfile = open(argv[1], 'r')
    for line in textfile:
	cardinal = line.rstrip('\n')
	print(*decode(cardinal, roman_lookup), sep='')
    textfile.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
