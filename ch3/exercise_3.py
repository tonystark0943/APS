#3a
def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

result = gcd_recursive(a, b)

print("GCD (Recursive) of", a, "and", b, "is:", result)

#3b
def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

c = int(input("Enter first number: "))
d = int(input("Enter second number: "))

result2 = gcd_iterative(c, d)

print("GCD (Iterative) of", c, "and", d, "is:", result2)

#3c
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

result3 = lcm(x, y)

print("LCM of", x, "and", y, "is:", result3)

