def my_pow(x, n):
    return x ** n

def main():
    # Take input from the user
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))
    
    # Calculate x raised to the power n
    result = my_pow(x, n)
    
    print(f"{x} raised to the power of {n} is: {result}")

if __name__ == "__main__":
    main()
