def find_coin_position(N, X, S, swaps):
    current_position = X

    for A, B in swaps:
        if current_position == A:
            current_position = B
        elif current_position == B:
            current_position = A

    return current_position

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X, S = map(int, input("Enter N, X, and S separated by spaces: ").split())
        swaps = []
        for _ in range(S):
            A, B = map(int, input().split())
            swaps.append((A, B))
        results.append(find_coin_position(N, X, S, swaps))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
