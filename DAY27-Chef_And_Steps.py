def can_traverse(N, K, distances):
    result = ''
    for distance in distances:
        if distance % K == 0:
            result += '1'
        else:
            result += '0'
    return result

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, K = map(int, input("Enter the number of distances and the step length separated by spaces: ").split())
        distances = list(map(int, input("Enter the distances separated by spaces: ").split()))
        results.append(can_traverse(N, K, distances))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
