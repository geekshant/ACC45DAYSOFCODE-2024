def determine_best_offer(A, B):
    valuation_first_investor = A * 10  # Since A is for 10% of the company
    valuation_second_investor = B * 5  # Since B is for 20% of the company

    if valuation_first_investor > valuation_second_investor:
        return "FIRST"
    elif valuation_first_investor < valuation_second_investor:
        return "SECOND"
    else:
        return "ANY"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B = map(int, input("Enter the offers from first and second investors separated by spaces: ").split())
        results.append(determine_best_offer(A, B))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
