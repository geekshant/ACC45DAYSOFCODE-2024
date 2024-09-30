def can_obtain_length(N, X):
    if N == X:
        return "YES"
    if N < X:
        return "NO"
    return "YES" if (N - X) % 2 == 0 else "NO"

# Input: number of test cases
T = int(input("Enter the number of test cases: "))

results = []

# Process each test case
for _ in range(T):
    N, X = map(int, input("Enter N and X separated by a space: ").split())
    results.append(can_obtain_length(N, X))

# Output results for each test case
for result in results:
    print(result)