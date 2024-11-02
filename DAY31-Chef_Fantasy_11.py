def possible_choices(N):
    # The number of ways to choose 2 out of N players
    return N * (N - 1)

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of players Chef is considering: "))
        results.append(possible_choices(N))

    print("\nPossible choices for each test case:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
