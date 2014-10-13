#import fileinput
from sys import argv


def main():
    filename = argv[1]
    f = open(filename)
    quantity = int(f.readline())
    lines = []
    for line in f:
        line = line.strip('\n')
        lines.append(line)
    sl = sorted(lines, key=len, reverse = True)
    for i in range(quantity):
        print(sl[i])

if __name__ == '__main__':
    main()
