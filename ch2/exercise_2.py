def number_as_text(n):
    str_num = str(n)
    value_to_text = ""
    
    digit_words = {
        '0': "ZERO",
        '1': "ONE",
        '2': "TWO",
        '3': "THREE",
        '4': "FOUR",
        '5': "FIVE",
        '6': "SIX",
        '7': "SEVEN",
        '8': "EIGHT",
        '9': "NINE"
    }
    
    for digit in str_num:
        value_to_text += digit_words[digit] + " "
    
    return value_to_text.strip()

nat = number_as_text(67)
print(nat)  
