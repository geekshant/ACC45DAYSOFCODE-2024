# Read the number of test cases
T = int(input("enter the number of test cases: ").strip())

# Process each test case
results = []
for _ in range(T):
    L, K = map(int, input("enter the numbers seperated by space: ").strip().split())
    base = L // K
    extra = L % K
    results.append(extra)

# Output results for all test cases
print("\n".join(map(str, results)))
