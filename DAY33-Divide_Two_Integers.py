def divide(dividend, divisor):
    # Constants for 32-bit signed integer range
    MAX_INT = 2**31 - 1
    MIN_INT = -2**31
    
    if divisor == 0:
        raise ValueError("Divisor cannot be zero.")
    
    # Check if the result will be positive or negative
    negative = (dividend < 0) ^ (divisor < 0)
    
    # Use absolute values for calculation
    dividend, divisor = abs(dividend), abs(divisor)
    
    # Initialize the quotient
    quotient = 0
    
    # Subtract divisor from dividend until dividend is less than divisor
    while dividend >= divisor:
        temp, multiple = divisor, 1
        while dividend >= (temp << 1):
            temp <<= 1
            multiple <<= 1
        dividend -= temp
        quotient += multiple
    
    if negative:
        quotient = -quotient
    
    # Handle overflow cases
    if quotient < MIN_INT:
        return MIN_INT
    if quotient > MAX_INT:
        return MAX_INT
    
    return quotient

def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))
    
    result = divide(dividend, divisor)
    print(f"The quotient is: {result}")

if __name__ == "__main__":
    main()
