def count_contest_problems(T, test_cases):
    results = []
    for case in test_cases:
        N, contest_codes = case
        start38_count = contest_codes.count('START38')
        ltime108_count = contest_codes.count('LTIME108')
        results.append((start38_count, ltime108_count))
    return results

def main():
    T = int(input("Enter the number of test cases: "))
    test_cases = []

    for _ in range(T):
        N = int(input())
        contest_codes = input().split()
        test_cases.append((N, contest_codes))

    results = count_contest_problems(T, test_cases)

    print("\nResults:")
    for start38_count, ltime108_count in results:
        print(start38_count, ltime108_count)

if __name__ == "__main__":
    main()
