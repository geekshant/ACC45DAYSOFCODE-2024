def can_split_animals_evenly(N, animals):
    from collections import Counter
    count = Counter(animals)
    for value in count.values():
        if value % 2 != 0:
            return "NO"
    return "YES"

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the number of animals in the store: "))
        animals = list(map(int, input("Enter the types of animals separated by spaces: ").split()))
        results.append(can_split_animals_evenly(N, animals))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
