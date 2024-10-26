def count_tuesdays(N):
    # Count the number of full weeks
    full_weeks = N // 7
    
    # Remaining days after accounting for full weeks
    remaining_days = N % 7

    # Count Tuesdays
    tuesdays = full_weeks
    if remaining_days >= 2:
        tuesdays += 1

    return tuesdays

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of spooky days until Halloween: "))
        results.append(count_tuesdays(N))

    print("\nNumber of Tuesdays until Halloween:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
