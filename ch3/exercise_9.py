def print_pascal(n):
    if n == 1:
        print([1])
        return [1]
    
    prev_row = print_pascal(n - 1)
    
    current_row = [1]  
    for i in range(len(prev_row) - 1):
        current_row.append(prev_row[i] + prev_row[i + 1])
    current_row.append(1)  
    
    print(current_row)
    return current_row  

n = int(input("Enter the number of rows for Pascal's Triangle: "))

if n <= 0:
    print("Please enter a positive integer!")
else:
    print_pascal(n)
