def swap_adjacent_characters(s):
    swapped = list(s)
    for i in range(0, len(s) - 1, 2):
        swapped[i], swapped[i + 1] = swapped[i + 1], swapped[i]
    return ''.join(swapped)

def replace_characters(s):
    replaced = []
    for char in s:
        new_char = chr(ord('z') - (ord(char) - ord('a')))
        replaced.append(new_char)
    return ''.join(replaced)

def encode_message(N, S):
    swapped_message = swap_adjacent_characters(S)
    encoded_message = replace_characters(swapped_message)
    return encoded_message

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the length of the message: "))
        S = input("Enter the message string: ")
        results.append(encode_message(N, S))

    print("\nEncoded Messages:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
