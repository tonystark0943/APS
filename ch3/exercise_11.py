def calc_permutations(text):
    if len(text) == 1:
        return [text]  
    
    permutations = set()  
    for i in range(len(text)):
        remaining = text[:i] + text[i+1:]
        for perm in calc_permutations(remaining):
            permutations.add(text[i] + perm)
    
    return list(permutations)  
text = input("Enter a string to calculate all permutations: ")

result = calc_permutations(text)

print("All permutations of", text, "are:")
for p in result:
    print(p)
print("Total permutations:", len(result))
