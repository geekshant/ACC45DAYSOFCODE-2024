def is_palindrome(x):
    str_x = str(x)
    return str_x == str_x[::-1]

def main():
    # Take input from the user
    x = int(input("Enter an integer: "))
    
    # Check if the integer is a palindrome
    result = is_palindrome(x)
    
    print(f"Is {x} a palindrome? {'Yes' if result else 'No'}")

if __name__ == "__main__":
    main()
