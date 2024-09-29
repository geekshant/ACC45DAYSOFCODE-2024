def min_total_cost(N, X):
    # N: This is the number of friends in the group who want to buy Chef-TV subscriptions.
    # X: This is the cost of one Chef-TV subscription in rupees
    # Calculate the number of subscriptions needed
    num_subscriptions = (N + 5) // 6  # Equivalent to math.ceil(N / 6)
    return num_subscriptions * X

# Input: number of test cases
T = int(input("Enter the number of test cases: "))

results = []

# Process each test case
for _ in range(T):
    N, X = map(int, input("Enter N and X separated by a space: ").split())
    results.append(min_total_cost(N, X))

# Output results for each test case
for result in results:
    print(result)


'''

if i give a input of N and X as asked in question which 1 100, 12 250 and 16 135 the output will be 100, 500 and 405 respectively

'''