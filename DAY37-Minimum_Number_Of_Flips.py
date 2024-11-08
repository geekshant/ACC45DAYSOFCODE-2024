def min_operations_to_zero_sum(N, A):
    total_sum = sum(A)

    if total_sum == 0:
        return 0

    if N % 2 != 0:
        return -1

    positive_count = A.count(1)
    negative_count = A.count(-1)

    if abs(positive_count - negative_count) % 2 != 0:
        return -1

    operations_needed = abs(positive_count - negative_count) // 2
    return operations_needed

def main():
    T = int(input("enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("enter the number in array: "))
        A = list(map(int, input("enter the array list seperated by space: ").split()))
        results.append(min_operations_to_zero_sum(N, A))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
