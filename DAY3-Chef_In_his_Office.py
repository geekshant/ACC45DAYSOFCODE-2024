def total_working_hours(X, Y):
    # Calculate total hours from Monday to Thursday
    weekdays_hours = X * 4
    # Add hours for Friday
    total_hours = weekdays_hours + Y
    return total_hours

# Input: number of test cases
T = int(input("Enter the number of test cases: "))

results = []

# Process each test case
for _ in range(T):
    X, Y = map(int, input("Enter X and Y separated by a space: ").strip().split())
    results.append(total_working_hours(X, Y))

# Output results for each test case
for result in results:
    print(result)
    
'''

here if i give X = 8 and Y = 7, 
i will get 39 as output
OR i can use X = 10 and Y = 2 as questionn asked, i will get the desirable output

'''
