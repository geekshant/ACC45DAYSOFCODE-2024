def calculate_total_price(A, B, C):
    # Find the sum of the two highest prices
    total_price = A + B + C - min(A, B, C)
    return total_price

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B, C = map(int, input("Enter the prices of the three items separated by spaces: ").split())
        results.append(calculate_total_price(A, B, C))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
