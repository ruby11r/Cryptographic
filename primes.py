#!usr/bin/env python3
from functools  import wraps
from time import perf_counter
from math import sqrt
from random import seed, choice

# Processing time using a closure and decorator
def timeit(fn):
    @wraps(fn)
    def execute(*args, **kwargs):
        start = perf_counter()
        r = fn(*args, **kwargs)
        end = perf_counter()
        print(f'{fn.__name__} execution duration: {end - start:.4f} seconds')
        return r
    return execute


class PrimeNumber:
     # Generates a list of prime numbers
    def __init__(self, ran_seed):
        self.ran_seed = ran_seed

    # Processing time
    def is_prime_a(self, n):
        """
        Check if n is a prime number. denominators checked up to n//2
        """
        if n < 2:
            return False

        for i in range(2, n // 2 + 1):
            if n % i == 0:
                return False
        return True

    def is_prime_b(self, n):
        """
        Check if n is a prime number. denominators checked up to the square root of n
        """
        if n < 2:
            return False

        for i in range(2, int(sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True


    def generate_primes(self, rng: tuple, fn):
        """
        Generate a list of prime numbers within a range from rng[0] to rng[1]
        """
        # rng as two numbers tuple inclusively
        if rng[0] < 2 or rng[1] < 2 or (rng[1] <= rng[0]):
            print('>> Error: Invalid number range, try again!')
            return -1
        results = []
        print('>> INFO: Generating prime numbers....')
        for n in range(rng[0], rng[1] + 1):
            if fn(n):
                results.append(n)
        print('>> total {0} prime numbers generated!'.format(len(results)))
        return results

    @timeit
    def pick_primes(self, rng: tuple, fn, nr):
        """
        pick nr prime numbers within rng[0] to rng[1]
        params
        rng: the range of numbers to pick
        nr: the number of prime numbers to pick
        fn: the function to generate prime numbers, is_prime_a or is_prime_b
        """
        results = []
        if self.ran_seed is not None:
            seed(self.ran_seed)
            lst = self.generate_primes(rng, fn)
            results = [choice(lst) for _ in range(nr)]
            return results
        return None