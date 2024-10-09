def int_to_roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
        ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
        ]
    roman_num = ''
    for i in range(len(val)):
        while num >= val[i]:
            roman_num += syb[i]
            num -= val[i]
    return roman_num

if __name__ == "__main__":
    # Take input from the user
    num = int(input("Enter an integer to convert to Roman numeral: "))
    
    # Convert integer to Roman numeral
    result = int_to_roman(num)
    
    print(f"The Roman numeral for {num} is: {result}")
