def is_game_valid(N, X):
    return "YES" if X % N == 0 else "NO"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N, X = map(int, input().split())
        results.append(is_game_valid(N, X))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
