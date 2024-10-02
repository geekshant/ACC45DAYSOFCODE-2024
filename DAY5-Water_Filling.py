def check_bottles(B1, B2, B3):
    empty_count = [B1, B2, B3].count(0)
    if empty_count >= 2:
        return "Water filling time"
    else:
        return "Not now"

# Input: number of test cases
T = int(input("Enter the number of test cases: "))
if not (1 <= T <= 1000):
    raise ValueError("the number of test cases should be between 1 and 1000")

results = []

# Process each test case
for _ in range(T):
    B1, B2, B3 = map(int, input("Enter the states of three bottles (0 for empty, 1 for full) separated by spaces: ").split())
    if not (B1 == 0 or B1 == 1) and (B2 == 0 or B2 == 1) and (B3 == 0 or B3 == 1):
        raise ValueError("the value of Bi should be either 0 or 1") 
    results.append(check_bottles(B1, B2, B3))

# Output results for each test case
for result in results:
    print(result)
