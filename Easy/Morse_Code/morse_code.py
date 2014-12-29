__author__ = "Sean R. Vinas"
__date__ = "2 December 2014"
__doc__ = """ """


from sys import argv


def main():
    """Print out each word to its morse code equivalent."""
    morse = {'.-':'A', '-...':'B', '-.-.':'C', '-..':'D', '.':'E', '..-.':'F', '--.':'G', '....':'H', '..':'I', '.---':'J', '-.-':'K', '.-..':'L', '--':'M', '-.':'N', '---':'O', '.--.':'P', '--.-':'Q', '.-.':'R', '...':'S', '-':'T', '..-':'U', '...-':'V', '.--':'W', '-..-':'X', '-.--':'Y', '--..':'Z', '.----':'1', '..---':'2', '...--':'3', '....-':'4', '.....':'5', '-....':'6', '--...':'7', '---..':'8', '----.':'9', '-----':'0'}
    textfile = open(argv[1], 'r')
    for line in textfile:
    	line = line.rstrip('\n').split('  ')
    	for n in line:
            for i in n.split():
    		print(morse[i], sep='', end='')
	    print(' ', sep='', end='')
	print()
    textfile.close()


if __name__ == "__main__":
    main()
