def count_substrings(text, value_to_find):
    if len(text) < len(value_to_find):
        return 0
    
    if text[:len(value_to_find)] == value_to_find:
        return 1 + count_substrings(text[len(value_to_find):], value_to_find)
    else:
        return count_substrings(text[1:], value_to_find)
    
text = input("Enter the main text: ")
value_to_find = input("Enter the substring to count: ")

result = count_substrings(text, value_to_find)

print(f"The substring '{value_to_find}' occurs {result} times in '{text}'")
