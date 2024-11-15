def can_transform(start, result):
    if len(start) != len(result):
        return False

    # Remove all 'X' characters and check if the remaining characters and their order match
    start_no_x = start.replace("X", "")
    result_no_x = result.replace("X", "")
    if start_no_x != result_no_x:
        return False

    # Use two pointers to check if the transformation is valid
    i, j = 0, 0
    while i < len(start) and j < len(result):
        # Skip 'X' characters in both strings
        while i < len(start) and start[i] == 'X':
            i += 1
        while j < len(result) and result[j] == 'X':
            j += 1

        # If one pointer reaches the end, the other must also reach the end
        if (i < len(start)) != (j < len(result)):
            return False

        if i < len(start) and j < len(result):
            # If the characters at the pointers don't match, return False
            if start[i] != result[j]:
                return False
            # Check valid move
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i += 1
            j += 1

    return True

def main():
    start = input("Enter the starting string: ")
    result = input("Enter the resulting string: ")

    if can_transform(start, result):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()
