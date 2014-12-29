__author__ = "Sean R. Vinas"
__date__ = "7 December 2014"
__doc__ = """In a given text, if there are two or more identical characters in sequence, delete the repetitions and leave only the first character."""


from sys import argv

def trim_reps(line):
    """Print the line without sequential char repitions
    Args:
	line: String without newline char
    Returns:
	new_line
    For example:
    >>> trim_reps('S')
    'S'
    >>> trim_reps('Sss')
    'Ss'
    >>> trim_reps(' Sss')
    ' Ss'
    >>> trim_reps(' Sss ')
    ' Ss '
    """
    prev_char = ''
    line_without_reps = ''
    for n, char in enumerate(line):
	if n > 0:
	    prev_char = line[n-1]
	if char != prev_char:
	    line_without_reps += char
    return line_without_reps


def main():
    """Read line by line from a text file. For each line remove repetitions of
    characters and print."""
    textfile = open(argv[1], 'r')
    for line in textfile:
	line = line.rstrip('\n')
	print(trim_reps(line))
    textfile.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
