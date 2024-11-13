def remove_anagrams(words):
    i = 1
    while i < len(words):
        if sorted(words[i]) == sorted(words[i - 1]):
            words.pop(i)
        else:
            i += 1
    return words

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        words = input("Enter words separated by spaces: ").split()
        results.append(remove_anagrams(words))

    print("\nResults:")
    for result in results:
        print(" ".join(result))

if __name__ == "__main__":
    main()
