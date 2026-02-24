def is_number_palindrome(number):
    if number < 10:
        return True

    n = number
    digits = 0
    while n > 0:
        n //= 10
        digits += 1

    first_digit = number // (10 ** (digits - 1))
    last_digit = number % 10

    if first_digit != last_digit:
        return False

    middle_number = (number % (10 ** (digits - 1))) // 10

    return is_number_palindrome(middle_number)

number = int(input("Enter a positive integer: "))

if number < 0:
    print("Please enter a positive integer!")
else:
    result = is_number_palindrome(number)
    print(number, "is a palindrome:" if result else number, "is NOT a palindrome")
