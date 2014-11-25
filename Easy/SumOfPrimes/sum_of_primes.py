'''Sean Vinas 14 Nov 2014.'''
from itertools import count, islice


def primes(n):
    prime_list = []
    for i in islice(count(), 2, None):
        if len(prime_list) == n:
            return prime_list
        if is_prime(i):
            prime_list.append(i)
    return prime_list


def is_prime(n):
    for i in range(2, n):
        if n%i==0:
            return False
    return True


def main():
    print(sum(primes(1000)))


if __name__ == '__main__':
    main()
