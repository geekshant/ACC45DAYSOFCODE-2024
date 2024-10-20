def balanced_reversal(N, A):
    count_0 = A.count('0')
    count_1 = N - count_0  # Remaining characters must be '1' since length of A is N
    return '0' * count_0 + '1' * count_1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the value of N: "))
        A = input("Enter the value of A: ").strip()
        results.append(balanced_reversal(N, A))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
