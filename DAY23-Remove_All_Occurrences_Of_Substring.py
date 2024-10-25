def remove_occurrences(s, part):
    while part in s:
        s = s.replace(part, "", 1)
    return s

def main():
    # Take input from the user
    s = input("Enter the main string: ")
    part = input("Enter the substring to remove: ")
    
    # Remove all occurrences of the substring
    result = remove_occurrences(s, part)
    
    print(f"Resulting string after removing all occurrences of '{part}': {result}")

if __name__ == "__main__":
    main()
