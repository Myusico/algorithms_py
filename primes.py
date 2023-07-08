import time


def sieve_primes(n):
    numbers = [True for i in range(n + 1)]
    i = 3
    while i * i <= n:
        if numbers[i]:
            for j in range(3 * i, n + 1, i + i):
                numbers[j] = False
        i += 2
    primes = [2]
    for i in range(3, n + 1, 2):
        if numbers[i]:
            primes.append(i)
    return primes


def factor_sieve(n):
    factors = [0 for i in range(n + 1)]
    primes = []
    for i in range(2, n + 1):
        if factors[i] == 0:
            factors[i] = i
            primes.append(i)
        for prime in primes:
            if prime > factors[i] or prime * i > n:
                break
            factors[prime * i] = prime
    return primes


def factorize(n, primes):
    factors = []
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            while n % p == 0:
                n //= p
            factors.append(p)
    if n > 1:
        factors.append(n)
    return factors


def is_coprime(n, factors):
    for p in factors:
        if p > n:
            break
        if n % p == 0:
            return False
    return True


def phi(n):
    """Euler's totient function"""
    result = n
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        result -= result // 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 2
    if n > 1:
        result -= result // n
    return result


def phi_with_primes(n, primes):
    """Euler's totient function with pre-computed primes"""
    result = n
    for p in primes:
        if p * p > n:
            break
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
    if n > 1:
        result -= result // n
    return result


def gcd(a, b):
    remain = a % b
    while remain != 0:
        a = b
        b = remain
        remain = a % b
    return b


def extended_euclidean(a, b):
    s = 1
    t = 0
    u = 0
    v = 1
    # pre-condition: a=sA+tB and b=uA+vB
    while b != 0:
        q = a//b
        r = a % b
        a = b
        b = r
        new_u = s-q*u
        new_v = t-q*v
        s = u
        t = v
        u = new_u
        v = new_v
    # post_condition: gcd(A,B)=a=sA+tB
    return a, s, t
