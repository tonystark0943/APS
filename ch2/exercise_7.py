#7a
def from_roman_number(roman_number):
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev = 0
    for ch in reversed(roman_number):
        val = values[ch]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

print(from_roman_number("XVII"))

#7b
def to_roman_number(value):
    numerals = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ''
    for n, s in numerals:
        while value >= n:
            result += s
            value -= n
    return result

print(to_roman_number(17))