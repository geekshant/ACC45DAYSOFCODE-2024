def max_rent_duration(X, Y):
    return (Y - 1) // X

def main():
    T = int(input("Enter the number of test cases (1-1000): "))
    results = []

    for _ in range(T):
        X, Y = map(int, input("Enter the values of X and Y separated by a space (1 <= X, Y <= 10^9): ").split())
        results.append(max_rent_duration(X, Y))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
