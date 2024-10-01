def can_win_contest(A, B, C, X):
    if 1 <= A <= 10 and 1 <= B <= 10 and 1 <= C <= 10 and 1 <= X <= 10:
        if X in {A, B, C}:
            return "Yes"
        else:
            return "No"
    else:
        return "Invalid input. A, B, C, and X must be between 1 and 10."

# Input: number of test cases
T = int(input("Enter the number of test cases: "))

results = []

# Process each test case
for _ in range(T):
    A, B, C, X = map(int, input("Enter A, B, C, and X separated by spaces: ").split())
    results.append(can_win_contest(A, B, C, X))

# Output results for each test case
for result in results:
    print(result)
