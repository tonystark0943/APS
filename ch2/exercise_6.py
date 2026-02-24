def calc_checksum(digits):
    i = 1
    s = 0
    for d in digits:
        s += i * int(d)
        i += 1
    return s % 10

cs = calc_checksum("11111")
print(cs)