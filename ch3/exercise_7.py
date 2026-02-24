#7a

def to_binary(n):
    if n < 0:
        raise ValueError("n must be >= 0")
    
    if n <= 1:
        return str(n)
    remainder, last_digit = divmod(n, 2)
    
    return to_binary(remainder) + str(last_digit)

number = int(input("Enter a non-negative integer: "))
binary_representation = to_binary(number)
print(f"The binary representation of {number} is: {binary_representation}")

#7b

def to_octal(n):
    if n < 8:  
        return str(n)
    return to_octal(n // 8) + str(n % 8)
def to_hex(n):
    hex_digits = "0123456789ABCDEF" 
    if n < 16:  
        return hex_digits[n]
    return to_hex(n // 16) + hex_digits[n % 16]
n = int(input("Enter a positive integer: "))

if n < 0:
    print("Please enter a positive integer!")
else:
    octal_result = to_octal(n)
    hex_result = to_hex(n)
    print("Octal representation of", n, "is:", octal_result)
    print("Hexadecimal representation of", n, "is:", hex_result)
