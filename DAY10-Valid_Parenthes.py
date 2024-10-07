def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top_element = stack.pop() if stack else '#'
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)
    
    return not stack

if __name__ == "__main__":
    # Take input from the user
    s = input("Enter the string containing brackets: ")
    
    # Check if the input string is valid
    result = isValid(s)
    print(f"Is the input string valid? {'Yes' if result else 'No'}")
