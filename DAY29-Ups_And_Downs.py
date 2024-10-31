def rearrange_array(N, A):
    for i in range(N - 1):
        if i % 2 == 0:
            if A[i] > A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
        else:
            if A[i] < A[i + 1]:
                A[i], A[i + 1] = A[i + 1], A[i]
    return A

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the size of the array: "))
        A = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
        results.append(rearrange_array(N, A))

    print("\nRearranged Arrays:")
    for result in results:
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()
