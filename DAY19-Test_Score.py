def can_achieve_score(N, X, Y):
    # Check if Y is a multiple of X and does not exceed N * X
    return "YES" if Y % X == 0 and Y <= N * X else "NO"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X, Y = map(int, input("Enter N, X, and Y separated by spaces: ").split())
        results.append(can_achieve_score(N, X, Y))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
