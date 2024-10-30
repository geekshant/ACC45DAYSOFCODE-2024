def recover_array(N, B):
    total_sum = sum(B) // (N + 1)
    A = [b - total_sum for b in B]
    return A

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the size of the array: "))
        B = list(map(int, input("Enter the elements of array B separated by spaces: ").split()))
        results.append(recover_array(N, B))

    print("\nRecovered Arrays:")
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
