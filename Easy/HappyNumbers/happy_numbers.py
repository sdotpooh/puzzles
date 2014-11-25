''' Sean Vinas 14 Nov 2014'''
from sys import argv


def sum_squares(s):
    return str(sum([squares[c] for c in s]))


def happy(s):
    duplicate = set()
    while s not in duplicate:
        if s == '1':
            duplicate.clear()
            return 1
        duplicate.add(s)
        s = sum_squares(s)
    duplicate.clear()
    return 0


def main():
    global squares
    squares = dict(zip([str(i) for i in range(10)],
        [i*i for i in range(10)]))

    f = open(argv[1])
    for line in f:
        x = line.rstrip('\n')
        print(happy(x))
    f.close()


if __name__ == '__main__':
    main()
