from sys import argv


def main():
    filename = argv[1]
    f = open(filename)
    for line in f:
        line = line.split(',')
        sentence = list(line[0])
        remove = list(line[1].strip('\n').strip(' '))
        for r in remove:
            for c in range(sentence.count(r)):
                sentence.remove(r)
        for c in sentence:
            print(c, end='')
        print()


if __name__ == '__main__':
    main()
