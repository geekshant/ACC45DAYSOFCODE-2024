def is_palindrome(s):
    return s == s[::-1]

def max_deletable_subsequence(n, s):
    if is_palindrome(s):
        return n - 1
    return n - 1 if is_palindrome(s[1:]) or is_palindrome(s[:-1]) else -1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the length of the string: "))
        S = input("Enter the string: ")
        if N > 1 and any(s != S[0] for s in S): # At least two distinct characters
            results.append(N - 2)
        else:
            results.append(-1)
            
    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
