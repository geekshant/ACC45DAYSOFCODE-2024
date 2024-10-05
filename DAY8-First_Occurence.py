def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

if __name__ == "__main__":
    # Take input from the user
    haystack = input("Enter the haystack string: ")
    needle = input("Enter the needle string: ")
    
    # Find the first occurrence of needle in haystack
    result = strStr(haystack, needle)
    print(f"The index of the first occurrence of '{needle}' in '{haystack}' is: {result}")
