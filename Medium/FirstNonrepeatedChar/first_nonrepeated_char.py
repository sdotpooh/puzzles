from sys import argv


def main():
    filename = argv[1]
    f = open(filename)
    for line in f:
        line = list(line)
        for c in line:
            if line.count(c) == 1:
                print(c)
                break


if __name__ == '__main__':
    main()
