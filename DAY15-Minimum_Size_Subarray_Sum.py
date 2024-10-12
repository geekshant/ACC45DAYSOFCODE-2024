def min_subarray_len(target, nums):
    n = len(nums)
    min_length = float('inf')
    current_sum = 0
    start = 0
    
    for end in range(n):
        current_sum += nums[end]
        
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)
            current_sum -= nums[start]
            start += 1
    
    return min_length if min_length != float('inf') else 0

if __name__ == "__main__":
    # Take input from the user
    target = int(input("Enter the target sum: "))
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    # Calculate the minimal length of the subarray
    result = min_subarray_len(target, nums)
    
    print(f"The minimal length of a subarray whose sum is greater than or equal to {target} is: {result}")
