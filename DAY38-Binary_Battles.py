import math

def calculate_total_time(N, A, B):
    # Calculate number of rounds (log base 2 of N)
    rounds = int(math.log2(N))
    total_time = rounds * A + (rounds - 1) * B
    return total_time

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, A, B = map(int, input().split())
        results.append(calculate_total_time(N, A, B))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
