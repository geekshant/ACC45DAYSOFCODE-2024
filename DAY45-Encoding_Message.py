def encode_message(N, S):
    # Step 1: Swap characters in pairs
    swapped_message = list(S)
    for i in range(0, N - 1, 2):
        swapped_message[i], swapped_message[i + 1] = swapped_message[i + 1], swapped_message[i]
    swapped_message = ''.join(swapped_message)
    
    # Step 2: Replace each letter with its corresponding letter in the alphabet
    encoded_message = []
    for char in swapped_message:
        if 'a' <= char <= 'z':
            new_char = chr(ord('a') + (ord('z') - ord(char)))
            encoded_message.append(new_char)
        else:
            encoded_message.append(char)
    
    return ''.join(encoded_message)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("enter the number of letters in string: "))
        S = input("enter the string: ")
        results.append(encode_message(N, S))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
