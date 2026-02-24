def calc_prime_factors_optimized(value):
    all_primes = calc_primes_up_to(value)
    prime_factors = []
    remaining_value = value
    while remaining_value > 1:
        for current_prime in all_primes:
            while remaining_value % current_prime == 0:
                remaining_value = remaining_value // current_prime
                prime_factors.append(current_prime)
    return prime_factors

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

print(calc_prime_factors_optimized(14))