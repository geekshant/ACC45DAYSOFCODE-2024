def minimum_operations(X, Y):
    operations = 0
    while X < 2 * Y and Y < 2 * X:
        if X < Y:
            X += 1
        else:
            Y += 1
        operations += 1
    return operations

def main():
    T = int(input("Enter the number of test cases (1-81): "))
    results = []

    for _ in range(T):
        X, Y = map(int, input("Enter the values of X and Y separated by a space: ").split())
        results.append(minimum_operations(X, Y))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
