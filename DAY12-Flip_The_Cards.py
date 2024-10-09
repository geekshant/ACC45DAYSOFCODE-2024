def minimum_flips(N, X):
    return min(X, N - X)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X = map(int, input("Enter the values of N and X separated by a space: ").split())
        results.append(minimum_flips(N, X))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
