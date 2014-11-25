''' Sean Vinas 14 Nov 2014'''
from sys import argv


def main():
    f = open(argv[1])
    for line in f:
        line = line.rstrip('\n').split(';')
        set_a = set(map(int, line[0].split(',')))
        set_b = set(map(int, line[1].split(',')))
        inter = set_a.intersection(set_b)
        print(*inter, sep=',')

    f.close()


if __name__ == '__main__':
    main()
