def reverse_string(text):
    if len(text) <= 1:   # Base case
        return text
    return text[-1] + reverse_string(text[:-1])

text = input("Enter a string: ")
result = reverse_string(text)

print("Reversed string:", result)
