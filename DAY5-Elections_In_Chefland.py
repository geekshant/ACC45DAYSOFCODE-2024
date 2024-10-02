def determine_winner(XA, XB, XC):
    if XA > 50:
        return "A"
    elif XB > 50:
        return "B"
    elif XC > 50:
        return "C"
    else:
        return "NOTA"

# Read the number of test cases
T = int(input("enter the number of test cases: "))
if not (1 <= T <= 500):
    raise ValueError("the number of test cases should be between 1 and 500")

results = []

# Process each test case
for _ in range(T):
    XA, XB, XC = map(int, input("enter the voting numbers for each party XA, XB & XC seperated by space: ").split())
    if not (0 <= XA <= 101) and (0 <= XB <= 101) and (0 <= XC <= 101) and (XA + XB + XC == 101):
        raise ValueError("the number of votes should be between 1 and 101 and the sum of votes should be 101")
    results.append(determine_winner(XA, XB, XC))

# Output results for each test case
for result in results:
    print(result)
