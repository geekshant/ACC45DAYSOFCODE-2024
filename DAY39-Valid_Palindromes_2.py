def is_palindrome_range(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def valid_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return is_palindrome_range(s, left + 1, right) or is_palindrome_range(s, left, right - 1)
        left += 1
        right -= 1
    return True

def main():
    s = input("Enter the string: ")
    result = valid_palindrome(s)
    print("Can the string be a palindrome after deleting at most one character?", result)

if __name__ == "__main__":
    main()
