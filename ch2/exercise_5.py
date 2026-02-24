def prime_pairs(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    twin = []
    cousin = []
    sexy = []

    for n in range(2, limit + 1):
        if is_prime(n):
            if n + 2 <= limit and is_prime(n + 2):
                twin.append((n, n + 2))
            if n + 4 <= limit and is_prime(n + 4):
                cousin.append((n, n + 4))
            if n + 6 <= limit and is_prime(n + 6):
                sexy.append((n, n + 6))

    return twin, cousin, sexy

twin, cousin, sexy = prime_pairs(50)
print(f"twin: {twin}\ncousin: {cousin}\nsexy: {sexy}")