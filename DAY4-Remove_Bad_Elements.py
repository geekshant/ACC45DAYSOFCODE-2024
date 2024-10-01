def min_operations_to_make_elements_same(arr):
    from collections import Counter
    count = Counter(arr)
    most_frequent_count = max(count.values())
    return len(arr) - most_frequent_count

if __name__ == "__main__":
    # Input: number of test cases
    T = int(input("Enter the number of test cases: "))
    
    results = []
    
    for _ in range(T):
        N = int(input("Enter the length of the array: "))
        A = list(map(int, input(f"Enter {N} space-separated integers: ").split()))
        results.append(min_operations_to_make_elements_same(A))
    
    # Output results for each test case
    for result in results:
        print(f"the minimum number of operations required to make all the elements same: {result}")