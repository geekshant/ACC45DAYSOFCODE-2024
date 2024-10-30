def min_steps(A, B, K):
    distance = abs(A - B)
    if distance % K == 0:
        return distance // K
    else:
        return distance // K + 1

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        A, B, K = map(int, input("Enter A, B, and K separated by spaces: ").split())
        results.append(min_steps(A, B, K))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
