import math

n = 100


# perform the Sieve of Eratosthenes algorithm and return all primes <= n
def sieve_of_eratosthenes():
    all_numbers = [*range(2, int(n + 1))]
    # r = 2
    # delete = r + r
    primes_up_to_n = ""
    # if n < r:
    # primes_up_to_n = ["empty"]
    # while r <= math.ceil(math.sqrt(n)):
    #  while delete <= n:
    #    if all_numbers.__contains__(delete):
    #      all_numbers.remove(delete)
    # delete += r
    # r += 1
    # delete = r + r
    # primes_up_to_n = all_numbers

    if n < 2:
        primes_up_to_n = ["empty"]
    else:
        for j in all_numbers:
            for i in range(2, n+1):
                if all_numbers.__contains__(i * j):
                    all_numbers.remove(i * j)

        primes_up_to_n = all_numbers
    return primes_up_to_n


print(sieve_of_eratosthenes())
