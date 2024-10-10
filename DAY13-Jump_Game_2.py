def min_jumps(nums):
    n = len(nums)
    if n == 1:
        return 0
    
    max_reach = nums[0]
    step = nums[0]
    jumps = 1

    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        max_reach = max(max_reach, i + nums[i])
        step -= 1
        
        if step == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            step = max_reach - i
    
    return -1

if __name__ == "__main__":
    # Take input from the user
    nums = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    # Calculate the minimum number of jumps to reach the last index
    result = min_jumps(nums)
    
    print(f"The minimum number of jumps to reach the last index is: {result}")
