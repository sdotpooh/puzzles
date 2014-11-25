from sys import argv


def main():
    f = open(argv[1])
    for line in f:
        line = list(map(int, line.rstrip('\n').split(',')))
        for i in range(line[1], sum(line), line[1]):
            if i >= line[0]:
                print(i)
                break
    f.close()


if __name__ == '__main__':
    main()
