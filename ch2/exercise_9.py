def calc_armstrong_numbers():
    result = []
    for x in range(1, 10):
        for y in range(10):
            for z in range(10):
                n = x * 100 + y * 10 + z
                if n == x**3 + y**3 + z**3:
                    result.append(n)
    return result

print(calc_armstrong_numbers())