#Recursive

def fib(n):
    if (n==1 or n==2):
        return 1
    return fib(n-1) + fib(n-2)

print(fib (3))

#Iterative

def fibo(n):
    a, b = 0 ,1
    c = a+b
    for i in range(2,n):
        a = b
        b = c
        c = a+b

    print(c)
print(fibo(3))