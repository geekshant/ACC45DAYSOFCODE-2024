def calculate_total_duration(N, A, B):
    odd_count = (N + 1) // 2
    even_count = N // 2
    total_duration = (odd_count * B) + (even_count * A)
    return total_duration

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, A, B = map(int, input("Enter N, A, and B separated by spaces: ").split())
        results.append(calculate_total_duration(N, A, B))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
