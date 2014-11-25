'''Sean Vinas 14 Nov 2014.'''

def palindromes():
    pal = []
    for x in range(9, 0, -1):
        for y in range(9, -1, -1):
                pal.append(int(str(x)+str(y)+str(x)))
    for i in range(99, 10, -11):
        pal.append(i)
    return pal

def is_prime(n):
    for i in range(2, n, 1):
        if n%i==0:
            return False
    return True

def find_largest_prime(l):
    for x in l:
        if is_prime(x) == True:
            return x
    return 0


def main():
    print(find_largest_prime(palindromes()))


if __name__ == '__main__':
    main()
