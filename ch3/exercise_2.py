def count_digits(value):
    if value < 0:
        raise ValueError("value must be >= 0")

    if value < 10:
        return 1
    

def calc_sum_of_digits(value):
    if value < 0:
        raise ValueError("value must be >= 0")
    
    if value < 10:
        return value
    remainder = value // 10
    last_digit = value % 10
    
    return calc_sum_of_digits(remainder) + last_digit