# Read number of test cases
T = int(input("enter the number of test cases: ").strip())

# Process each test case
results = []
for _ in range(T):
    N = int(input("enter the number: ").strip())
    # Calculate the number of Tuesdays
    if N == 1:
        results.append(0)
    else:
        results.append((N - 1) // 7 + 1)

# Print all results for the test cases
print("\n".join(map(str, results)))
