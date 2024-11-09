def max_distance(N, M, A):
    distance = 0
    for i in range(N):
        distance += max(abs(A[i] - 1), abs(A[i] - M))
    return distance

def main():
    T = int(input().strip())
    results = []

    for _ in range(T):
        N, M = map(int, input().strip().split())
        A = list(map(int, input().strip().split()))
        results.append(max_distance(N, M, A))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
