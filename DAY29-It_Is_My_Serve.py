def find_server(P, Q):
    # Calculate total points
    total_serves = P + Q
    
    # Determine the group of two serves
    group_number = total_serves // 2
    
    # If group number is even, Alice serves; if odd, Bob serves
    if group_number % 2 == 0:
        return "Alice"
    else:
        return "Bob"

# Input reading
T = int(input("Enter the number of test cases: "))
results = []
for _ in range(T):
    P, Q = map(int, input("Enter scores for Alice and Bob: ").split())
    # Append the result of each test case
    results.append(find_server(P, Q))

# Output all results
print("\n".join(results))
