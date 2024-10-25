def min_operations_to_make_elements_same(arr):
    from collections import Counter
    frequency = Counter(arr)
    max_frequency = max(frequency.values())
    return len(arr) - max_frequency

def main():
    T = int(input("Enter the number of test cases: "))
    results = []

    for _ in range(T):
        N = int(input("Enter the length of the array: "))
        arr = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
        results.append(min_operations_to_make_elements_same(arr))

    print("\nResults:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
