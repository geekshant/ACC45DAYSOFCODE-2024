def plusOne(digits):
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0

    return [1] + digits

if __name__ == "__main__":
    # Take input from the user
    digits = list(map(int, input("Enter the digits of the large integer separated by spaces: ").split()))
    
    # Increment the large integer by one
    result = plusOne(digits)
    print("Result after incrementing by one:", result)
