def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s
    
    # Create an array of strings for each row
    rows = [''] * numRows
    cur_row = 0
    going_down = False
    
    # Place each character in the appropriate row
    for char in s:
        rows[cur_row] += char
        if cur_row == 0 or cur_row == numRows - 1:
            going_down = not going_down
        cur_row += 1 if going_down else -1
    
    # Combine the rows to get the final string
    return ''.join(rows)

if __name__ == "__main__":
    # Take input from the user
    s = input("Enter the string to be converted: ")
    numRows = int(input("Enter the number of rows: "))
    
    # Convert the string using the zigzag pattern
    result = convert(s, numRows)
    print(f"The converted string is: {result}")
