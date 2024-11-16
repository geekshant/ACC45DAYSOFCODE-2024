def minimum_coins_required(N):
    full_sets = N // 5
    remaining_gifts = N % 5
    total_coins = (full_sets * 4) + remaining_gifts
    return total_coins

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of gifts: "))
        results.append(minimum_coins_required(N))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
