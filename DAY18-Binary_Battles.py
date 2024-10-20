import math

def total_time(N, A, B):
    rounds = int(math.log2(N))  # Number of rounds is log2(N)
    total_duration = rounds * A + (rounds - 1) * B  # Total time including breaks
    return total_duration

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, A, B = map(int, input("Enter N, A, and B separated by spaces: ").split())
        results.append(total_time(N, A, B))

    print("\nTotal time taken for each test case:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
