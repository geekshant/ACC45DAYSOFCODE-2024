def myAtoi(s: str) -> int:
    # Define the 32-bit signed integer limits
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Step 1: Trim leading whitespace
    s = s.lstrip()
    
    # Check if string is empty after trimming
    if not s:
        return 0
    
    # Step 2: Determine the sign
    sign = 1
    index = 0
    if s[0] == '-':
        sign = -1
        index += 1
    elif s[0] == '+':
        index += 1
    
    # Step 3: Read digits and convert to integer
    result = 0
    while index < len(s) and s[index].isdigit():
        result = result * 10 + int(s[index])
        index += 1
    
    # Apply the sign to the result
    result *= sign
    
    # Step 4: Clamp the result within 32-bit integer bounds
    if result < INT_MIN:
        return INT_MIN
    elif result > INT_MAX:
        return INT_MAX
    return result

# Take input from the user
user_input = input("Enter a string to convert to an integer: ")
converted_integer = myAtoi(user_input)
print("Converted integer:", converted_integer)
