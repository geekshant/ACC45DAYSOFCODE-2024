def canJump(nums):
    max_reach = 0
    for i, jump in enumerate(nums):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + jump)
    return True

if __name__ == "__main__":
    # Take input from the user
    nums = list(map(int, input("Enter the array elements separated by spaces: ").split()))
    
    # Determine if we can reach the last index
    result = canJump(nums)
    print(f"Can reach the last index: {'true' if result else 'false'}")
