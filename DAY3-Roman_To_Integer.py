def romanToInt(s: str) -> int:
    roman_to_int = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    
    total = 0
    prev_value = 0
    
    for char in reversed(s):
        current_value = roman_to_int[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
        
    return total

# This part is to take user input
if __name__ == "__main__":
    try:
        roman_numeral = input("Enter a Roman numeral: ").strip().upper()
        result = romanToInt(roman_numeral)
        print(f"The integer value of the Roman numeral {roman_numeral} is {result}")
    except Exception as e:
        print(f"An error occurred: {e}")