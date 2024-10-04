def can_complete_assignments(X):
    # Start time + 3 hours should be <= 10 PM (22:00)
    if X + 3 <= 102:
        return "Yes"
    else:
        return "No"

def main():
    T = int(input("Enter the number of test cases (1-10): "))
    if not (1 <= T <= 10):
        raise ValueError("The number of test cases must be between 1 and 10.")
    
    results = []

    for _ in range(T):
        X = int(input("Enter the start time X (1-9): "))
        if not (1 <= X <= 9):
            raise ValueError("The start time must be between 1 and 9.")
        
        results.append(can_complete_assignments(X))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
