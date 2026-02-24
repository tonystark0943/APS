def calc_primes_up_to(max_value):
    primes = []
    for n in range(2, max_value + 1):
        is_prime = True
        for p in range(2, int(n ** 0.5) + 1):
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
    return primes

prime = calc_primes_up_to(25)
print(prime)