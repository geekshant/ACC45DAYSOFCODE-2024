def calculate_skipped_strings(N, strings):
    total_skips = 0
    for i in range(1, N):
        total_skips += abs(strings[i] - strings[i - 1]) - 1
    return total_skips

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of times Chef has to pluck a string: "))
        strings = list(map(int, input("Enter the string numbers Chef has to pluck, separated by spaces: ").split()))
        results.append(calculate_skipped_strings(N, strings))

    print("\nTotal number of strings Chef has to skip for each test case:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
