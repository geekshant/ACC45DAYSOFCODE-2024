def generate_substitution_table(key):
    # Create an empty dictionary for the substitution table
    substitution_table = {}
    # Initialize a set to keep track of seen characters
    seen = set()
    # Initialize the current alphabet letter
    current_letter = 'a'
    
    # Iterate through each character in the key
    for char in key:
        if char.isalpha() and char not in seen:
            # Add the character to the substitution table
            substitution_table[char] = current_letter
            # Add the character to the seen set
            seen.add(char)
            # Move to the next alphabet letter
            current_letter = chr(ord(current_letter) + 1)
            if current_letter > 'z':
                break
    
    return substitution_table

def decode_message(key, message):
    # Generate the substitution table
    substitution_table = generate_substitution_table(key)
    
    # Decode the message
    decoded_message = []
    for char in message:
        if char == ' ':
            decoded_message.append(' ')
        else:
            decoded_message.append(substitution_table.get(char, char))
    
    return ''.join(decoded_message)

def main():
    key = input("Enter the cipher key: ")
    message = input("Enter the secret message: ")
    
    result = decode_message(key, message)
    print("Decoded message:", result)

if __name__ == "__main__":
    main()
