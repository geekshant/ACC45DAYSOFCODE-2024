def count_odd_even_pairs(N):
    # Count the number of odd and even numbers up to N
    odd_count = (N + 1) // 2
    even_count = N // 2
    # The number of pairs (A, B) such that A + B is odd
    return odd_count * even_count *2

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("enter the numbers: "))
        results.append(count_odd_even_pairs(N))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
