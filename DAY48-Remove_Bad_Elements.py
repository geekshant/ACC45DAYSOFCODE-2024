def min_operations_to_make_same(array):
    from collections import Counter
    freq = Counter(array)
    max_frequency = max(freq.values())
    return len(array) - max_frequency

def main():
    T = int(input("Enter the number of test cases: "))
    results = []
    
    for _ in range(T):
        N = int(input("Enter the length of the array: "))
        array = list(map(int, input("Enter the elements of the array: ").split()))
        results.append(min_operations_to_make_same(array))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
