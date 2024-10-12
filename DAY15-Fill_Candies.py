import math

def minimum_bags(N, K, M):
    capacity_per_bag = K * M
    return (N + capacity_per_bag - 1) // capacity_per_bag

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, K, M = map(int, input("Enter the values of N, K, and M separated by spaces: ").split())
        results.append(minimum_bags(N, K, M))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
