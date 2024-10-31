def rearrange_array(arr):
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Swap adjacent elements at odd indices
    for i in range(1, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    
    return arr

# Input reading and processing
t = int(input("Enter the number of test cases: "))
results = []
for _ in range(t):
    n = int(input("Enter the size of the array: "))
    arr = list(map(int, input("Enter the elements of the array: ").split()))
    # Rearrange the array and store result
    results.append(" ".join(map(str, rearrange_array(arr))))

# Output all results
print("\n".join(results))
