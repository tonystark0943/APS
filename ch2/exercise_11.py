def calc_friends(max_exclusive):
    friends = {}
    for i in range(2, max_exclusive):
        divisors1 = find_proper_divisors(i)
        sum_div1 = sum(divisors1)
        divisors2 = find_proper_divisors(sum_div1)
        
        sum_div2 = sum(divisors2)
        if i == sum_div2 and sum_div1 != sum_div2:
            friends[i] = sum_div1
    return friends

def find_proper_divisors(i):
    divisors = []

    for d in range(1, int(i ** 0.5) + 1):
        if i % d == 0:
            divisors.append(d)
            other = i // d
            if other != d and other != i:
                divisors.append(other)

    # remove i itself if it slipped in
    if i in divisors:
        divisors.remove(i)

    return divisors

print(find_proper_divisors(220))
