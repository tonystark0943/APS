def calc_max_possible_change(values):
    sorted_numbers = list(values)
    sorted_numbers.sort()
    max_possible_change = 0

    for current_value in sorted_numbers:
        if current_value > max_possible_change + 1:
            break
        max_possible_change += current_value
    return max_possible_change

print(calc_max_possible_change([1,2,4]))

