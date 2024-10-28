def calculate_min_cost(S):
    from collections import Counter
    freq = Counter(S)
    cost = 0
    for count in freq.values():
        cost += (count + 1) // 2
    return cost

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        S = input("Enter the string representing the jewels: ")
        results.append(calculate_min_cost(S))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
