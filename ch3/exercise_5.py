def sum_rec(values):
    if len(values) == 0:  
        return 0
    return values[0] + sum_rec(values[1:])  

values = input("Enter numbers separated by space: ").split()
values = [int(x) for x in values]  

result = sum_rec(values)

print("Sum of the list is:", result)
