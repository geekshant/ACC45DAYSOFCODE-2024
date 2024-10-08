def can_partition_with_odd_product(N, A):
    odd_count = sum(1 for x in A if x % 2 != 0)
    return "YES" if odd_count >= 2 else "NO"

def main():
    T = int(input("Enter the number of test cases: "))
    if not (1 <= T <= 100000):
        raise ValueError("The number of test cases must be between 1 and 100,000.")

    results = []

    for _ in range(T):
        N = int(input("\nEnter the size of the array: "))
        if not (2 <= N <= 100000):
            raise ValueError("The size of the array must be between 2 and 100,000.")
        A = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
        if len(A) != N or any(not (1 <= x <= 1000000000) for x in A):
            raise ValueError("Each element of the array must be between 1 and 1,000,000,000, and the length of the array must be N.")
        results.append(can_partition_with_odd_product(N, A))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
