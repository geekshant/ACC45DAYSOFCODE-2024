def longest_common_prefix(strs):
    if not strs:
        return "", 0
    
    # Start with the first string in the array as the common prefix
    common_prefix = strs[0]
    
    for string in strs[1:]:
        while string[:len(common_prefix)] != common_prefix:
            common_prefix = common_prefix[:-1]
            if not common_prefix:
                return "", 0
                
    count = sum(1 for s in strs if s.startswith(common_prefix))
    return common_prefix, count

if __name__ == "__main__":
    # Take the number of strings as input
    n = int(input("Enter the number of strings: "))
    
    # Take all the strings as input in one line, separated by spaces
    input_str = input(f"Enter {n} strings separated by space: ")
    strs = input_str.split()
    
    # Find the longest common prefix
    result, count = longest_common_prefix(strs)
    print(f"The longest common prefix is: '{result}' which appears {count} times")
