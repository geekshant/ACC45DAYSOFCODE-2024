def minimum_moves(N, cards):
    from collections import Counter
    count = Counter(cards)
    most_common = max(count.values())
    return N - most_common

def main():
    T = int(input("Enter the number of test cases (1-100): "))
    if not (1 <= T <= 100):
        raise ValueError("The number of test cases must be between 1 and 100.")
    
    results = []

    for _ in range(T):
        N = int(input("Enter the number of cards on the table (1-100): "))
        if not (1 <= N <= 100):
            raise ValueError("The number of cards must be between 1 and 100.")
        
        cards = list(map(int, input("Enter the card numbers separated by spaces: ").split()))
        if len(cards) != N or any(not (1 <= card <= 10) for card in cards):
            raise ValueError("Each card number must be between 1 and 10, and the length of the list must be N.")
        
        results.append(minimum_moves(N, cards))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
