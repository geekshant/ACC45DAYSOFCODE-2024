def will_chef_pass(N, X, P):
    # Calculate the total score
    score = 3 * X - (N - X)
    # Check if the score is at least P
    return "PASS" if score >= P else "FAIL"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X, P = map(int, input("Enter N, X, and P separated by spaces: ").split())
        results.append(will_chef_pass(N, X, P))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
