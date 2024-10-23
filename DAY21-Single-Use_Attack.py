def minimum_attacks(H, X, Y):
    # Check if using the special attack will help
    if H <= Y:
        return 1
    else:
        # Use the special attack once
        remaining_health = H - Y
        # Calculate the remaining attacks needed
        regular_attacks = (remaining_health + X - 1) // X  # ceiling division
        return regular_attacks + 1  # Adding the special attack

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        H, X, Y = map(int, input("Enter H, X, and Y separated by spaces: ").split())
        results.append(minimum_attacks(H, X, Y))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
