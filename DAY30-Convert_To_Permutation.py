def min_operations_to_permutation(N, A):
    count = [0] * (N + 1)
    for num in A:
        if num <= N:
            count[num] += 1
    
    missing = [i for i in range(1, N + 1) if count[i] == 0]
    operations = 0
    j = 0

    for i in range(N):
        if A[i] > N or count[A[i]] > 1:
            if j < len(missing):
                operations += missing[j] - A[i]
                j += 1

    if j != len(missing):
        return -1

    return operations

def main():
    T = int(input("enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("enter the numbers of number in array: "))
        A = list(map(int, input("enter the numbers of array: ").split()))
        results.append(min_operations_to_permutation(N, A))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
