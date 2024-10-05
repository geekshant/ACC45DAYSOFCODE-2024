def is_pseudo_sorted(arr):
    n = len(arr)
    # Check if already sorted
    if arr == sorted(arr):
        return "YES"
    
    for i in range(n - 1):
        # Swap adjacent elements
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        
        # Check if the array becomes sorted after the swap
        if arr == sorted(arr):
            return "YES"
        
        # Swap back to original configuration
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return "NO"

def main():
    T = int(input("Enter the number of test cases (1-1000): "))
    if not (1 <= T <= 1000):
        raise ValueError("The number of test cases must be between 1 and 1000.")
    
    results = []

    for _ in range(T):
        N = int(input("Enter the size of the array (2-10^5): "))
        if not (2 <= N <= 100000):
            raise ValueError("The size of the array must be between 2 and 100,000.")
        
        arr = list(map(int, input(f"Enter {N} space-separated integers (each between 1 and 10^9): ").split()))
        if len(arr) != N or any(not (1 <= x <= 1000000000) for x in arr):
            raise ValueError("Each element of the array must be between 1 and 1,000,000,000, and the length of the array must be N.")
        
        results.append(is_pseudo_sorted(arr))

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
