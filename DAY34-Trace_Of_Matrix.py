def max_trace_submatrix(matrix, n):
    max_trace = 0

    for i in range(n):
        for j in range(n):
            current_trace = 0
            k = 0
            while i + k < n and j + k < n:
                current_trace += matrix[i + k][j + k]
                max_trace = max(max_trace, current_trace)
                k += 1

    return max_trace

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the size of the matrix: "))
        matrix = []
        for _ in range(N):
            row = list(map(int, input().split()))
            matrix.append(row)
        results.append(max_trace_submatrix(matrix, N))

    print("\nMaximum Traces:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
