#8a
def is_power_of_2(n):
    if n == 1:          
        return True
    if n == 0 or n % 2 != 0:  
        return False
    return is_power_of_2(n // 2) 
n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer!")
else:
    result = is_power_of_2(n)
    print(n, "is a power of 2:" if result else n, "is NOT a power of 2")

#8b
def power_of(value, exponent):
    if exponent == 0:      
        return 1
    return value * power_of(value, exponent - 1)  
value = int(input("Enter the base (positive integer): "))
exponent = int(input("Enter the exponent (non-negative integer): "))

if value < 0 or exponent < 0:
    print("Please enter positive numbers only!")
else:
    result = power_of(value, exponent)
    print(f"{value}^{exponent} =", result)

#8c
def power_of_iter(value, exponent):
    result = 1
    for _ in range(exponent):
        result *= value
    return result

value = int(input("Enter the base (positive integer): "))
exponent = int(input("Enter the exponent (non-negative integer): "))

if value < 0 or exponent < 0:
    print("Please enter positive numbers only!")
else:
    result = power_of_iter(value, exponent)
    print(f"{value}^{exponent} =", result)
