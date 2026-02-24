def calc_perfect_numbers(max_exclusive):
    numbers = []
    for i in range(2, max_exclusive):
        divisors=[]
        for j in range(1, i):
            if i%j==0:
                divisors.append(j)
        
        if sum(divisors)==i:
            numbers.append(i)

    print(numbers)

calc_perfect_numbers(1000)
