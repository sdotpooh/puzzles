__author__ = "Sean R. Vinas"
__date__ = "2 December 2014"
__doc__ = """You are given a number N and a pattern. The pattern consists of lowercase latin letters and one operation "+" or "-". The challenge is to split the number and evaluate it according to this pattern e.g.
1232 ab+cd -> a:1, b:2, c:3, d:2 -> 12+32 -> 44."""


from sys import argv


def format_line(line, decoder):
    """
    Args:
    	line: A string
    Returns:
    	list containing numbers and operators
    For example:
    >>> format_line('3413289830 a-bcdefghij', {'a':0, 'b':1, 'c':2, 'd':3,
    ... 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9})
    '3-413289830'
    """
    decoded = ''
    line = line.rstrip('\n').split()
    #['1232', 'ab+cd']
    for n in line[1]:
    	if n in decoder:
    	    decoded += line[0][decoder[n]]
	else:
            decoded += n
    return decoded


def find_operator(expression):
    """Returns the index of the mathematical operator (+,- etc)
    Args:
    	expression: A string of digits and operators
    Returns:
    	The index of the mathematical operator
    For example:
    >>> find_operator('12+34')
    2
    """
    digits = '0123456789'
    for n in range(len(expression)):
    	if expression[n] not in digits:
            return n


def trim_zeros(expression, operator_index, section):
    """Trims leading zeros from a string expression.
    Args:
    	expression: A string containing digits and math operator
    Returns:
    	An expression without leading zeros not including operator or following
    	digits
    For example:
    >>> trim_zeros('00009+0602', 5, 'leading')
    '9'

    >>> trim_zeros('0000+0602', 4, 'leading')
    '0'

    >>> trim_zeros('00009+0602', 5, 'trailing')
    '602'

    >>> trim_zeros('00009+000', 5, 'trailing')
    '0'
    """
    if section == 'leading':
    	expression = expression[:operator_index]
    else:
    	expression = expression[operator_index+1:]
    len_expression = len(expression)-1
    i = 0
    while expression[i] == '0' and i < len_expression:
    	i += 1
    if i == len_expression and expression[i] == '0':
    	return '0'
    else:
    	return expression[i:]


def trim_expression(expression):
    """	Trims leading zeros from a string expression both before and after
    math operator symbol.
    Args:
    	expression: A string containing digits and math operator
    Returns:
    	An expression without leading zeros
    For example:
    >>> trim_expression('09+0000602')
    '9+602'
    """
    operator_index = find_operator(expression)
    expression_a = trim_zeros(expression, operator_index, 'leading')
    operator = expression[operator_index]
    expression_b = trim_zeros(expression, operator_index, 'trailing')
    return expression_a+operator+expression_b


def main():
    """Read each line from text file, calculate solution based on mapping the
    numbers based on the alphabetic index."""
    decoder = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8,
    	'j':9}
    textfile = open(argv[1], 'r')
    for line in textfile:
    	print(eval(trim_expression(format_line(line, decoder))))
    textfile.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()
