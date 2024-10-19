def travel_time_comparison(T, cases):
    results = []
    for X, Y in cases:
        if X < Y:
            results.append("BIKE")
        elif Y < X:
            results.append("CAR")
        else:
            results.append("SAME")
    return results

def main():
    T = int(input("Enter the number of test cases: "))
    cases = []

    for _ in range(T):
        X, Y = map(int, input("Enter the travel times for bike and car separated by a space: ").split())
        cases.append((X, Y))

    results = travel_time_comparison(T, cases)

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
